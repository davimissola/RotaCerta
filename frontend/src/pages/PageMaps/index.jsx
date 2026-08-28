import './page-maps.css';
import { FooterMaps } from "../../components/FooterMaps";
import { HeaderMaps } from "../../components/HeaderMaps";
import { Maps } from "../../components/Maps";
import { ViewsRotas } from "../../components/ViewsRotas";


export function PageMaps() {
    return (
        <main className="page-maps">
            <HeaderMaps />

            <Maps />

            <FooterMaps />

            <ViewsRotas />
        </main>
    )
}