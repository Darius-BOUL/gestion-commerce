import useFetch from "../hooks/useFetch";
import { ENDPOINTS } from "../api/endpoints";

export default function Clients() {
  const { data, loading } = useFetch(ENDPOINTS.clients);

  if (loading) return <p>Chargement...</p>;

  return (
    <div>
      <h1>Clients</h1>
      <ul>
        {data.map((c) => (
          <li key={c.id}>{c.nom} — {c.telephone}</li>
        ))}
      </ul>
    </div>
  );
}
