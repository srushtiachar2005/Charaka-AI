import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "ml_models", "prakriti_model.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "ml_models", "feature_columns.pkl")

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURES_PATH)

def predict_prakriti(user_input: dict):
    df = pd.DataFrame([user_input])
    df_encoded = pd.get_dummies(df)

    df_encoded = df_encoded.reindex(columns=feature_columns, fill_value=0)

    probs = model.predict_proba(df_encoded)[0]
    return dict(zip(model.classes_, probs))
