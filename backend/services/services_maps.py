from schemas.maps import GoogleMapsRouteResponse, GoogleMapsRoute
import polyline



# provavelmente este jeito nao funciona, mas vale aprofundar
def criar_rotas_adicionais(response):
    dados = GoogleMapsRouteResponse.model_validate(response.json())

    i = 0
    for rota in dados.routes:
        i += 1
        print(f'ROTA #{i}')
        print('-------')
        pontos: list[tuple[float, float]] = polyline.decode(
            rota.polyline.encodedPolyline,
            precision=5
        )
        print(pontos)
        print('--------------------')

        valor_intermediario: int = len(pontos) // 3
        pontos_intermediarios: list[tuple[float, float]] = [
            pontos[0],
            pontos[valor_intermediario],
            pontos[valor_intermediario*2],
            pontos[-1],
            ]

        for p in range(len(pontos_intermediarios)-1):
            print(f'{pontos_intermediarios[p]} -----> {pontos_intermediarios[p + 1]}')