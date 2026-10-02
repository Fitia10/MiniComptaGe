import { useState } from "react";
import api from "../services/api";


function CompteForm({ onCompteCreated }) {

    const [form, setForm] = useState({
        code: "",
        libelle: "",
        type: "ACTIF"
    });


    const handleChange = (event) => {

        setForm({
            ...form,
            [event.target.name]: event.target.value
        });

    };


    const handleSubmit = async (event) => {

        event.preventDefault();

        try {

            const response = await api.post(
                "comptes/",
                form
            );

            onCompteCreated(response.data);

            setForm({
                code: "",
                libelle: "",
                type: "ACTIF"
            });

        } catch (error) {

            console.error(
                "Erreur :",
                error
            );

        }

    };


    return (
        <form onSubmit={handleSubmit}>

            <input
                name="code"
                placeholder="Code"
                value={form.code}
                onChange={handleChange}
            />

            <input
                name="libelle"
                placeholder="Libellé"
                value={form.libelle}
                onChange={handleChange}
            />

            <select
                name="type"
                value={form.type}
                onChange={handleChange}
            >

                <option value="ACTIF">
                    Actif
                </option>

                <option value="PASSIF">
                    Passif
                </option>

                <option value="CHARGE">
                    Charge
                </option>

                <option value="PRODUIT">
                    Produit
                </option>

            </select>

            <button type="submit">
                Ajouter
            </button>

        </form>
    );
}


export default CompteForm;