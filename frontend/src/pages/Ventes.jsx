import { useState } from "react";
import api from "../api/axios";
import { ENDPOINTS } from "../api/endpoints";

export default function Ventes() {
  const [produitId, setProduitId] = useState("");
  const [clientId, setClientId] = useState("");
  const [qte, setQte] = useState("");

  const enregistrerVente = async (e) => {
    e.preventDefault();

    try {
      await api.post(ENDPOINTS.ventes, {
        produit: produitId,
        client: clientId,
        quantite: qte,
      });

      alert("Vente enregistrée avec succès !");
      setProduitId("");
      setClientId("");
      setQte("");
    } catch (error) {
      console.error(error);
      alert("Erreur lors de l'enregistrement de la vente");
    }
  };

  return (
    <div>
      <h1>Ventes</h1>

      <form onSubmit={enregistrerVente} style={{ marginTop: "20px" }}>
        <div>
          <label>ID Produit :</label>
          <input
            type="number"
            value={produitId}
            onChange={(e) => setProduitId(e.target.value)}
          />
        </div>

        <div>
          <label>ID Client :</label>
          <input
            type="number"
            value={clientId}
            onChange={(e) => setClientId(e.target.value)}
          />
        </div>

        <div>
          <label>Quantité :</label>
          <input
            type="number"
            value={qte}
            onChange={(e) => setQte(e.target.value)}
          />
        </div>

        <button type="submit" style={{ marginTop: "10px" }}>
          Enregistrer la vente
        </button>
      </form>
    </div>
  );
}
