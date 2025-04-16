import React, { useState } from "react";
import "./App.css";

function App() {
  const [selectedShape, setSelectedShape] = useState("square");
  const [inputs, setInputs] = useState({
    side: "",
    length: "",
    width: "",
    base: "",
    height: "",
    radius: ""
  });
  const [area, setArea] = useState(null);
  const [error, setError] = useState("");

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setInputs(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const calculateArea = async () => {
    setError("");
    setArea(null);

    let endpoint = "";
    let params = new URLSearchParams();

    switch (selectedShape) {
      case "square":
        endpoint = "/area/square";
        params.append("side", inputs.side);
        break;
      case "rectangle":
        endpoint = "/area/rectangle";
        params.append("length", inputs.length);
        params.append("width", inputs.width);
        break;
      case "triangle":
        endpoint = "/area/triangle";
        params.append("base", inputs.base);
        params.append("height", inputs.height);
        break;
      case "circle":
        endpoint = "/area/circle";
        params.append("radius", inputs.radius);
        break;
      default:
        setError("Invalid shape selected");
        return;
    }

    try {
      const response = await fetch(
        `http://localhost:5000${endpoint}?${params.toString()}`
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

  const renderInputs = () => {
    switch (selectedShape) {
      case "square":
        return (
          <input
            type="number"
            name="side"
            placeholder="Enter side length"
            value={inputs.side}
            onChange={handleInputChange}
          />
        );
      case "rectangle":
        return (
          <>
            <input
              type="number"
              name="length"
              placeholder="Enter length"
              value={inputs.length}
              onChange={handleInputChange}
            />
            <input
              type="number"
              name="width"
              placeholder="Enter width"
              value={inputs.width}
              onChange={handleInputChange}
            />
          </>
        );
      case "triangle":
        return (
          <>
            <input
              type="number"
              name="base"
              placeholder="Enter base"
              value={inputs.base}
              onChange={handleInputChange}
            />
            <input
              type="number"
              name="height"
              placeholder="Enter height"
              value={inputs.height}
              onChange={handleInputChange}
            />
          </>
        );
      case "circle":
        return (
          <input
            type="number"
            name="radius"
            placeholder="Enter radius"
            value={inputs.radius}
            onChange={handleInputChange}
          />
        );
      default:
        return null;
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>📐 Area Calculator</h1>
        <div className="shape-selector">
          <select
            value={selectedShape}
            onChange={(e) => setSelectedShape(e.target.value)}
          >
            <option value="square">Square</option>
            <option value="rectangle">Rectangle</option>
            <option value="triangle">Triangle</option>
            <option value="circle">Circle</option>
          </select>
        </div>
        <div className="input-container">
          {renderInputs()}
        </div>
        <button onClick={calculateArea}>Calculate Area</button>
        {area !== null && <p>✅ Area: {area.toFixed(2)} square units</p>}
        {error && <p style={{ color: "red" }}>❌ {error}</p>}
      </header>
    </div>
  );
}

export default App;
