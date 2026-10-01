import {
    BrowserRouter,
    Routes,
    Route,
    Link
} from "react-router-dom";

import Comptes from "./pages/Comptes";


function App() {

    return (
        <BrowserRouter>

            <nav>

                <Link to="/">
                    Dashboard
                </Link>

                {" | "}

                <Link to="/comptes">
                    Comptes
                </Link>

            </nav>


            <Routes>

                <Route
                    path="/"
                    element={<h1>Dashboard</h1>}
                />

                <Route
                    path="/comptes"
                    element={<Comptes />}
                />

            </Routes>

        </BrowserRouter>
    );
}


export default App;