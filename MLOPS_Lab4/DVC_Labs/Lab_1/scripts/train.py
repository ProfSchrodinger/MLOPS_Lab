import argparse
import os
import json
import joblib
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import silhouette_score

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

features_v1 = [
    'BALANCE', 
    'BALANCE_FREQUENCY', 
    'PURCHASES', 
    'ONEOFF_PURCHASES', 
    'INSTALLMENTS_PURCHASES', 
    'CASH_ADVANCE', 
    'PURCHASES_FREQUENCY', 
    'CREDIT_LIMIT', 
    'PAYMENTS', 
    'MINIMUM_PAYMENTS', 
    'PRC_FULL_PAYMENT', 
    'TENURE'
]

features_v2_drop = ['CUST_ID']

def train(feature_set_version):
    
    data_path = os.path.join(PROJECT_ROOT, 'data', 'cc_general.csv')
    df = pd.read_csv(data_path)
    
    if feature_set_version == 'v1':
        print("Using 12-feature set (v1)")
        features = features_v1
    elif feature_set_version == 'v2':
        print("Using all-feature set (v2)")
        features = [col for col in df.columns if col not in features_v2_drop]
    else:
        raise ValueError("Invalid feature set version")
        
    X = df[features]
    
    pipeline = make_pipeline(
        SimpleImputer(strategy='mean'),
        StandardScaler(),
        KMeans(n_clusters=6, random_state=42, n_init=10)
    )
    
    print("Training model...")
    model = pipeline.fit(X)
    
    labels = model.predict(X)
    X_transformed = model[:-1].transform(X)
    score = silhouette_score(X_transformed, labels)
    print(f"Model trained. Silhouette Score: {score}")
    
    model_dir = os.path.join(PROJECT_ROOT, 'model')
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, 'model.joblib')
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
    
    metrics_path = os.path.join(PROJECT_ROOT, 'metrics.json')
    metrics = {'silhouette_score': score}
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=4)
    print(f"Metrics saved to {metrics_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        help="Feature set version to use (v1 or v2)",
        required=True
    )
    args = parser.parse_args()
    train(args.version)