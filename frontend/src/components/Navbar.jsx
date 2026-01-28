import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ padding: "10px", background: "#eee" }}>
      <Link to="/">Dashboard</Link> |{" "}
      <Link to="/produits">Produits</Link> |{" "}
      <Link to="/clients">Clients</Link> |{" "}
      <Link to="/ventes">Ventes</Link> |{" "}
      <Link to="/dettes">Dettes</Link> |{" "}
      <Link to="/login">Login</Link>
    </nav>
  );
}
