import './page-maps.css';
import { FooterMaps } from "../../components/FooterMaps";
import { HeaderMaps } from "../../components/HeaderMaps";
import { Maps } from "../../components/Maps";
import { ViewsRotas } from "../../components/ViewsRotas";
import { useState } from 'react';
import { MenuDrawer } from '../../components/MenuDrawer';


export function PageMaps() {
    const [routes, setRoutes] = useState({})
    const [menuDrawerOpen, setMenuDrawerOpen] = useState(false)
    return (
        <main className="page-maps">
            <HeaderMaps setRoutes={setRoutes} setMenuDrawerOpen={setMenuDrawerOpen} menuDrawerOpen={menuDrawerOpen} />

            <Maps routes={routes}/>

            <FooterMaps />

            <MenuDrawer open={true} setMenuDrawerOpen={setMenuDrawerOpen} menuDrawerOpen={menuDrawerOpen} />
            <ViewsRotas />
        </main>
    )
}