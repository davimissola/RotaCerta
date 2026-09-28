import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
import httpx
from services.services_maps import criar_rotas_adicionais
from schemas.maps import GoogleMapsRouteResponse




load_dotenv()
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')



router = APIRouter(prefix='/maps',
                   tags=['MAPS'])


@router.get('/autocomplete/{endereco}')
async def maps_autocomplete(endereco: str):
    if not GOOGLE_MAPS_API_KEY:
        raise HTTPException(status_code=500, detail='API do Google Maps não está configurada.')

    url = 'https://places.googleapis.com/v1/places:autocomplete'
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': GOOGLE_MAPS_API_KEY,
    }
    payload = {
        'input': endereco,
        'locationBias': {
            'circle': {
                'center': {
                    'latitude': -22.902222,
                    'longitude': -47.067222
                },
                'radius': 500.0
            }
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url=url, headers=headers, json=payload)

    return response.json()



@router.get('/route/{endereco}')
async def maps_route(endereco: str):
    print(endereco)
    if not GOOGLE_MAPS_API_KEY:
        raise HTTPException(status_code=500, detail='API do Google Maps não está configurada.')

    url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': GOOGLE_MAPS_API_KEY,
        'X-Goog-FieldMask': 'routes.polyline,routes.duration,routes.distanceMeters', 
    }
    payload = {
        'origin': {
                'location': {
                    'latLng': {
                        'latitude': -22.90116,
                        'longitude': -47.06168,
                    }
                }
            # comentarios sao o jeito padrao, acima foi um teste
            # 'address': 'Colégio Técnico de Campinas - Unicamp - Rua Culto à Ciência - Centro, Campinas - SP, Brasil' # alterar pra localização atual do usuario
        },
        'destination': {
                'location': {
                    'latLng': {
                        'latitude': -22.91307,
                        'longitude': -47.05554,
                    }
                }
            # 'address': endereco
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
            # criar_rotas_adicionais(response)

            return response.json()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
    