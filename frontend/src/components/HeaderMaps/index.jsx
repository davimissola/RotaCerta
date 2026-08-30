import { useEffect, useRef, useState } from 'react'
import { MenuDrawer } from '../MenuDrawer'
import './header-maps.css'



export function HeaderMaps() {
    const inputEndereco = useRef(null)
    const [endereco, setEndereco] = useState('')
    const [sugestaoEndereco, setSugestaoEndereco] = useState([])

    // mandar pro backend
    async function handleSubmit(e) {
        e.preventDefault()

        await fetch(`http://127.0.0.1:8000/maps/route/${endereco}`)
            .then(reponse => reponse.json())
            .then(data => console.log(data))
    }

    // autocomplete
    useEffect(() => {
        if (!endereco) {
            setSugestaoEndereco([])
            return
        }

        const timeout = setTimeout(async () => {
            const response = await fetch('https://places.googleapis.com/v1/places:autocomplete', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    "X-Goog-Api-Key": "AIzaSyBZsvi_7gi5HnUk_eF1XRRTJeHxD9blvrU"
                },
                body: JSON.stringify({
                    'input': endereco,
                    "locationBias": {
                        "circle": {
                            "center": {
                                "latitude": -22.902222,
                                "longitude": -47.067222
                            },
                            "radius": 500.0
                        }
                    }
                })
            })

            const data = await response.json()
            const enderecos = data?.suggestions ?? []
            setSugestaoEndereco(enderecos.slice(0, 5))
        }, 600)

        return () => clearTimeout(timeout)
    }, [endereco])



    return (
        <header>
            <button className='button-menu'>
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-menu-icon lucide-menu"><path d="M4 5h16"/><path d="M4 12h16"/><path d="M4 19h16"/></svg>
            </button>
            <MenuDrawer open={false} />

            <form onSubmit={handleSubmit}>
                <input 
                    type="text"
                    placeholder='Para onde vai hoje?'
                    value={endereco}
                    onChange={(e) => setEndereco(e.target.value)}
                    ref={inputEndereco}
                />

                {sugestaoEndereco.length > 0 ? (
                    <div className="div-sugestao-endereco">
                        {sugestaoEndereco.map(sugestao => {
                            return (
                                <button 
                                    key={sugestao.placePrediction.placeId} 
                                    className='button-sugestao-endereco'
                                    onClick={() => setEndereco(sugestao.placePrediction.text.text)}
                                    type='submit'
                                    >
                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-map-pin-icon lucide-map-pin"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/></svg>
                                        <div>
                                            {sugestao.placePrediction.structuredFormat.mainText.text}
                                            <span>{sugestao.placePrediction.structuredFormat.secondaryText.text}</span>
                                        </div>
                                </button>
                            )
                        })}
                    </div>
                ) : null}
            </form>
        </header>
    )
}