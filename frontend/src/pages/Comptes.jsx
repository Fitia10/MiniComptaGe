import { useEffect, useState } from "react";

import api from "../services/api";
import CompteForm from "../components/CompteForm";


function Comptes() {

    const [comptes, setComptes] = useState([]);


    const loadComptes = async () => {

        try {

            const response = await api.get(
                "comptes/"
            );

            setComptes(response.data);

        } catch (error) {

            console.error(error);

        }

    };


    useEffect(() => {

        loadComptes();

    }, []);


    const handleCompteCreated = (compte) => {

        setComptes([
            ...comptes,
            compte
        ]);

    };


    return (
        <div>

            <h1>Comptes</h1>

            <CompteForm
                onCompteCreated={
                    handleCompteCreated
                }
            />


            <hr />


            {comptes.map(compte => (

                <p key={compte.id}>

                    {compte.code}
                    {" - "}
                    {compte.libelle}
                    {" - "}
                    {compte.type}

                </p>

            ))}

        </div>
    );
}


export default Comptes;