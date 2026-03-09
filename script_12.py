
# Create app/models.py
models_code = '''"""
Models Page - ML model comparison and feature importance
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def show_models():
    st.title("🤖 Machine Learning Models")
    
    st.markdown("""
    This page shows the performance of different ML models trained on India farm data 
    to predict yield gaps based on climate, soil, and management factors.
    """)
    
    # Check if models have been trained
    if not os.path.exists('ml/metrics.csv'):
        st.warning("⚠️ Models not trained yet. Please run the training pipeline first.")
        st.code("cd yield_gap_analysis\\npython ml/train_model.py")
        return
    
    # Load metrics
    metrics_df = pd.read_csv('ml/metrics.csv')
    
    # Model comparison section
    st.markdown("### 📊 Model Performance Comparison")
    
    # Highlight best model
    best_model = metrics_df[metrics_df['Best_Model'] == True].iloc[0]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Best Model", best_model['Algorithm'])
    
    with col2:
        st.metric("R² Score", f"{best_model['R2']*100:.1f}%")
    
    with col3:
        st.metric("MAE", f"{best_model['MAE']:.2f} bu/ac")
    
    with col4:
        st.metric("RMSE", f"{best_model['RMSE']:.2f} bu/ac")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Model comparison table
    st.markdown("#### Detailed Model Comparison")
    
    display_df = metrics_df.copy()
    display_df['R2'] = display_df['R2'].apply(lambda x: f"{x*100:.2f}%")
    display_df['Best Model'] = display_df['Best_Model'].apply(lambda x: "✓" if x else "")
    display_df = display_df.drop('Best_Model', axis=1)
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # Visualize model comparison
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # R² comparison
        fig = go.Figure(data=[go.Bar(
            x=metrics_df['Algorithm'],
            y=metrics_df['R2'] * 100,
            marker_color=['#3fb950' if row['Best_Model'] else '#58a6ff' 
                          for _, row in metrics_df.iterrows()]
        )])
        
        fig.update_layout(
            title='R² Score Comparison (%)',
            yaxis_title='R² Score (%)',
            template='plotly_dark',
            paper_bgcolor='#161b22',
            plot_bgcolor='#161b22',
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # RMSE comparison
        fig = go.Figure(data=[go.Bar(
            x=metrics_df['Algorithm'],
            y=metrics_df['RMSE'],
            marker_color=['#3fb950' if row['Best_Model'] else '#f85149' 
                          for _, row in metrics_df.iterrows()]
        )])
        
        fig.update_layout(
            title='RMSE Comparison (bu/ac)',
            yaxis_title='RMSE (bu/ac)',
            template='plotly_dark',
            paper_bgcolor='#161b22',
            plot_bgcolor='#161b22',
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Feature importance section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🎯 Feature Importance Analysis")
    
    if os.path.exists('ml/feature_importance.csv'):
        feature_imp = pd.read_csv('ml/feature_importance.csv')
        
        # Top features
        st.markdown("#### Top 10 Most Important Features")
        
        top_features = feature_imp.head(10)
        
        fig = go.Figure(data=[go.Bar(
            y=top_features['Feature'],
            x=top_features['Importance'],
            orientation='h',
            marker_color='#58a6ff'
        )])
        
        fig.update_layout(
            title='Feature Importance (Higher = More Important)',
            xaxis_title='Importance Score',
            yaxis_title='',
            template='plotly_dark',
            paper_bgcolor='#161b22',
            plot_bgcolor='#161b22',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Feature importance table
        st.markdown("#### All Features")
        st.dataframe(feature_imp, use_container_width=True, hide_index=True)
        
    else:
        st.info("Feature importance not available. Train a tree-based model.")
    
    # Model download
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 💾 Download Trained Model")
    
    if os.path.exists('ml/model.pkl'):
        with open('ml/model.pkl', 'rb') as f:
            st.download_button(
                label="Download model.pkl",
                data=f,
                file_name="yield_gap_model.pkl",
                mime="application/octet-stream"
            )
        st.success("Model ready for download!")
    else:
        st.info("Train the model first to enable download.")

if __name__ == "__main__":
    show_models()
'''

with open('yield_gap_analysis/app/models.py', 'w') as f:
    f.write(models_code)

print("✅ Created app/models.py")
