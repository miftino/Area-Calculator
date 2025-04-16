import React, { useState } from "react";
import "./App.css";

function App() {
  const [side, setSide] = useState("");
  const [area, setArea] = useState(null);
  const [error, setError] = useState("");

  const calculateSquare = async () => {
    setError("");
    setArea(null);

    try {
      const response = await fetch(
        `"http://localhost:5000/area/square?side=5"`
      );
      const data = await response.json();

      if (response.ok) {
        setArea(data.area);
      } else {
        setError(data.error || "Something went wrong.");
      }
    } catch (err) {
      setError("Unable to reach the server.");
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>📐 Square Area Calculator</h1>
        <input
          type="number"
          placeholder="Enter side length"
          value={side}
          onChange={(e) => setSide(e.target.value)}
        />
        <button onClick={calculateSquare}>Calculate</button>
        {area !== null && <p>✅ Area: {area}</p>}
        {error && <p style={{ color: "red" }}>❌ {error}</p>}
      </header>
    </div>
  );
}

export default App;
