from schemas.maps import GoogleMapsRouteResponse, GoogleMapsRoute
from typing import Literal
import polyline
import httpx
from itertools import product





class ServicesMaps:
    def __init__(self, GOOGLE_MAPS_API_KEY):
        self.chave_api: str = GOOGLE_MAPS_API_KEY


    def decodificar_polyline(self, encodedPolyline: str) -> list[tuple[float, float]]:
        pontos = polyline.decode(
            encodedPolyline,
            precision=5
        )
        return pontos


    async def criar_rotas_adicionais(self, response):
        dados = GoogleMapsRouteResponse.model_validate(response.json())
        todas_subrotas: list[list[list[GoogleMapsRoute]]] = []

        for rota in dados.routes:
            rota_subrotas: list[list[GoogleMapsRoute]] = []
            rota_pontos_intermediarios = self.dividir_rota(rota)

            for i in range(len(rota_pontos_intermediarios)-1):
                origem = rota_pontos_intermediarios[i]
                destino = rota_pontos_intermediarios[i+1]

                response_add = await self.buscar_rotas_api(
                    origem,
                    destino,
                    tipo_localizacao='coordenada'
                    )
                dados_add = GoogleMapsRouteResponse.model_validate(
                    response_add.json()
                    )
                rota_subrotas.append(dados_add.routes)

            todas_subrotas.append(rota_subrotas)

        # todos os segmentos
        return todas_subrotas


    def dividir_rota(self, rota: GoogleMapsRoute):
        pontos = self.decodificar_polyline(rota.polyline.encodedPolyline)

        distancia_metros: int = int(rota.distanceMeters)
        if 2000 > distancia_metros:
            quantidade_segmentos = 1
        elif 8000 > distancia_metros:
            quantidade_segmentos = 2
        elif 16000 > distancia_metros:
            quantidade_segmentos = 3
        else:
            quantidade_segmentos = 4

        rota_pontos_intermediarios: list[tuple[float, float]] = [
            pontos[
                round(i * (len(pontos) - 1) / quantidade_segmentos)
            ]
            for i in range(quantidade_segmentos + 1)
            ]
        return rota_pontos_intermediarios


    def combinar_subrotas(self, todas_subrotas: list[list[list[GoogleMapsRoute]]]):
        todas_combinacoes = []
        for rota_subrotas in todas_subrotas:
            combinacoes_rota = list(
                product(*rota_subrotas)
            )

            todas_combinacoes.append(combinacoes_rota)
        return todas_combinacoes


    def juntar_combinacoes(self, todas_combinacoes: list[list[tuple[GoogleMapsRoute, ...]]]):
        routes = {'routes': []}
        for combinacoes in todas_combinacoes:
            for rota in combinacoes:
                todos_pontos = []
                for subrota in rota:
                    pontos_subrota = self.decodificar_polyline(subrota.polyline.encodedPolyline)

                    if not todos_pontos:
                        todos_pontos.extend(pontos_subrota)
                    else:
                        todos_pontos.extend(pontos_subrota[1:])
                routes['routes'].append(todos_pontos)
        return routes


    async def buscar_rotas_api(self, origem, destino, tipo_localizacao: Literal['endereco', 'coordenada']):
        url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
        headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': self.chave_api,
            'X-Goog-FieldMask': 'routes.polyline,routes.duration,routes.distanceMeters', 
        }
        if tipo_localizacao == 'endereco':
            payload = {
                'origin': {
                    'address': origem
                },
                'destination': {
                    'address': destino
                },
                "travelMode": "DRIVE",
                "routingPreference": "TRAFFIC_AWARE",
                "computeAlternativeRoutes": True,  
                "routeModifiers": {
                    "avoidTolls": False,
                    "avoidHighways": False,
                    "avoidFerries": False
                },
                "languageCode": "pt-BR",
                "units": "METRIC"
            }
        elif tipo_localizacao == 'coordenada':
            payload = {
                'origin': {
                    'location': {
                        'latLng': {
                            "latitude": origem[0],
                            "longitude": origem[1]
                        }
                    }
                },
                'destination': {
                    'location': {
                        'latLng': {
                            "latitude": destino[0],
                            "longitude": destino[1]
                        }
                    }
                },
                "travelMode": "DRIVE",
                "routingPreference": "TRAFFIC_AWARE",
                "computeAlternativeRoutes": True,  
                "routeModifiers": {
                    "avoidTolls": False,
                    "avoidHighways": False,
                    "avoidFerries": False
                },
                "languageCode": "pt-BR",
                "units": "METRIC"
            }
        else:
            raise Exception('Tipo localização inválida')

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url=url, headers=headers, json=payload)
                return response
        except Exception as e:
            raise Exception(e)

