
# Generate soil_data.csv for Indian regions
soil_data = []

for region in indian_regions.keys():
    for year in years:
        # Different soil characteristics by region
        if region in ['Punjab', 'Haryana', 'Uttar Pradesh']:
            avg_ph = np.random.uniform(7.0, 8.0)
            avg_quality = np.random.uniform(75, 90)
        elif region in ['West Bengal', 'Odisha', 'Bihar']:
            avg_ph = np.random.uniform(6.0, 7.5)
            avg_quality = np.random.uniform(70, 85)
        elif region in ['Maharashtra', 'Karnataka']:
            avg_ph = np.random.uniform(6.5, 7.8)
            avg_quality = np.random.uniform(68, 83)
        elif region in ['Rajasthan', 'Gujarat']:
            avg_ph = np.random.uniform(7.2, 8.2)
            avg_quality = np.random.uniform(65, 80)
        else:
            avg_ph = np.random.uniform(6.2, 7.6)
            avg_quality = np.random.uniform(70, 88)
        
        soil_data.append({
            'Region': region,
            'Year': year,
            'Avg_Soil_pH': round(avg_ph, 2),
            'Avg_Soil_Quality_Score': round(avg_quality, 1)
        })

soil_df = pd.DataFrame(soil_data)
soil_df.to_csv('yield_gap_analysis/data/soil_data.csv', index=False)

print("✅ Generated soil_data.csv with", len(soil_df), "records")
print(soil_df.head(10))
