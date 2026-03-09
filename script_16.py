
# Create requirements.txt
requirements = '''# Core dependencies
streamlit==1.29.0
pandas==2.1.4
numpy==1.26.2

# Machine Learning
scikit-learn==1.3.2
xgboost==2.0.3
joblib==1.3.2
shap==0.44.0

# Visualization
plotly==5.18.0
folium==0.15.1
streamlit-folium==0.15.1
matplotlib==3.8.2
seaborn==0.13.0

# API (for future use)
fastapi==0.108.0
uvicorn==0.25.0

# Utilities
reportlab==4.0.7
openpyxl==3.1.2
'''

with open('yield_gap_analysis/requirements.txt', 'w') as f:
    f.write(requirements)

print("✅ Created requirements.txt")
