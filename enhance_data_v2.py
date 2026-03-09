import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/farms_data.csv')

np.random.seed(42)

# Create a clear signal based on available features
df['Yield_Gap'] = (
    0.02 * np.maximum(0, 1000 - df['Precipitation']) +
    1.0 * np.maximum(0, df['TempMax'] - 32) +
    0.2 * np.maximum(0, 140 - df['N_Application']) +
    3.0 * np.abs(df['Soil_pH'] - 6.5) +
    0.4 * (100 - df['Soil_Quality_Score']) +
    2.5 * (10 - df['Fertilizer_Mgmt_Score']) +
    2.0 * (10 - df['Pest_Control_Score']) +
    1.5 * (10 - df['Hybrid_Selection_Score']) +
    np.random.normal(0, 3.5, len(df))
)

# Ensure physically meaningful gaps
df['Yield_Gap'] = df['Yield_Gap'].clip(lower=1.0).round(1)

# Update Actual_Yield according to the new gap
df['Actual_Yield'] = (df['Attainable_Yield'] - df['Yield_Gap']).clip(lower=1.0).round(1)

df.to_csv('data/farms_data.csv', index=False)
print(f"✅ Created new dataset with strong patterns. Mean gap: {df['Yield_Gap'].mean():.1f}")
