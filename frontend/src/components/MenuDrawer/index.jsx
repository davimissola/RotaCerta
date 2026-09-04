import userDark from '../../assets/user-dark.jpg';
import './menu-drawer.css'


export function MenuDrawer({ setMenuDrawerOpen, menuDrawerOpen }) {
    return (
        <div className={`div-menu-drawer ${menuDrawerOpen ? 'aberto' : 'fechado'}`}>
            <div className='menu-drawer-top'>
                <button onClick={() => setMenuDrawerOpen(false)}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-x-icon lucide-x"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
                </button>

                <div className="div-account">
                    <img src={userDark} alt="Foto de perfil do usuário" />
                    <div className='div-account-infos'>
                        <a href="#">Ainda não entrou?</a>
                        <p>Entre para salvar suas rotas e locais favoritos</p>
                    </div>
                </div>
            </div>

            <div className="menu-drawer-bottom">
                <a href="#" className="a-nav-bar">Explorar</a>
                <a href="#" className="a-nav-bar">Salvar contatos</a>
                <a href="#" className="a-nav-bar">Configurações</a>
                <a href="#" className="a-nav-bar">Ajuda</a>
            </div>
        </div>
    )
}