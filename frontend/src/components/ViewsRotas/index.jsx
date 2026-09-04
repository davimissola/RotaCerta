import { useRef, useState } from 'react'
import './views-rotas.css'


export function ViewsRotas({ routes }) {
    const sectionViews = useRef(null)

    const [openViews, setOpenViews] = useState(false)

    return (
        <section className='section-views-rotas' ref={sectionViews} style={{height: openViews ? '90%' : '15%'}}>
            <div className='views-rotas-line' onClick={() => setOpenViews(!openViews)}/>
            
            <div className="div-radio-rota">
                <input type="radio" id="opcao1" name="escolha" value="opcao1" defaultChecked />
                <label htmlFor="opcao1">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-shield-user-icon lucide-shield-user"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="M6.376 18.91a6 6 0 0 1 11.249.003"/><circle cx="12" cy="11" r="4"/></svg>
                    Rota recomendada
                </label>

                <input type="radio" id="opcao2" name="escolha" value="opcao2" />
                <label htmlFor="opcao2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-lock-icon lucide-lock"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                    Rota mais segura
                </label>

                <input type="radio" id="opcao3" name="escolha" value="opcao3" />
                <label htmlFor="opcao3">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-gauge-icon lucide-gauge"><path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/></svg>
                    Rota mais rápida
                </label>
            </div>
            
            { routes?.routes?.length > 0 && (
                <div className="div-show-routes">
                    { routes.routes.map(route => {
                        return (
                            <div className='div-route'>  
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"><path d="M199.2 181.4L173.1 256L466.9 256L440.8 181.4C436.3 168.6 424.2 160 410.6 160L229.4 160C215.8 160 203.7 168.6 199.2 181.4zM103.6 260.8L138.8 160.3C152.3 121.8 188.6 96 229.4 96L410.6 96C451.4 96 487.7 121.8 501.2 160.3L536.4 260.8C559.6 270.4 576 293.3 576 320L576 512C576 529.7 561.7 544 544 544L512 544C494.3 544 480 529.7 480 512L480 480L160 480L160 512C160 529.7 145.7 544 128 544L96 544C78.3 544 64 529.7 64 512L64 320C64 293.3 80.4 270.4 103.6 260.8zM192 368C192 350.3 177.7 336 160 336C142.3 336 128 350.3 128 368C128 385.7 142.3 400 160 400C177.7 400 192 385.7 192 368zM480 400C497.7 400 512 385.7 512 368C512 350.3 497.7 336 480 336C462.3 336 448 350.3 448 368C448 385.7 462.3 400 480 400z"/></svg>
                                <div className='route-infos'>
                                    <div>
                                        <h3>Rota mais segura</h3>
                                        <h4>89% segurança</h4>            
                                    </div>
                                    <div>
                                        <p>{(route.distanceMeters / 1000).toFixed(1)}km</p>                              
                                        <p>{(route.duration.replace('s', '') / 60).toFixed(0)} min</p>                       
                                    </div>
                                </div>
                            </div>
                        )
                    })}
                </div>
            )}

        </section>
    )
}