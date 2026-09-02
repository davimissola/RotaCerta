import './page-maps.css';
import { FooterMaps } from "../../components/FooterMaps";
import { HeaderMaps } from "../../components/HeaderMaps";
import { Maps } from "../../components/Maps";
import { ViewsRotas } from "../../components/ViewsRotas";
import { useState } from 'react';


export function PageMaps() {
    const [routes, setRoutes] = useState({})
    return (
        <main className="page-maps">
            <HeaderMaps setRoutes={setRoutes} />

            <Maps routes={routes}/>

            <FooterMaps />

            <ViewsRotas />
        </main>
    )
}