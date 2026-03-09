
# Create app/main.py - Entry point
main_app_code = '''"""
AI Farm Yield Gap Analysis Platform
Main entry point for the Streamlit application
"""

import streamlit as st
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Page configuration
st.set_page_config(
    page_title="AI Farm Yield Gap Analysis",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

try:
    load_css()
except:
    pass

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Dashboard'

# Sidebar navigation
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0; border-bottom: 1px solid #30363d;'>
        <h1 style='font-size: 1.8rem; margin: 0; color: #58a6ff;'>🌾 AI Farm Yield Gap</h1>
        <p style='font-size: 0.9rem; color: #8b949e; margin: 0.5rem 0 0 0;'>Analysis Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigation menu
    pages = {
        '📊 Dashboard': 'Dashboard',
        '🗺️ Farm Map': 'Farm Map',
        '🤖 Models': 'Models',
        '📄 Reports': 'Reports',
        '🗄️ Data Sources': 'Data Sources',
        '⚙️ Settings': 'Settings'
    }
    
    for label, page in pages.items():
        if st.button(label, key=page, use_container_width=True):
            st.session_state.current_page = page
    
    # User profile card at bottom
    st.markdown("<br>" * 8, unsafe_allow_html=True)
    st.markdown("""
    <div style='position: fixed; bottom: 20px; width: 250px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 1rem;'>
        <div style='display: flex; align-items: center; gap: 12px;'>
            <div style='width: 40px; height: 40px; background: linear-gradient(135deg, #58a6ff, #1f6feb); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: white;'>AS</div>
            <div>
                <div style='font-weight: 600; color: #e6edf3;'>Dr. Anya Sharma</div>
                <div style='font-size: 0.85rem; color: #8b949e;'>Lead Agronomist</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main content area - route to appropriate page
current_page = st.session_state.current_page

if current_page == 'Dashboard':
    from dashboard import show_dashboard
    show_dashboard()
elif current_page == 'Farm Map':
    from farm_map import show_farm_map
    show_farm_map()
elif current_page == 'Models':
    from models import show_models
    show_models()
elif current_page == 'Reports':
    from reports import show_reports
    show_reports()
elif current_page == 'Data Sources':
    from data_sources import show_data_sources
    show_data_sources()
elif current_page == 'Settings':
    from settings import show_settings
    show_settings()
'''

with open('yield_gap_analysis/app/main.py', 'w') as f:
    f.write(main_app_code)

print("✅ Created app/main.py")
