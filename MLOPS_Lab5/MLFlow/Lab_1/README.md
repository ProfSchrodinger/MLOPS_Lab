# Heart Disease Prediction with MLflow & Neural Networks

An end-to-end MLOps pipeline designed to predict heart disease stages (0-4) using a Multi-Layer Perceptron (Neural Network). This project demonstrates a full lifecycle workflow including experiment tracking, model registry, and real-time REST API deployment.

## Tech Stack
* **Core:** Python 3.x, Pandas, Scikit-Learn, NumPy
* **MLOps:** MLflow (Tracking, Registry, Serving)
* **Visualization:** Seaborn, Matplotlib

## Project Structure
```bash
heart_disease_mlflow/
├── data/                   # Contains heart.csv
├── mlruns/                 # Local MLflow storage
├── mlflow_working.ipynb # Main workflow (EDA -> Train -> Deploy)
└── README.md               # Documentation
```

## Quick Start

1. Setup
```bash
pip install pandas numpy scikit-learn mlflow seaborn matplotlib
```

2. Train & Register
Run the cells in mlflow_working.ipynb. This script will:
* Clean and encode the Heart Disease dataset.
* Train a Multiclass Neural Network (MLPClassifier).
* Automatically register the best model to the MLflow Registry.

3. View Experiments
Launch the UI to compare metrics:
```bash
mlflow ui
```

## Deployment (Real-Time)

1. Serve the Model
Host the production model on a local port (5002). Run this in a terminal:
```bash
mlflow models serve -m "models:/heart_disease_multiclass_production/Production" -p 5002 --no-conda
```

2. Inference
Send a POST request to http://127.0.0.1:5002/invocations with patient data (JSON).
<br> Example Python Client:
```bash
import requests
url = '[http://127.0.0.1:5002/invocations](http://127.0.0.1:5002/invocations)'
data = {"dataframe_split": test_data.to_dict(orient='split')}
response = requests.post(url, json=data)
print(response.json())
```