
# Generate weather_data.csv for Indian regions
weather_data = []

for region in indian_regions.keys():
    for year in years:
        if region in ['Punjab', 'Haryana', 'Rajasthan']:
            avg_precip = np.random.uniform(450, 650)
            avg_temp_max = np.random.uniform(33, 40)
            avg_temp_min = np.random.uniform(19, 24)
        elif region in ['West Bengal', 'Odisha']:
            avg_precip = np.random.uniform(1300, 1800)
            avg_temp_max = np.random.uniform(29, 35)
            avg_temp_min = np.random.uniform(21, 26)
        elif region in ['Maharashtra', 'Karnataka', 'Andhra Pradesh', 'Telangana']:
            avg_precip = np.random.uniform(700, 1000)
            avg_temp_max = np.random.uniform(31, 37)
            avg_temp_min = np.random.uniform(20, 25)
        else:
            avg_precip = np.random.uniform(900, 1300)
            avg_temp_max = np.random.uniform(30, 36)
            avg_temp_min = np.random.uniform(18, 23)
        
        weather_data.append({
            'Region': region,
            'Year': year,
            'Avg_Precipitation': round(avg_precip, 1),
            'Avg_TempMax': round(avg_temp_max, 1),
            'Avg_TempMin': round(avg_temp_min, 1)
        })

weather_df = pd.DataFrame(weather_data)
weather_df.to_csv('yield_gap_analysis/data/weather_data.csv', index=False)

print("✅ Generated weather_data.csv with", len(weather_df), "records")
print(weather_df.head(10))
