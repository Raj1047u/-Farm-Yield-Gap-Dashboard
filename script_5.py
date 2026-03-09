
# Create ml/predict.py
ml_predict_code = '''"""
Prediction utilities for yield gap analysis
"""

import pandas as pd
import numpy as np
import joblib

def load_model_artifacts():
    """Load trained model and preprocessing artifacts"""
    model = joblib.load('ml/model.pkl')
    scaler = joblib.load('ml/scaler.pkl')
    le_region = joblib.load('ml/le_region.pkl')
    le_crop = joblib.load('ml/le_crop.pkl')
    le_season = joblib.load('ml/le_season.pkl')
    le_irrigation = joblib.load('ml/le_irrigation.pkl')
    
    return model, scaler, le_region, le_crop, le_season, le_irrigation

def preprocess_for_prediction(df, le_region, le_crop, le_season, le_irrigation):
    """Preprocess data for prediction"""
    df = df.copy()
    
    # Feature engineering
    df['Yield_Ratio'] = df['Actual_Yield'] / df['Attainable_Yield']
    df['Temp_Range'] = df['TempMax'] - df['TempMin']
    df['Management_Score'] = (df['Fertilizer_Mgmt_Score'] + 
                               df['Pest_Control_Score'] + 
                               df['Hybrid_Selection_Score']) / 3
    
    # Encode categorical variables
    df['Region_Encoded'] = le_region.transform(df['Region'])
    df['Crop_Encoded'] = le_crop.transform(df['Crop_Type'])
    df['Season_Encoded'] = le_season.transform(df['Season'])
    df['Irrigation_Encoded'] = le_irrigation.transform(df['Irrigation_Type'])
    
    feature_cols = [
        'Precipitation', 'TempMax', 'TempMin', 'Temp_Range',
        'N_Application', 'Soil_pH', 'Soil_Quality_Score',
        'Fertilizer_Mgmt_Score', 'Pest_Control_Score', 'Hybrid_Selection_Score',
        'Management_Score', 'Region_Encoded', 'Crop_Encoded', 
        'Season_Encoded', 'Irrigation_Encoded', 'Year'
    ]
    
    return df[feature_cols]

def predict_yield_gap(model, scaler, X):
    """Make yield gap predictions"""
    X_scaled = scaler.transform(X)
    predictions = model.predict(X_scaled)
    return predictions
'''

with open('yield_gap_analysis/ml/predict.py', 'w') as f:
    f.write(ml_predict_code)

print("✅ Created ml/predict.py")
