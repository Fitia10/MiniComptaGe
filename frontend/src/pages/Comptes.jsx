import { useEffect, useState } from "react";
import api from "../services/api";


function Comptes() {

    const [comptes, setComptes] = useState([]);

    useEffect(() => {

        api.get("comptes/")
            .then(response => {
                setComptes(response.data);
            })
            .catch(error => {
                console.error(
                    "Erreur lors du chargement des comptes :",
                    error
                );
            });

    }, []);


    return (
        <div>

            <h1>Comptes</h1>

            {comptes.map(compte => (
                <p key={compte.id}>
                    {compte.code} - {compte.libelle}
                </p>
            ))}

        </div>
    );
}


export default Comptes;