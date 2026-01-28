import useFetch from "../hooks/useFetch";
import { ENDPOINTS } from "../api/endpoints";
import CardStat from "../components/CardStat";

export default function Dashboard() {
  const { data, loading } = useFetch(ENDPOINTS.dashboard);

  if (loading) return <p>Chargement...</p>;

  return (
    <div>
      <h1>Dashboard</h1>

      <div className="stats-grid">
        <CardStat title="Total Ventes" value={data.total_ventes} />
        <CardStat title="Total Dettes" value={data.total_dettes} />
        <CardStat title="Produits Vendus" value={data.total_produits_vendus} />
      </div>

      <h2>Top Produits</h2>
      <ul>
        {data.top_produits.map((p) => (
          <li key={p.produit__nom}>
            {p.produit__nom} — {p.total_vendu} vendus
          </li>
        ))}
      </ul>
    </div>
  );
}
