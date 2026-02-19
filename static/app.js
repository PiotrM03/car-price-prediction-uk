document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("car-form");
    const resultDiv = document.getElementById("result");
  
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
  
      const miles = Number(document.getElementById("miles").value);
      const age = Number(document.getElementById("age").value);
      const engineVol = Number(document.getElementById("engine_vol").value);
      const engineSize = Number(document.getElementById("engine_size").value);

      const data = {
        make: document.getElementById("make").value,
        model: document.getElementById("model").value,
        body_type: document.getElementById("body_type").value,
        transmission: document.getElementById("transmission").value,
        fuel_type: document.getElementById("fuel_type").value,
        engine_vol: engineVol,
        engine_size: engineSize,
        miles: miles,
        age: age
      };

      if (Number.isNaN(miles) || miles <= 0) {
        resultDiv.textContent = "Miles must be a positive number.";
        return;
      }
      
      if (Number.isNaN(age) || age < 0) {
        resultDiv.textContent = "Age must be 0 or greater.";
        return;
      }
      
      if (Number.isNaN(engineVol) || engineVol <= 0) {
        resultDiv.textContent = "Engine volume must be a positive number.";
        return;
      }
      
      if (Number.isNaN(engineSize) || engineSize <= 0) {
        resultDiv.textContent = "Engine size must be a positive number.";
        return;
      }
  
      try {
        const response = await fetch("/predict", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });
  
        const json = await response.json();

        if (!response.ok) {
          resultDiv.textContent = json.error || "Prediction failed";
          return;
        }
        
        const price = json.predicted_price;
        
        resultDiv.textContent = `Predicted price: £${price.toLocaleString("en-GB", {
          maximumFractionDigits: 0,
        })}`;

      } catch (err) {
        resultDiv.textContent = "Error contacting server";
        console.error(err);
      }
    });
  });