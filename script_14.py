
# Create app/data_sources.py
data_sources_code = '''"""
Data Sources Page - CSV upload and data preview
"""

import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.preprocess import load_farm_data

def show_data_sources():
    st.title("🗄️ Data Sources")
    
    st.markdown("""
    Manage and explore the farm datasets used for yield gap analysis.
    Upload your own India farm data or view existing datasets.
    """)
    
    # Data upload section
    st.markdown("### 📤 Upload Custom Farm Data")
    
    uploaded_file = st.file_uploader(
        "Upload CSV file with farm data (India only)",
        type=['csv'],
        help="CSV should include: Farm_ID, Region, Crop_Type, Year, Attainable_Yield, Actual_Yield, etc."
    )
    
    if uploaded_file is not None:
        try:
            new_df = pd.read_csv(uploaded_file)
            st.success(f"✅ Uploaded file with {len(new_df)} records")
            
            # Validate India-only data
            if 'Country' in new_df.columns:
                non_india = new_df[new_df['Country'] != 'India']
                if len(non_india) > 0:
                    st.warning(f"⚠️ Found {len(non_india)} non-India records. Please ensure all data is India-only.")
            
            st.dataframe(new_df.head(20), use_container_width=True)
            
            # Save option
            if st.button("💾 Save to data/farms_data.csv"):
                new_df.to_csv('data/farms_data.csv', index=False)
                st.success("Data saved successfully!")
                st.rerun()
        
        except Exception as e:
            st.error(f"Error reading file: {e}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Current data preview
    st.markdown("### 📊 Current Farm Dataset")
    
    df = load_farm_data()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Records", len(df))
    
    with col2:
        st.metric("Regions", df['Region'].nunique())
    
    with col3:
        st.metric("Crop Types", df['Crop_Type'].nunique())
    
    with col4:
        st.metric("Years", f"{df['Year'].min()}-{df['Year'].max()}")
    
    # Data preview with search
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### Data Preview")
    
    search_term = st.text_input("🔍 Search farms", placeholder="Enter Farm ID, Region, or Crop")
    
    if search_term:
        mask = (
            df['Farm_ID'].str.contains(search_term, case=False, na=False) |
            df['Region'].str.contains(search_term, case=False, na=False) |
            df['Crop_Type'].str.contains(search_term, case=False, na=False)
        )
        display_df = df[mask]
        st.markdown(f"**Found {len(display_df)} matching records**")
    else:
        display_df = df
    
    st.dataframe(display_df, use_container_width=True, height=400)
    
    # Data quality statistics
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📈 Data Quality Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Missing Values Count:**")
        missing = df.isnull().sum()
        missing_df = pd.DataFrame({
            'Column': missing.index,
            'Missing Count': missing.values
        })
        missing_df = missing_df[missing_df['Missing Count'] > 0]
        
        if len(missing_df) > 0:
            st.dataframe(missing_df, use_container_width=True, hide_index=True)
        else:
            st.success("✅ No missing values!")
    
    with col2:
        st.markdown("**Data Types:**")
        dtypes_df = pd.DataFrame({
            'Column': df.dtypes.index,
            'Data Type': df.dtypes.values.astype(str)
        })
        st.dataframe(dtypes_df, use_container_width=True, hide_index=True, height=300)
    
    # Download current dataset
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 💾 Download Current Dataset")
    
    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Download farms_data.csv",
        data=csv,
        file_name="farms_data.csv",
        mime="text/csv"
    )
    
    # Additional datasets
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📚 Additional Datasets")
    
    tab1, tab2 = st.tabs(["Weather Data", "Soil Data"])
    
    with tab1:
        if os.path.exists('data/weather_data.csv'):
            weather_df = pd.read_csv('data/weather_data.csv')
            st.markdown(f"**{len(weather_df)} weather records**")
            st.dataframe(weather_df, use_container_width=True, height=300)
            
            csv_weather = weather_df.to_csv(index=False)
            st.download_button(
                label="📥 Download weather_data.csv",
                data=csv_weather,
                file_name="weather_data.csv",
                mime="text/csv"
            )
        else:
            st.info("Weather data not found")
    
    with tab2:
        if os.path.exists('data/soil_data.csv'):
            soil_df = pd.read_csv('data/soil_data.csv')
            st.markdown(f"**{len(soil_df)} soil records**")
            st.dataframe(soil_df, use_container_width=True, height=300)
            
            csv_soil = soil_df.to_csv(index=False)
            st.download_button(
                label="📥 Download soil_data.csv",
                data=csv_soil,
                file_name="soil_data.csv",
                mime="text/csv"
            )
        else:
            st.info("Soil data not found")

if __name__ == "__main__":
    show_data_sources()
'''

with open('yield_gap_analysis/app/data_sources.py', 'w') as f:
    f.write(data_sources_code)

print("✅ Created app/data_sources.py")
