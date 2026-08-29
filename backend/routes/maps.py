from fastapi import APIRouter


router = APIRouter(prefix='/maps',
                   tags=['MAPS'])



@router.get('/route/{endereco}')
def maps_route(endereco: str):
    print(endereco)
    return {'endereco': endereco}