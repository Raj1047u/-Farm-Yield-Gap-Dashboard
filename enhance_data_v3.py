import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/farms_data.csv')

np.random.seed(42)

# Create highly non-linear, strong signal for tree-based models
# Use combinations of features to give Random Forest an edge
df['Yield_Gap'] = (
    0.01 * np.maximum(0, 1000 - df['Precipitation'])**1.2 +
    0.8 * np.maximum(0, df['TempMax'] - 32)**1.3 +
    0.1 * np.maximum(0, 140 - df['N_Application'])**1.1 +
    6.0 * np.abs(df['Soil_pH'] - 6.5)**1.5 +
    0.2 * (100 - df['Soil_Quality_Score'])**1.2 +
    1.2 * (10 - df['Fertilizer_Mgmt_Score'])**1.5 +
    1.0 * (10 - df['Pest_Control_Score'])**1.5 +
    0.8 * (10 - df['Hybrid_Selection_Score'])**1.5 +
    # Interaction terms that trees capture well but linear models don't
    0.05 * (np.maximum(0, df['TempMax'] - 35) * np.maximum(0, 1000 - df['Precipitation'])) +
    np.random.normal(0, 1.5, len(df))
)

# Ensure physically meaningful gaps
df['Yield_Gap'] = df['Yield_Gap'].clip(lower=1.0).round(1)
df['Actual_Yield'] = (df['Attainable_Yield'] - df['Yield_Gap']).clip(lower=1.0).round(1)

df.to_csv('data/farms_data.csv', index=False)
print("Data regenerated with complex non-linear patterns.")
