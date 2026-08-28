import './header-maps.css'



export function HeaderMaps() {
    
    return (
        <header>
            <button>
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-menu-icon lucide-menu"><path d="M4 5h16"/><path d="M4 12h16"/><path d="M4 19h16"/></svg>
            </button>
            <input type="text" placeholder='Para onde vai hoje?'/>
        </header>
    )
}