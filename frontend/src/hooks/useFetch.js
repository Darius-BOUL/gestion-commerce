import { useEffect, useState } from "react";
import api from "../api/axios";

export default function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get(url)
      .then((res) => setData(res.data))
      .finally(() => setLoading(false));
  }, [url]);

  return { data, loading };
}
