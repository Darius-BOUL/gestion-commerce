import useFetch from "../hooks/useFetch";
import { ENDPOINTS } from "../api/endpoints";

export default function Produits() {
  const { data, loading } = useFetch(ENDPOINTS.produits);

  if (loading) return <p>Chargement...</p>;

  return (
    <div>
      <h1>Produits</h1>
      <ul>
        {data.map((p) => (
          <li key={p.id}>
            {p.nom} — Stock : {p.stock} — Prix : {p.prix} FCFA
          </li>
        ))}
      </ul>
    </div>
  );
}
