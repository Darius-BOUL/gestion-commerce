export default function CardStat({ title, value }) {
  return (
    <div style={{ padding: "10px", border: "1px solid #ccc", margin: "5px" }}>
      <h3>{title}</h3>
      <p>{value}</p>
    </div>
  );
}
