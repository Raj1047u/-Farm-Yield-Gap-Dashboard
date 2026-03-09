
# Create app/settings.py
settings_code = '''"""
Settings Page - User preferences and configuration
"""

import streamlit as st

def show_settings():
    st.title("⚙️ Settings")
    
    st.markdown("""
    Configure application preferences and user settings.
    """)
    
    # Theme settings
    st.markdown("### 🎨 Theme Settings")
    
    theme = st.radio(
        "Color Theme",
        ["Dark (Current)", "Light"],
        help="Switch between dark and light themes"
    )
    
    if theme == "Light":
        st.info("💡 Light theme will be applied in future update")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # User profile
    st.markdown("### 👤 User Profile")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name", value="Dr. Anya Sharma")
        role = st.text_input("Role", value="Lead Agronomist")
    
    with col2:
        organization = st.text_input("Organization", value="Agricultural Research Institute")
        email = st.text_input("Email", value="anya.sharma@agri-research.in")
    
    if st.button("💾 Save Profile"):
        st.success("✅ Profile saved successfully!")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Data settings
    st.markdown("### 📊 Data Settings")
    
    auto_refresh = st.checkbox("Auto-refresh data", value=False)
    
    refresh_interval = st.selectbox(
        "Data refresh interval",
        ["1 hour", "6 hours", "12 hours", "24 hours"],
        index=3
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Notification settings
    st.markdown("### 🔔 Notifications")
    
    email_notifications = st.checkbox("Email notifications", value=True)
    
    notification_types = st.multiselect(
        "Notification types",
        ["High yield gap alerts", "New data available", "Model updates", "System maintenance"],
        default=["High yield gap alerts", "New data available"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Export settings
    st.markdown("### 💾 Export Settings")
    
    default_format = st.selectbox(
        "Default export format",
        ["CSV", "Excel", "PDF"],
        index=0
    )
    
    include_charts = st.checkbox("Include charts in exports", value=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Advanced settings
    with st.expander("🔧 Advanced Settings"):
        st.markdown("**Model Configuration**")
        
        model_threshold = st.slider(
            "Yield gap threshold for alerts (bu/ac)",
            min_value=20,
            max_value=80,
            value=50
        )
        
        confidence_level = st.slider(
            "Prediction confidence level (%)",
            min_value=80,
            max_value=99,
            value=95
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Performance**")
        
        cache_data = st.checkbox("Enable data caching", value=True)
        max_cache_size = st.selectbox(
            "Maximum cache size",
            ["100 MB", "250 MB", "500 MB", "1 GB"],
            index=1
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # About section
    st.markdown("### ℹ️ About")
    
    st.markdown("""
    **AI Farm Yield Gap Analysis Platform**
    
    Version: 1.0.0  
    
    An AI-powered platform for analyzing and closing yield gaps in Indian agriculture.
    Built with Python, Streamlit, scikit-learn, and XGBoost.
    
    **Tech Stack:**
    - Backend: Python, FastAPI
    - ML: scikit-learn, XGBoost, Random Forest
    - Frontend: Streamlit
    - Visualization: Plotly, Folium
    - Data: Pandas, NumPy
    
    **Data Source:** Synthetic India farm data (220+ farms across 14 states)
    
    © 2024 Agricultural Research Institute. All rights reserved.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Reset settings
    if st.button("🔄 Reset All Settings to Default", type="secondary"):
        st.warning("⚠️ This will reset all settings to their default values.")
        if st.button("Confirm Reset"):
            st.success("✅ Settings reset to defaults!")
            st.rerun()

if __name__ == "__main__":
    show_settings()
'''

with open('yield_gap_analysis/app/settings.py', 'w') as f:
    f.write(settings_code)

print("✅ Created app/settings.py")
