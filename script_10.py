
# Create app/dashboard.py - Main dashboard with 3-column layout
dashboard_code = '''"""
Main Dashboard Page - 3-column layout with India map, charts, and ML insights
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import folium
from streamlit_folium import st_folium
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.preprocess import load_farm_data, filter_data, calculate_summary_stats, add_yield_gap_category
from utils.recommendations import get_recommendations

def show_dashboard():
    st.title("🌾 Farm Yield Gap Dashboard")
    
    # Load data
    df = load_farm_data()
    df = add_yield_gap_category(df)
    
    # Top Filter Bar - 5 filters side by side
    st.markdown("### 🔍 Filters")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        country_filter = st.selectbox("Country", ['India'], key='country_dash')
    
    with col2:
        regions = ['All'] + sorted(df['Region'].unique().tolist())
        region_filter = st.selectbox("Region", regions, key='region_dash')
    
    with col3:
        crops = ['All'] + sorted(df['Crop_Type'].unique().tolist())
        crop_filter = st.selectbox("Crop Type", crops, key='crop_dash')
    
    with col4:
        years = ['All'] + sorted(df['Year'].unique().tolist(), reverse=True)
        year_filter = st.selectbox("Year", years, index=1, key='year_dash')  # Default 2024
    
    with col5:
        gap_type = st.selectbox("Yield Gap Type", ['Attainable vs. Actual'], key='gap_type_dash')
    
    # Apply filters
    filtered_df = filter_data(
        df,
        country=country_filter,
        region=region_filter if region_filter != 'All' else None,
        crop_type=crop_filter if crop_filter != 'All' else None,
        year=int(year_filter) if year_filter != 'All' else None
    )
    
    if len(filtered_df) == 0:
        st.warning("No data available for selected filters.")
        return
    
    stats = calculate_summary_stats(filtered_df)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 3-COLUMN LAYOUT
    left_col, middle_col, right_col = st.columns([1.2, 1.3, 1.0])
    
    # ==================== LEFT COLUMN ====================
    with left_col:
        st.markdown("### 🗺️ Interactive Farm Map")
        
        # Create India-centered Folium map
        india_center = [20.5937, 78.9629]
        m = folium.Map(
            location=india_center,
            zoom_start=5,
            tiles='OpenStreetMap',
            width='100%',
            height=400
        )
        
        # Add markers with color coding by yield gap
        for idx, row in filtered_df.iterrows():
            # Color code by yield gap
            if row['Yield_Gap'] > 50:
                color = 'red'
                category = 'High'
            elif row['Yield_Gap'] > 30:
                color = 'orange'
                category = 'Medium'
            else:
                color = 'green'
                category = 'Low'
            
            folium.CircleMarker(
                location=[row['Latitude'], row['Longitude']],
                radius=6,
                popup=f"<b>{row['Farm_ID']}</b><br>Gap: {row['Yield_Gap']:.1f} bu/ac<br>{row['Crop_Type']}, {row['Year']}",
                color=color,
                fill=True,
                fillColor=color,
                fillOpacity=0.7
            ).add_to(m)
        
        # Display map
        st_folium(m, width=None, height=400)
        
        # Legend
        st.markdown("""
        <div style='background: #161b22; padding: 0.8rem; border-radius: 6px; margin-top: 0.5rem;'>
            <div style='font-size: 0.85rem; color: #8b949e; margin-bottom: 0.3rem;'><b>Legend:</b></div>
            <div style='display: flex; gap: 1rem; font-size: 0.8rem;'>
                <span style='color: #f85149;'>🔴 High gap (>50)</span>
                <span style='color: #d29922;'>🟡 Medium gap (30-50)</span>
                <span style='color: #3fb950;'>🟢 Low gap (<30)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Farm Selection Table
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### Farm Selection Table")
        
        display_df = filtered_df[['Farm_ID', 'Attainable_Yield', 'Actual_Yield', 'Yield_Gap']].head(5)
        display_df.columns = ['Farm ID', 'Attainable', 'Actual', 'Gap']
        display_df['Attainable'] = display_df['Attainable'].apply(lambda x: f"{x:.0f} bu/ac")
        display_df['Actual'] = display_df['Actual'].apply(lambda x: f"{x:.0f} bu/ac")
        display_df['Gap'] = display_df['Gap'].apply(lambda x: f"{x:.0f} bu/ac")
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # ==================== MIDDLE COLUMN ====================
    with middle_col:
        st.markdown("### 📊 Yield Gap Analysis")
        
        # Create tabs
        tab1, tab2, tab3 = st.tabs(["Yield Gap Overview", "Interactive Analysis", "Yield Driver Analysis"])
        
        with tab1:
            # Donut chart - Avg Yield Gap Distribution
            avg_attainable = filtered_df['Attainable_Yield'].mean()
            avg_actual = filtered_df['Actual_Yield'].mean()
            avg_gap = avg_attainable - avg_actual
            
            fig = go.Figure(data=[go.Pie(
                labels=['Attainable', 'Actual', 'Gap'],
                values=[avg_attainable, avg_actual, avg_gap],
                hole=.5,
                marker=dict(colors=['#58a6ff', '#3fb950', '#f85149']),
                textinfo='label+percent+value',
                texttemplate='%{label}<br>%{percent}<br>%{value:.0f} bu/ac'
            )])
            
            fig.update_layout(
                title='Avg. Yield Gap Distribution',
                template='plotly_dark',
                paper_bgcolor='#161b22',
                plot_bgcolor='#161b22',
                height=350,
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.markdown("**Interactive Scatter Analysis**")
            
            # Scatter plot: Precipitation vs Yield Gap
            fig = px.scatter(
                filtered_df,
                x='Precipitation',
                y='Yield_Gap',
                color='Crop_Type',
                size='Attainable_Yield',
                hover_data=['Farm_ID', 'Region'],
                title='Precipitation vs Yield Gap by Crop Type',
                template='plotly_dark'
            )
            
            fig.update_layout(
                paper_bgcolor='#161b22',
                plot_bgcolor='#161b22',
                height=350
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.markdown("**Farm 124 (Corn, 2024)**")
            
            # Feature importance bar chart (using synthetic data)
            try:
                feature_importance = pd.read_csv('ml/feature_importance.csv').head(5)
                
                # Map feature names to categories
                feature_colors = {
                    'Precipitation': '#58a6ff',
                    'N_Application': '#d29922',
                    'Soil_pH': '#3fb950',
                    'TempMax': '#58a6ff',
                    'Soil_Quality_Score': '#3fb950',
                    'Fertilizer_Mgmt_Score': '#d29922',
                    'Pest_Control_Score': '#f85149',
                    'Hybrid_Selection_Score': '#8b949e'
                }
                
                colors = [feature_colors.get(feat, '#58a6ff') for feat in feature_importance['Feature']]
                
                fig = go.Figure(data=[go.Bar(
                    y=feature_importance['Feature'],
                    x=feature_importance['Importance'] * 100,
                    orientation='h',
                    marker=dict(color=colors)
                )])
                
                fig.update_layout(
                    title='Feature Importance (from ML model)',
                    xaxis_title='Importance (%)',
                    yaxis_title='',
                    template='plotly_dark',
                    paper_bgcolor='#161b22',
                    plot_bgcolor='#161b22',
                    height=350
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
            except:
                st.info("Run ML training first: `python ml/train_model.py`")
    
    # ==================== RIGHT COLUMN ====================
    with right_col:
        st.markdown("### 🤖 ML Insights")
        
        # ML Model Insights Card
        try:
            metrics_df = pd.read_csv('ml/metrics.csv')
            best_model = metrics_df[metrics_df['Best_Model'] == True].iloc[0]
            
            st.markdown(f"""
            <div style='background: #161b22; padding: 1rem; border-radius: 8px; border: 1px solid #30363d; margin-bottom: 1rem;'>
                <div style='font-weight: 600; color: #58a6ff; margin-bottom: 0.5rem;'>Model Insights</div>
                <div style='font-size: 0.9rem;'>
                    <div style='margin-bottom: 0.3rem;'><b>Model used:</b> {best_model['Algorithm']}</div>
                    <div style='margin-bottom: 0.5rem;'><b>Accuracy:</b> <span style='color: #3fb950; font-size: 1.2rem; font-weight: 600;'>{best_model['R2']*100:.1f}%</span></div>
                    <div style='color: #8b949e; font-size: 0.85rem; margin-bottom: 0.3rem;'><b>Variables:</b></div>
                    <div style='display: flex; flex-wrap: wrap; gap: 0.3rem;'>
                        <span style='background: #1f6feb; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.75rem;'>Precipitation</span>
                        <span style='background: #1f6feb; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.75rem;'>N Application</span>
                        <span style='background: #1f6feb; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.75rem;'>Soil pH</span>
                        <span style='background: #1f6feb; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.75rem;'>TempMax</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.info("Run ML training first")
        
        # Yield Gap Trend (2020-2024)
        st.markdown("**Yield Gap Trend (2020–2024)**")
        
        trend_df = df.groupby('Year').agg({
            'Attainable_Yield': 'mean',
            'Actual_Yield': 'mean'
        }).reset_index()
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=trend_df['Year'],
            y=trend_df['Attainable_Yield'],
            name='Attainable Yield',
            marker_color='#58a6ff'
        ))
        
        fig.add_trace(go.Bar(
            x=trend_df['Year'],
            y=trend_df['Actual_Yield'],
            name='Actual Yield',
            marker_color='#d29922'
        ))
        
        fig.update_layout(
            barmode='group',
            yaxis_title='Yield (bu/ac)',
            template='plotly_dark',
            paper_bgcolor='#161b22',
            plot_bgcolor='#161b22',
            height=280,
            margin=dict(l=40, r=20, t=20, b=40)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Intervention Recommendations
        st.markdown("**Intervention Recommendations**")
        st.markdown("<small>Personalized steps for Farm 124</small>", unsafe_allow_html=True)
        
        # Get recommendations for a sample farm
        if len(filtered_df) > 0:
            sample_farm = filtered_df.iloc[0]
            try:
                feature_importance_df = pd.read_csv('ml/feature_importance.csv')
            except:
                feature_importance_df = None
            
            recommendations = get_recommendations(sample_farm, feature_importance_df)
            
            for rec in recommendations:
                st.markdown(f"""
                <div style='background: #1a1f2e; padding: 0.8rem; border-radius: 6px; border-left: 3px solid #58a6ff; margin-bottom: 0.6rem;'>
                    <div style='font-size: 1.2rem; margin-bottom: 0.3rem;'>{rec['icon']}</div>
                    <div style='font-weight: 600; color: #e6edf3; margin-bottom: 0.3rem;'>{rec['title']}</div>
                    <div style='font-size: 0.85rem; color: #8b949e;'>{rec['description']}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Select a farm to see recommendations")

if __name__ == "__main__":
    show_dashboard()
'''

with open('yield_gap_analysis/app/dashboard.py', 'w') as f:
    f.write(dashboard_code)

print("✅ Created app/dashboard.py (comprehensive 3-column layout)")
