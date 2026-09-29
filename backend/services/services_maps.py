from schemas.maps import GoogleMapsRouteResponse, GoogleMapsRoute
from typing import Literal
import polyline
import httpx





class ServicesMaps:
    def __init__(self, GOOGLE_MAPS_API_KEY):
        self.chave_api: str = GOOGLE_MAPS_API_KEY
        todas_rotas = {} # dicionario com chave 'routes' e dentro de routes uma lista de TODAS as rotas


    async def buscar_rotas_api(self, origem, destino, tipo_localizacao: Literal['endereco', 'coodernada']):
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


    async def criar_rotas_adicionais(self, response):
        dados = GoogleMapsRouteResponse.model_validate(response.json())
        # todos_pontos_intermediarios: list[list[tuple[float, float]]] = []

        for rota in dados.routes:
            rota_pontos_intermediarios = self.dividir_rota(rota)
            # rota_pontos_intermediarios = [(x1, y1), (x2, y2), (x3, y3)]

            for i in range(len(rota_pontos_intermediarios-1)):
                response_add = self.buscar_rotas_api(origem=rota_pontos_intermediarios[i], destino=rota_pontos_intermediarios[i+1], tipo_localizacao='coodernada')
                dados_add = GoogleMapsRouteResponse.model_validate(response_add.json())
                # dados_add_1.routes armazena a lista com a polyline de até 3 rotas de (x1, y1) -> (x2, y2)


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


    def decodificar_polyline(encodedPolyline: str) -> list[tuple[float, float]]:
        pontos = polyline.decode(
            encodedPolyline,
            precision=5
        )
        return pontos