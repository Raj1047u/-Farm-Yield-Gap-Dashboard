
# Create app/farm_map.py
farm_map_code = '''"""
Farm Map Page - Full-screen India map with filtering
"""

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.preprocess import load_farm_data, filter_data, calculate_summary_stats

def show_farm_map():
    st.title("🗺️ Interactive Farm Map")
    
    # Load data
    df = load_farm_data()
    
    # Filter controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        regions = ['All'] + sorted(df['Region'].unique().tolist())
        region_filter = st.selectbox("Region", regions, key='region_map')
    
    with col2:
        crops = ['All'] + sorted(df['Crop_Type'].unique().tolist())
        crop_filter = st.selectbox("Crop Type", crops, key='crop_map')
    
    with col3:
        years = ['All'] + sorted(df['Year'].unique().tolist(), reverse=True)
        year_filter = st.selectbox("Year", years, key='year_map')
    
    # Apply filters
    filtered_df = filter_data(
        df,
        region=region_filter if region_filter != 'All' else None,
        crop_type=crop_filter if crop_filter != 'All' else None,
        year=int(year_filter) if year_filter != 'All' else None
    )
    
    stats = calculate_summary_stats(filtered_df)
    
    # Summary stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Farms", stats['total_farms'])
    
    with col2:
        st.metric("Avg Yield Gap", f"{stats['avg_yield_gap']:.1f} bu/ac")
    
    with col3:
        st.metric("Highest Gap Farm", 
                  f"{stats['highest_gap_farm']} ({stats['highest_gap_value']:.1f})")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create large India map
    india_center = [20.5937, 78.9629]
    m = folium.Map(
        location=india_center,
        zoom_start=5,
        tiles='OpenStreetMap',
        width='100%',
        height=600
    )
    
    # Add markers
    for idx, row in filtered_df.iterrows():
        if row['Yield_Gap'] > 50:
            color = 'red'
        elif row['Yield_Gap'] > 30:
            color = 'orange'
        else:
            color = 'green'
        
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=7,
            popup=folium.Popup(f"""
                <div style='width: 200px;'>
                    <h4>{row['Farm_ID']}</h4>
                    <b>Region:</b> {row['Region']}<br>
                    <b>Crop:</b> {row['Crop_Type']}<br>
                    <b>Year:</b> {row['Year']}<br>
                    <b>Yield Gap:</b> {row['Yield_Gap']:.1f} bu/ac<br>
                    <b>Attainable:</b> {row['Attainable_Yield']:.1f} bu/ac<br>
                    <b>Actual:</b> {row['Actual_Yield']:.1f} bu/ac
                </div>
            """, max_width=250),
            color=color,
            fill=True,
            fillColor=color,
            fillOpacity=0.7
        ).add_to(m)
    
    # Display map
    st_folium(m, width=None, height=600)
    
    # Legend and info
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Map Legend:**
        - 🔴 Red: High yield gap (>50 bu/ac)
        - 🟡 Orange: Medium yield gap (30-50 bu/ac)
        - 🟢 Green: Low yield gap (<30 bu/ac)
        """)
    
    with col2:
        st.markdown(f"""
        **Dataset Summary:**
        - Total farms displayed: **{len(filtered_df)}**
        - Regions covered: **{filtered_df['Region'].nunique()}**
        - Crop types: **{filtered_df['Crop_Type'].nunique()}**
        - Average yield gap: **{stats['avg_yield_gap']:.1f} bu/ac**
        """)

if __name__ == "__main__":
    show_farm_map()
'''

with open('yield_gap_analysis/app/farm_map.py', 'w') as f:
    f.write(farm_map_code)

print("✅ Created app/farm_map.py")
