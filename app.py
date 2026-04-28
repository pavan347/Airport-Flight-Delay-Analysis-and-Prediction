from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load dataset + model + encoders
df = pd.read_csv("Dataset/Airline_Delay_Dataset.csv")
model = joblib.load("Model/flight_delay_model.pkl")
carrier_encoder = joblib.load("Model/carrier_encoder.pkl")
airport_encoder = joblib.load("Model/airport_encoder.pkl")

def prepare_features(year, month, carrier_name, airport_name):
    # Filter by airport, airline & month
    filtered = df[
        (df['carrier_name'] == carrier_name) &
        (df['airport_name'] == airport_name) &
        (df['month'] == month)
    ]

    # If found, use averages
    if len(filtered) > 0:
        arr_flights = filtered["arr_flights"].mean()
        carrier_ct = filtered["carrier_ct"].mean()
        weather_ct = filtered["weather_ct"].mean()
        nas_ct = filtered["nas_ct"].mean()
        security_ct = filtered["security_ct"].mean()
        late_aircraft_ct = filtered["late_aircraft_ct"].mean()
    else:
        # fallback: airport + carrier averages
        fallback = df[
            (df['carrier_name'] == carrier_name) &
            (df['airport_name'] == airport_name)
        ]
        if len(fallback) > 0:
            arr_flights = fallback["arr_flights"].mean()
            carrier_ct = fallback["carrier_ct"].mean()
            weather_ct = fallback["weather_ct"].mean()
            nas_ct = fallback["nas_ct"].mean()
            security_ct = fallback["security_ct"].mean()
            late_aircraft_ct = fallback["late_aircraft_ct"].mean()
        else:
            # global fallback
            arr_flights = df["arr_flights"].mean()
            carrier_ct = df["carrier_ct"].mean()
            weather_ct = df["weather_ct"].mean()
            nas_ct = df["nas_ct"].mean()
            security_ct = df["security_ct"].mean()
            late_aircraft_ct = df["late_aircraft_ct"].mean()

    # Encode categories
    carrier_encoded = carrier_encoder.transform([carrier_name])[0]
    airport_encoded = airport_encoder.transform([airport_name])[0]

    # Final feature vector
    return np.array([[
        year, month, carrier_encoded, airport_encoded,
        arr_flights, carrier_ct, weather_ct,
        nas_ct, security_ct, late_aircraft_ct
    ]])

@app.route("/")
def home():
    # Pass dropdown options to HTML
    carriers = sorted(df["carrier_name"].unique())
    airports = sorted(df["airport_name"].unique())
    return render_template("index.html", carriers=carriers, airports=airports)

@app.route("/predict", methods=["POST"])
def predict():
    year = int(request.form["year"])
    month = int(request.form["month"])
    carrier_name = request.form["carrier_name"]
    airport_name = request.form["airport_name"]

    input_vector = prepare_features(year, month, carrier_name, airport_name)
    
    prediction = model.predict(input_vector)[0]

    result = "Delay Expected" if prediction == 1 else "No Delay Expected"

    carriers = sorted(df["carrier_name"].unique())
    airports = sorted(df["airport_name"].unique())

    return render_template(
        "index.html",
        prediction=result,
        carriers=carriers,
        airports=airports
    )

if __name__ == "__main__":
    app.run(debug=True)
