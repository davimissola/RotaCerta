import { useRef, useState } from 'react'
import './views-rotas.css'


export function ViewsRotas() {
    const sectionViews = useRef(null)

    const [openViews, setOpenViews] = useState(false)
    function onOpenViews() {
        setOpenViews(!openViews)
    }
    return (
        <section className='section-views-rotas' ref={sectionViews} style={{height: openViews ? '90%' : '15%'}}>
            <div className='views-rotas-line' onClick={() => onOpenViews()}/>
            
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
        </section>
    )
}