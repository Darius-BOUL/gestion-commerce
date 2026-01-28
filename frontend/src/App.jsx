import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Produits from "./pages/Produits";
import Clients from "./pages/Clients";
import Ventes from "./pages/Ventes";
import Dettes from "./pages/Dettes";
import Login from "./pages/Login";
import Navbar from "./components/Navbar";

export default function App() {
  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/produits" element={<Produits />} />
        <Route path="/clients" element={<Clients />} />
        <Route path="/ventes" element={<Ventes />} />
        <Route path="/dettes" element={<Dettes />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </>
  );
}
