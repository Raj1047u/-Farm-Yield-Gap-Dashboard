
# Generate realistic synthetic India farm dataset with 200+ rows
np.random.seed(42)

# Indian states with approximate center coordinates
indian_regions = {
    'Punjab': (30.73, 75.34),
    'Haryana': (29.06, 76.09),
    'Uttar Pradesh': (26.85, 80.95),
    'Bihar': (25.10, 85.31),
    'Madhya Pradesh': (23.47, 77.95),
    'Maharashtra': (19.75, 75.71),
    'Karnataka': (15.32, 75.71),
    'Andhra Pradesh': (17.12, 79.21),
    'Telangana': (18.11, 79.02),
    'Gujarat': (22.31, 72.14),
    'Rajasthan': (26.91, 75.79),
    'West Bengal': (22.98, 87.75),
    'Odisha': (20.95, 85.10),
    'Tamil Nadu': (11.06, 78.39)
}

# Crop types suitable for each region
region_crops = {
    'Punjab': ['Wheat', 'Rice', 'Cotton'],
    'Haryana': ['Wheat', 'Rice', 'Sugarcane'],
    'Uttar Pradesh': ['Wheat', 'Sugarcane', 'Rice', 'Maize'],
    'Bihar': ['Rice', 'Wheat', 'Maize'],
    'Madhya Pradesh': ['Wheat', 'Rice', 'Maize', 'Cotton'],
    'Maharashtra': ['Cotton', 'Sugarcane', 'Rice'],
    'Karnataka': ['Rice', 'Maize', 'Cotton', 'Sugarcane'],
    'Andhra Pradesh': ['Rice', 'Sugarcane', 'Cotton'],
    'Telangana': ['Rice', 'Cotton', 'Maize'],
    'Gujarat': ['Cotton', 'Wheat', 'Rice'],
    'Rajasthan': ['Wheat', 'Maize', 'Cotton'],
    'West Bengal': ['Rice', 'Wheat', 'Maize'],
    'Odisha': ['Rice', 'Wheat', 'Maize'],
    'Tamil Nadu': ['Rice', 'Sugarcane', 'Cotton']
}

# Seasons
seasons = ['Kharif', 'Rabi']
years = [2020, 2021, 2022, 2023, 2024]
irrigation_types = ['canal', 'tube_well', 'rainfed', 'drip']

# Generate 220 farm records
n_farms = 220
farm_data = []

for i in range(n_farms):
    farm_id = f"FARM_{str(i+1).zfill(3)}"
    region = np.random.choice(list(indian_regions.keys()))
    crop = np.random.choice(region_crops[region])
    year = np.random.choice(years)
    season = np.random.choice(seasons)
    
    # Get base coordinates for region and jitter
    base_lat, base_lon = indian_regions[region]
    lat = base_lat + np.random.uniform(-1.5, 1.5)
    lon = base_lon + np.random.uniform(-1.5, 1.5)
    
    # Generate realistic yield values
    if crop == 'Wheat':
        attainable = np.random.uniform(180, 220)
        actual = attainable * np.random.uniform(0.70, 0.92)
    elif crop == 'Rice':
        attainable = np.random.uniform(190, 230)
        actual = attainable * np.random.uniform(0.68, 0.90)
    elif crop == 'Maize':
        attainable = np.random.uniform(170, 210)
        actual = attainable * np.random.uniform(0.72, 0.93)
    elif crop == 'Cotton':
        attainable = np.random.uniform(160, 200)
        actual = attainable * np.random.uniform(0.65, 0.88)
    else:  # Sugarcane
        attainable = np.random.uniform(200, 240)
        actual = attainable * np.random.uniform(0.70, 0.91)
    
    yield_gap = attainable - actual
    
    # Climate data (vary by region and season)
    if region in ['Punjab', 'Haryana', 'Rajasthan']:
        precipitation = np.random.uniform(400, 700)
        temp_max = np.random.uniform(32, 42)
        temp_min = np.random.uniform(18, 25)
    elif region in ['West Bengal', 'Odisha', 'Assam']:
        precipitation = np.random.uniform(1200, 2000)
        temp_max = np.random.uniform(28, 36)
        temp_min = np.random.uniform(20, 27)
    elif region in ['Maharashtra', 'Karnataka', 'Andhra Pradesh', 'Telangana']:
        precipitation = np.random.uniform(600, 1100)
        temp_max = np.random.uniform(30, 38)
        temp_min = np.random.uniform(19, 26)
    else:
        precipitation = np.random.uniform(800, 1400)
        temp_max = np.random.uniform(29, 37)
        temp_min = np.random.uniform(17, 24)
    
    # Soil and management factors
    n_application = np.random.uniform(80, 180)
    soil_ph = np.random.uniform(5.5, 8.0)
    soil_quality = np.random.uniform(60, 95)
    irrigation = np.random.choice(irrigation_types, p=[0.3, 0.35, 0.25, 0.1])
    
    # Management scores (0-10)
    fertilizer_score = np.random.uniform(5, 9.5)
    pest_score = np.random.uniform(5.5, 9)
    hybrid_score = np.random.uniform(6, 9.5)
    
    farm_data.append({
        'Farm_ID': farm_id,
        'Country': 'India',
        'Region': region,
        'Crop_Type': crop,
        'Year': year,
        'Season': season,
        'Attainable_Yield': round(attainable, 1),
        'Actual_Yield': round(actual, 1),
        'Yield_Gap': round(yield_gap, 1),
        'Precipitation': round(precipitation, 1),
        'TempMax': round(temp_max, 1),
        'TempMin': round(temp_min, 1),
        'N_Application': round(n_application, 1),
        'Soil_pH': round(soil_ph, 2),
        'Soil_Quality_Score': round(soil_quality, 1),
        'Irrigation_Type': irrigation,
        'Fertilizer_Mgmt_Score': round(fertilizer_score, 1),
        'Pest_Control_Score': round(pest_score, 1),
        'Hybrid_Selection_Score': round(hybrid_score, 1),
        'Latitude': round(lat, 4),
        'Longitude': round(lon, 4)
    })

farms_df = pd.DataFrame(farm_data)
farms_df.to_csv('yield_gap_analysis/data/farms_data.csv', index=False)

print("✅ Generated farms_data.csv with", len(farms_df), "records")
print("\n📊 Dataset Summary:")
print(f"  - Regions: {farms_df['Region'].nunique()}")
print(f"  - Crop Types: {farms_df['Crop_Type'].nunique()}")
print(f"  - Years: {sorted(farms_df['Year'].unique())}")
print(f"  - Average Yield Gap: {farms_df['Yield_Gap'].mean():.1f} bu/ac")
print("\n🗺️ Sample coordinates verification (India only):")
print(farms_df[['Farm_ID', 'Region', 'Latitude', 'Longitude']].head(10))
