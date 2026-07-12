import { useState } from "react";
import { predictFlood } from "./api";

export default function App() {
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    const data = {
      rainfall: 120,
      discharge: 300,
      soil_moisture: 0.85
    };

    const res = await predictFlood(data);
    setResult(res);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>FloodSense-GPT</h1>

      <button onClick={handlePredict}>
        Predict Flood Risk
      </button>

      {result && (
        <div>
          <h3>Risk: {result.risk_level}</h3>
          <p>{result.explanation}</p>
        </div>
      )}
    </div>
  );
}
