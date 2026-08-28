// API KEY GOOGLE -> AIzaSyAbBtqKTwT0CYeXFkMWSCgrajNJlVfHMfo - AIzaSyAbBtqKTwT0CYeXFkMWSCgrajNJlVfHMfo
import './maps.css'
import { useEffect } from 'react'




export function Maps() {

    useEffect(() => {
        async function carregarMapa() {
            try {
                const mapsApi = window.google?.maps

                if (!mapsApi) {
                    throw new Error('A API do Google Maps ainda não está disponível.')
                }

                await mapsApi.importLibrary('maps')
            } catch (error) {
                console.error('Não foi possível carregar o Google Maps.', error)
            }
        }
        carregarMapa()
    }, [])
    return (
        <section className="maps-container">
            <gmp-map
                center="-22.902222, -47.067222"
                zoom="13"
                map-id="DEMO_MAP_ID"
            ></gmp-map>
        </section>
    )
}