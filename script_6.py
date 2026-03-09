
# Create utils/preprocess.py
utils_preprocess_code = '''"""
Data preprocessing utilities
"""

import pandas as pd
import numpy as np

def load_farm_data():
    """Load farm dataset"""
    df = pd.read_csv('data/farms_data.csv')
    return df

def filter_data(df, country=None, region=None, crop_type=None, year=None):
    """Filter farm data based on criteria"""
    filtered_df = df.copy()
    
    if country and country != 'All':
        filtered_df = filtered_df[filtered_df['Country'] == country]
    
    if region and region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == region]
    
    if crop_type and crop_type != 'All':
        filtered_df = filtered_df[filtered_df['Crop_Type'] == crop_type]
    
    if year and year != 'All':
        filtered_df = filtered_df[filtered_df['Year'] == year]
    
    return filtered_df

def calculate_summary_stats(df):
    """Calculate summary statistics"""
    stats = {
        'total_farms': len(df),
        'avg_yield_gap': df['Yield_Gap'].mean(),
        'avg_attainable': df['Attainable_Yield'].mean(),
        'avg_actual': df['Actual_Yield'].mean(),
        'highest_gap_farm': df.loc[df['Yield_Gap'].idxmax(), 'Farm_ID'] if len(df) > 0 else None,
        'highest_gap_value': df['Yield_Gap'].max() if len(df) > 0 else 0
    }
    return stats

def get_yield_gap_categories(yield_gap):
    """Categorize yield gap into Low/Medium/High"""
    if yield_gap < 30:
        return 'Low'
    elif yield_gap < 50:
        return 'Medium'
    else:
        return 'High'

def add_yield_gap_category(df):
    """Add yield gap category column"""
    df['Yield_Gap_Category'] = df['Yield_Gap'].apply(get_yield_gap_categories)
    return df
'''

with open('yield_gap_analysis/utils/preprocess.py', 'w') as f:
    f.write(utils_preprocess_code)

print("✅ Created utils/preprocess.py")
