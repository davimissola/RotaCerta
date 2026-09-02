// API KEY GOOGLE -> AIzaSyBZsvi_7gi5HnUk_eF1XRRTJeHxD9blvrU - 27/08, email cc26125@g.unicamp.br
import './maps.css'
import { useEffect, useRef } from 'react'
import polyline from '@mapbox/polyline';

const MAP_STYLE = [
    { elementType: 'geometry', stylers: [{ color: '#f4f5f6' }] },
    { elementType: 'labels.text.fill', stylers: [{ color: '#59666e' }] },
    { elementType: 'labels.text.stroke', stylers: [{ color: '#f4f5f6' }] },
    { featureType: 'administrative', elementType: 'geometry', stylers: [{ color: '#d4d8dd' }] },
    { featureType: 'administrative.locality', elementType: 'labels.text.fill', stylers: [{ color: '#2d3135' }] },
    { featureType: 'poi', elementType: 'geometry', stylers: [{ color: '#e7e9ec' }] },
    { featureType: 'poi.park', elementType: 'geometry', stylers: [{ color: '#e4eee9' }] },
    { featureType: 'road', elementType: 'geometry', stylers: [{ color: '#ffffff' }] },
    { featureType: 'road', elementType: 'geometry.stroke', stylers: [{ color: '#dfe3e6' }] },
    { featureType: 'road.highway', elementType: 'geometry', stylers: [{ color: '#cbdce3' }] },
    { featureType: 'road.highway', elementType: 'geometry.stroke', stylers: [{ color: '#aebfc7' }] },
    { featureType: 'road.highway', elementType: 'labels.text.fill', stylers: [{ color: '#303d44' }] },
    { featureType: 'water', elementType: 'geometry', stylers: [{ color: '#dcecf3' }] },
    { featureType: 'water', elementType: 'labels.text.fill', stylers: [{ color: '#5f8495' }] },
]



export function Maps({ routes }) {
    const mapContainerRef = useRef(null)
    const mapRef = useRef(null)

    useEffect(() => {
        async function carregarMapa() {
            try {
                const mapsApi = window.google?.maps

                if (!mapsApi) {
                    throw new Error('A API do Google Maps ainda não está disponível.')
                }

                await mapsApi.importLibrary('maps')

                if (mapRef.current || !mapContainerRef.current) {
                    return
                }

                mapRef.current = new mapsApi.Map(mapContainerRef.current, {
                    center: { lat: -22.902222, lng: -47.067222 },
                    zoom: 13,
                    styles: MAP_STYLE,
                    mapTypeControl: false,
                    streetViewControl: false,
                    fullscreenControl: false,
                    clickableIcons: false,
                })
            } catch (error) {
                console.error('Não foi possível carregar o Google Maps.', error)
            }
        }
        carregarMapa()
    }, [])


    // desenhar mapa
    useEffect(() => {
        if (Object.keys(routes).length === 0 || !mapRef.current) return

    }, [routes])


    return (
        <section className="maps-container">
            <div ref={mapContainerRef} className="gmp-map" />
        </section>
    )
}