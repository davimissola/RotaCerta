from pydantic import BaseModel



class Polyline(BaseModel):
    encodedPolyline: str


class GoogleMapsRoute(BaseModel):
    distanceMeters: int
    duration: str
    polyline: Polyline


class GoogleMapsRouteResponse(BaseModel):
    routes: list[GoogleMapsRoute]