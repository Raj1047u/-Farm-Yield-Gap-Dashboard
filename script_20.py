
# Let me create a version without XGBoost for now and use only sklearn models
ml_train_code_fixed = '''"""
ML Model Training Pipeline for Yield Gap Analysis
Trains multiple regression models and saves the best performing one
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
import os

def load_and_preprocess_data():
    """Load and preprocess farm data"""
    print("📂 Loading data...")
    df = pd.read_csv('data/farms_data.csv')
    
    # Feature engineering
    df['Yield_Ratio'] = df['Actual_Yield'] / df['Attainable_Yield']
    df['Temp_Range'] = df['TempMax'] - df['TempMin']
    df['Management_Score'] = (df['Fertilizer_Mgmt_Score'] + 
                               df['Pest_Control_Score'] + 
                               df['Hybrid_Selection_Score']) / 3
    
    # Encode categorical variables
    le_region = LabelEncoder()
    le_crop = LabelEncoder()
    le_season = LabelEncoder()
    le_irrigation = LabelEncoder()
    
    df['Region_Encoded'] = le_region.fit_transform(df['Region'])
    df['Crop_Encoded'] = le_crop.fit_transform(df['Crop_Type'])
    df['Season_Encoded'] = le_season.fit_transform(df['Season'])
    df['Irrigation_Encoded'] = le_irrigation.fit_transform(df['Irrigation_Type'])
    
    # Save encoders
    joblib.dump(le_region, 'ml/le_region.pkl')
    joblib.dump(le_crop, 'ml/le_crop.pkl')
    joblib.dump(le_season, 'ml/le_season.pkl')
    joblib.dump(le_irrigation, 'ml/le_irrigation.pkl')
    
    return df

def prepare_features(df):
    """Select and prepare features for modeling"""
    feature_cols = [
        'Precipitation', 'TempMax', 'TempMin', 'Temp_Range',
        'N_Application', 'Soil_pH', 'Soil_Quality_Score',
        'Fertilizer_Mgmt_Score', 'Pest_Control_Score', 'Hybrid_Selection_Score',
        'Management_Score', 'Region_Encoded', 'Crop_Encoded', 
        'Season_Encoded', 'Irrigation_Encoded', 'Year'
    ]
    
    X = df[feature_cols]
    y = df['Yield_Gap']
    
    return X, y, feature_cols

def train_models(X_train, X_test, y_train, y_test):
    """Train multiple models and compare performance"""
    print("\\n🤖 Training models...")
    
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(random_state=42, max_depth=10),
        'Random Forest': RandomForestRegressor(
            n_estimators=120, 
            random_state=42, 
            max_depth=15,
            min_samples_split=4,
            min_samples_leaf=2
        )
    }
    
    results = []
    best_r2 = 0
    best_model_name = None
    best_model = None
    
    for name, model in models.items():
        print(f"  Training {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        
        results.append({
            'Algorithm': name,
            'R2': round(r2, 4),
            'MAE': round(mae, 2),
            'MSE': round(mse, 2),
            'RMSE': round(rmse, 2),
            'Best_Model': False
        })
        
        print(f"    R² = {r2:.4f}, MAE = {mae:.2f}, RMSE = {rmse:.2f}")
        
        if r2 > best_r2:
            best_r2 = r2
            best_model_name = name
            best_model = model
    
    # Mark best model
    for result in results:
        if result['Algorithm'] == best_model_name:
            result['Best_Model'] = True
    
    return results, best_model, best_model_name

def save_model_artifacts(model, results, feature_cols):
    """Save model and evaluation artifacts"""
    print("\\n💾 Saving model artifacts...")
    
    # Save best model
    joblib.dump(model, 'ml/model.pkl')
    print("  ✓ Saved model.pkl")
    
    # Save metrics
    metrics_df = pd.DataFrame(results)
    metrics_df.to_csv('ml/metrics.csv', index=False)
    print("  ✓ Saved metrics.csv")
    
    # Get and save feature importance (for tree-based models)
    if hasattr(model, 'feature_importances_'):
        feature_importance = pd.DataFrame({
            'Feature': feature_cols,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        feature_importance.to_csv('ml/feature_importance.csv', index=False)
        print("  ✓ Saved feature_importance.csv")
        
        print("\\n📊 Top 5 Feature Importances:")
        for idx, row in feature_importance.head().iterrows():
            print(f"  {row['Feature']}: {row['Importance']:.4f}")

def main():
    """Main training pipeline"""
    print("=" * 60)
    print("🌾 AI Farm Yield Gap Analysis - Model Training Pipeline")
    print("=" * 60)
    
    # Create ml directory if it doesn't exist
    os.makedirs('ml', exist_ok=True)
    
    # Load and preprocess data
    df = load_and_preprocess_data()
    print(f"  ✓ Loaded {len(df)} farm records from India")
    
    # Prepare features
    X, y, feature_cols = prepare_features(df)
    print(f"  ✓ Prepared {len(feature_cols)} features")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"  ✓ Train size: {len(X_train)}, Test size: {len(X_test)}")
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    joblib.dump(scaler, 'ml/scaler.pkl')
    
    # Train models
    results, best_model, best_model_name = train_models(
        X_train_scaled, X_test_scaled, y_train, y_test
    )
    
    print(f"\\n🏆 Best Model: {best_model_name}")
    
    # Save artifacts
    save_model_artifacts(best_model, results, feature_cols)
    
    print("\\n✅ Training complete! Model ready for deployment.")
    print("=" * 60)

if __name__ == "__main__":
    main()
'''

with open('ml/train_model.py', 'w') as f:
    f.write(ml_train_code_fixed)

print("✅ Updated ml/train_model.py (without XGBoost dependency)")

# Now run it
exec(open('ml/train_model.py').read())
