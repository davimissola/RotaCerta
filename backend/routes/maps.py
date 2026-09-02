from fastapi import APIRouter
import httpx

# teste localizaçao -> Avenida do Ipiranga - Ponte Preta, Campinas - SP, Brasil


router = APIRouter(prefix='/maps',
                   tags=['MAPS'])



@router.get('/route/{endereco}')
async def maps_route(endereco: str):
    url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': 'AIzaSyBZsvi_7gi5HnUk_eF1XRRTJeHxD9blvrU', # lembrar de tirar api key do codigo
        'X-Goog-FieldMask': 'routes.polyline,routes.duration,routes.distanceMeters', # routes.legs.polyline,routes.legs.steps.polyline
    }
    payload = {
        'origin': {
            'address': 'Colégio Técnico de Campinas - Unicamp - Rua Culto à Ciência - Centro, Campinas - SP, Brasil' # alterar pra localização atual do usuario
        },
        'destination': {
            'address': endereco
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

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url=url, headers=headers, json=payload)
            data = response.json()
            print(data)
    except Exception as e:
        print(e)
    return data