# Airport Flight Delay Analytics and Prediction

A machine learning-based web application that predicts flight delays based on historical airline data. This project includes both data analysis (Jupyter notebook) and a Flask web application for interactive predictions.

## Features

- **Flight Delay Prediction**: Predict whether a flight will be delayed based on year, month, carrier, and airport
- **Interactive Web Interface**: User-friendly web application built with Flask
- **Data Analytics**: Comprehensive analysis of airline delay patterns using Jupyter notebook
- **Machine Learning Models**: Pre-trained models using scikit-learn
- **Historical Data**: Analysis based on real airline delay datasets

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

### 1. Clone or Download the Repository

```bash
cd "Airport Flight Delay Analytics and Prediction"
```

### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

## Project Structure

```
Airport Flight Delay Analytics and Prediction/
│
├── afdaap.ipynb                    # Jupyter notebook for data analysis
├── app.py                          # Flask web application
├── requirements.txt                # Python dependencies
│
├── Dataset/
│   └── Airline_Delay_Dataset.csv  # Historical flight delay data
│
├── Model/
│   ├── flight_delay_model.pkl     # Trained ML model
│   ├── carrier_encoder.pkl        # Carrier name encoder
│   └── airport_encoder.pkl        # Airport name encoder
│
└── templates/
    └── index.html                  # Web application template
```

## Running the Application

### Option 1: Web Application

1. **Make sure your virtual environment is activated**

2. **Run the Flask application:**
   ```bash
   python app.py
   ```

3. **Access the application:**
   - Open your web browser
   - Navigate to: `http://127.0.0.1:5000/` or `http://localhost:5000/`

4. **Using the application:**
   - Select the year from the dropdown
   - Select the month (1-12)
   - Choose a carrier (airline)
   - Choose an airport
   - Click "Predict" to see if a delay is expected

5. **Stop the application:**
   - Press `Ctrl + C` in the terminal

### Option 2: Jupyter Notebook (Data Analysis)

#### Running in VS Code (Recommended)

1. **Install the Jupyter extension in VS Code:**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Jupyter"
   - Install the extension published by Microsoft

2. **Open the notebook:**
   - In VS Code, open `afdaap.ipynb`
   - VS Code will automatically detect it as a Jupyter notebook

3. **Select Python interpreter:**
   - Click on "Select Kernel" in the top-right corner
   - Choose "Python Environments"
   - Select your virtual environment (should show the venv path)

4. **Run the notebook:**
   - Run cells individually by clicking the play button next to each cell
   - Or use "Run All" from the top menu
   - View outputs directly in VS Code

#### Alternative: Running in Browser

1. **Make sure your virtual environment is activated**

2. **Start Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

3. **Open the notebook:**
   - Your browser will open automatically
   - Navigate to and open `afdaap.ipynb`
   - Run cells sequentially to see the analysis

4. **Stop Jupyter:**
   - Press `Ctrl + C` in the terminal
   - Confirm shutdown when prompted

## Application Demo


| Home Page | Prediction Result |
|---|---|
| ![Home Page](demo/mainscreen.png) | ![Prediction Result](demo/resultscreen.png) |


## Usage

### Web Application Features

The web application allows you to:
- Select flight parameters (year, month, carrier, airport)
- Get instant delay predictions
- View results based on historical data patterns

### Prediction Logic

The model considers multiple factors:
- **Arrival flights**: Average number of flights
- **Carrier delays**: Historical carrier-related delays
- **Weather delays**: Weather-related delays
- **NAS delays**: National Aviation System delays
- **Security delays**: Security-related delays
- **Late aircraft delays**: Delays due to late arriving aircraft

## Troubleshooting

### Common Issues

1. **Import errors:**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Verify virtual environment is activated

2. **Port already in use:**
   - Change the port in `app.py` by modifying: `app.run(debug=True, port=5001)`
   - Or stop the process using port 5000

3. **Model files not found:**
   - Ensure all `.pkl` files are present in the `Model/` directory
   - Verify the `Dataset/` folder contains the CSV file

4. **Module not found errors:**
   - Reinstall requirements: `pip install --upgrade -r requirements.txt`

## Dependencies

Key dependencies include:
- **Flask**: Web framework
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **joblib**: Model serialization
- **matplotlib & seaborn**: Data visualization (for notebook)
- **jupyter**: Notebook interface

For complete list, see [requirements.txt](requirements.txt)

## Notes

- The application uses pre-trained models stored in the `Model/` directory
- Predictions are based on historical patterns from the dataset
- The model uses encoded categorical variables for carriers and airports
- Debug mode is enabled by default for development

## Future Enhancements

- Add more features for improved prediction accuracy
- Implement real-time data updates
- Add visualization dashboards
- Deploy to cloud platform (Heroku, AWS, Azure)
- Add API endpoints for programmatic access

## License

This project is available for educational and research purposes.

---

**For questions or issues, please refer to the troubleshooting section or check the code documentation.**
