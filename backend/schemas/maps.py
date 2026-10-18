from pydantic import BaseModel


"""
Schema pras instanciações de rota e decodificação futura de polilinha do maps
"""

class Polyline(BaseModel):
    encodedPolyline: str


class GoogleMapsRoute(BaseModel):
    distanceMeters: int
    duration: str
    polyline: Polyline


class GoogleMapsRouteResponse(BaseModel):
    routes: list[GoogleMapsRoute]
