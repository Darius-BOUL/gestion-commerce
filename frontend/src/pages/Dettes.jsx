import useFetch from "../hooks/useFetch";
import { ENDPOINTS } from "../api/endpoints";

export default function Dettes() {
  const { data, loading } = useFetch(ENDPOINTS.dettes);

  if (loading) return <p>Chargement...</p>;

  return (
    <div>
      <h1>Dettes</h1>
      <ul>
        {data.map((d) => (
          <li key={d.id}>
            {d.client_nom} — {d.montant} FCFA — {d.payee ? "Payée" : "Non payée"}
          </li>
        ))}
      </ul>
    </div>
  );
}
