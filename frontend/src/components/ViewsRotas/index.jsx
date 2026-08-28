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
            <h2>Veja suas rotas</h2>
        </section>
    )
}