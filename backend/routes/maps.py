import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
import httpx




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
    except Exception as e:
        print(e)
    return data