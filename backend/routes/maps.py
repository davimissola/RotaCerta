import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
import httpx
from services.services_maps import ServicesMaps




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


@router.get('/route/{destino}')
async def maps_route(destino: str):
    origem = 'Colégio Técnico de Campinas - Unicamp, R. Culto à Ciência, 177 - Centro, Campinas - SP, 13020-060'
    if not GOOGLE_MAPS_API_KEY:
        raise HTTPException(status_code=500, detail='API do Google Maps não está configurada.')

    try:
        service_maps = ServicesMaps(GOOGLE_MAPS_API_KEY)
        response = await service_maps.buscar_rotas_api(
            origem, 
            destino, 
            tipo_localizacao='endereco'
            )
        todas_subrotas = await service_maps.criar_rotas_adicionais(response)
        todas_combinacoes = service_maps.combinar_subrotas(todas_subrotas)
        routes = service_maps.juntar_combinacoes(todas_combinacoes)
            
        return routes
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))