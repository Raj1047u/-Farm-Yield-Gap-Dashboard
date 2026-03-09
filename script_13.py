
# Create app/reports.py
reports_code = '''"""
Reports Page - Generate and download farm yield gap reports
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os
from io import BytesIO

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.preprocess import load_farm_data, filter_data

def show_reports():
    st.title("📄 Yield Gap Reports")
    
    st.markdown("""
    Generate comprehensive reports analyzing yield gaps across Indian farms.
    Reports can be downloaded as CSV files and include farm-wise analysis.
    """)
    
    # Load data
    df = load_farm_data()
    
    # Report configuration
    st.markdown("### ⚙️ Report Configuration")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        regions = ['All'] + sorted(df['Region'].unique().tolist())
        region_filter = st.selectbox("Region", regions, key='region_report')
    
    with col2:
        crops = ['All'] + sorted(df['Crop_Type'].unique().tolist())
        crop_filter = st.selectbox("Crop Type", crops, key='crop_report')
    
    with col3:
        years = ['All'] + sorted(df['Year'].unique().tolist(), reverse=True)
        year_filter = st.selectbox("Year", years, key='year_report')
    
    # Apply filters
    filtered_df = filter_data(
        df,
        region=region_filter if region_filter != 'All' else None,
        crop_type=crop_filter if crop_filter != 'All' else None,
        year=int(year_filter) if year_filter != 'All' else None
    )
    
    st.markdown(f"**{len(filtered_df)} farms** match your criteria")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Report preview
    st.markdown("### 📊 Report Preview")
    
    # Summary statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Farms", len(filtered_df))
    
    with col2:
        st.metric("Avg Yield Gap", f"{filtered_df['Yield_Gap'].mean():.1f} bu/ac")
    
    with col3:
        st.metric("Max Yield Gap", f"{filtered_df['Yield_Gap'].max():.1f} bu/ac")
    
    with col4:
        st.metric("Min Yield Gap", f"{filtered_df['Yield_Gap'].min():.1f} bu/ac")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Yield gap by region
        region_summary = filtered_df.groupby('Region')['Yield_Gap'].mean().reset_index()
        region_summary = region_summary.sort_values('Yield_Gap', ascending=False)
        
        fig = px.bar(
            region_summary,
            x='Region',
            y='Yield_Gap',
            title='Average Yield Gap by Region',
            template='plotly_dark',
            color='Yield_Gap',
            color_continuous_scale='Reds'
        )
        
        fig.update_layout(
            paper_bgcolor='#161b22',
            plot_bgcolor='#161b22',
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Yield gap by crop
        crop_summary = filtered_df.groupby('Crop_Type')['Yield_Gap'].mean().reset_index()
        crop_summary = crop_summary.sort_values('Yield_Gap', ascending=False)
        
        fig = px.bar(
            crop_summary,
            x='Crop_Type',
            y='Yield_Gap',
            title='Average Yield Gap by Crop Type',
            template='plotly_dark',
            color='Yield_Gap',
            color_continuous_scale='Oranges'
        )
        
        fig.update_layout(
            paper_bgcolor='#161b22',
            plot_bgcolor='#161b22',
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Farm-wise report table
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📋 Farm-wise Yield Gap Report")
    
    report_df = filtered_df[[
        'Farm_ID', 'Region', 'Crop_Type', 'Year', 'Season',
        'Attainable_Yield', 'Actual_Yield', 'Yield_Gap',
        'Precipitation', 'TempMax', 'N_Application', 'Soil_pH',
        'Irrigation_Type', 'Fertilizer_Mgmt_Score', 'Pest_Control_Score'
    ]].copy()
    
    # Sort by yield gap descending
    report_df = report_df.sort_values('Yield_Gap', ascending=False)
    
    st.dataframe(report_df, use_container_width=True, hide_index=True, height=400)
    
    # Download options
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 💾 Download Report")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # CSV download
        csv = report_df.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name=f"yield_gap_report_{year_filter}_{region_filter}.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    with col2:
        # PDF download (placeholder - would need reportlab implementation)
        st.button(
            "📄 Generate PDF Report",
            use_container_width=True,
            help="PDF generation requires reportlab library"
        )
        st.info("PDF generation: Coming soon!")
    
    # Additional analysis
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📈 Additional Insights")
    
    # Correlation with factors
    correlation_data = filtered_df[[
        'Yield_Gap', 'Precipitation', 'TempMax', 'N_Application',
        'Soil_pH', 'Soil_Quality_Score', 'Fertilizer_Mgmt_Score'
    ]].corr()['Yield_Gap'].drop('Yield_Gap').sort_values()
    
    fig = px.bar(
        x=correlation_data.values,
        y=correlation_data.index,
        orientation='h',
        title='Correlation of Factors with Yield Gap',
        template='plotly_dark',
        color=correlation_data.values,
        color_continuous_scale='RdBu_r'
    )
    
    fig.update_layout(
        paper_bgcolor='#161b22',
        plot_bgcolor='#161b22',
        xaxis_title='Correlation Coefficient',
        yaxis_title='Factor',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    show_reports()
'''

with open('yield_gap_analysis/app/reports.py', 'w') as f:
    f.write(reports_code)

print("✅ Created app/reports.py")
