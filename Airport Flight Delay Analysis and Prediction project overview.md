# Project Overview

## What This Project Does
Airport Flight Delay Analytics and Prediction is a small machine learning web app that predicts whether a flight is likely to be delayed based on historical airline data.

## Folder Structure
- `afdaap.ipynb` - notebook for data analysis, exploration, and model work
- `app.py` - Flask app and prediction logic
- `requirements.txt` - Python dependencies
- `Dataset/`
  - `Airline_Delay_Dataset.csv` - historical training and lookup data
- `Model/`
  - `flight_delay_model.pkl` - trained prediction model
  - `carrier_encoder.pkl` - carrier label encoder
  - `airport_encoder.pkl` - airport label encoder
- `templates/`
  - `index.html` - single UI page for the web app

## Architecture
- Front end: HTML template rendered by Flask
- Back end: Flask app receives form input and returns prediction results
- Data layer: CSV dataset provides historical delay records and fallback averages
- ML layer: saved model and encoders are loaded at startup with `joblib`
- Prediction flow: input values are converted to numeric features, passed to the model, then mapped to a human-readable result

## User Journey
1. User opens the home page in the browser.
2. The form shows available years, months, carriers, and airports.
3. User enters flight details and submits the form.
4. Flask prepares features from the selected inputs and historical averages.
5. The model predicts delay or no delay.
6. The result is shown on the same page.

## Flow Summary
`Browser -> Flask form -> feature preparation -> model prediction -> result on UI`

## Notes
- The notebook is for analysis and model exploration.
- The web app uses pre-trained artifacts, so prediction is fast.
- If a specific carrier-airport-month match is missing, the app falls back to broader averages before predicting.