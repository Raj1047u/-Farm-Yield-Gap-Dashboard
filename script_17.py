
# Create comprehensive README.md
readme = '''# 🌾 AI Farm Yield Gap Analysis Platform

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29-red)
![scikit--learn](https://img.shields.io/badge/scikit--learn-1.3-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-green)
![Plotly](https://img.shields.io/badge/Plotly-5.18-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered, end-to-end platform for analyzing and closing yield gaps in Indian agriculture. This production-ready application uses machine learning to predict yield gaps and provide personalized intervention recommendations for farmers across India.

## 🎯 Key Features

- **📊 Interactive Dashboard**: 3-column layout with India farm map, yield gap analysis, and ML insights
- **🗺️ Geospatial Mapping**: Interactive Folium maps showing yield gaps across Indian states
- **🤖 ML Models**: Multiple regression models (Random Forest, XGBoost, Linear, Decision Tree)
- **💡 Smart Recommendations**: Personalized intervention strategies based on farm data
- **📈 Real-time Analytics**: Dynamic filtering and visualization of 220+ farm records
- **📄 Report Generation**: Downloadable CSV reports with comprehensive analysis
- **🎨 Dark Theme UI**: Modern, responsive Streamlit interface

## 🗺️ India-Only Focus

All data, maps, and analysis are specific to **India**:
- **14 Indian states** covered (Punjab, Haryana, UP, Bihar, MP, Maharashtra, Karnataka, AP, Telangana, Gujarat, Rajasthan, West Bengal, Odisha, Tamil Nadu)
- **220+ farm records** with valid India coordinates
- **5 major crops**: Wheat, Rice, Maize, Cotton, Sugarcane
- **2020-2024** data coverage

## 🏗️ Tech Stack

### Backend & ML
- **Python 3.9+**
- **FastAPI** (API framework, ready for expansion)
- **scikit-learn** (ML models)
- **XGBoost** (Gradient boosting)
- **Pandas & NumPy** (Data processing)

### Frontend & Visualization
- **Streamlit** (Web UI with dark theme)
- **Plotly** (Interactive charts)
- **Folium** (Interactive maps)
- **Matplotlib & Seaborn** (Additional plots)

### Data Storage
- **CSV-based** data storage (SQLite-ready architecture)
- Synthetic India farm dataset included

## 📁 Project Structure

```
yield_gap_analysis/
│
├── app/
│   ├── main.py              # Streamlit app entry point
│   ├── dashboard.py         # Main dashboard (3-column layout)
│   ├── farm_map.py          # Interactive India map page
│   ├── models.py            # ML model comparison page
│   ├── reports.py           # Report generation page
│   ├── data_sources.py      # Data upload and preview
│   └── settings.py          # Settings and preferences
│
├── ml/
│   ├── train_model.py       # Model training pipeline
│   ├── predict.py           # Prediction utilities
│   ├── model.pkl            # Trained model (generated)
│   ├── metrics.csv          # Model evaluation metrics
│   └── feature_importance.csv  # Feature importance scores
│
├── data/
│   ├── farms_data.csv       # 220+ India farm records
│   ├── weather_data.csv     # Climate data by region
│   └── soil_data.csv        # Soil quality data
│
├── utils/
│   ├── preprocess.py        # Data preprocessing utilities
│   └── recommendations.py   # Intervention recommendation engine
│
├── assets/
│   └── style.css            # Custom dark theme styling
│
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager
- 4GB RAM minimum
- Internet connection (for map tiles)

### Installation

1. **Clone or download the project**

```bash
cd yield_gap_analysis
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Train ML models**

```bash
python ml/train_model.py
```

Expected output:
```
🌾 AI Farm Yield Gap Analysis - Model Training Pipeline
  ✓ Loaded 220 farm records from India
  ✓ Prepared 16 features
  Training models...
  🏆 Best Model: Random Forest Regressor
  R² Score: ~89%
  ✅ Training complete!
```

4. **Launch the application**

```bash
streamlit run app/main.py
```

The app will open in your browser at `http://localhost:8501`

## 📊 Usage Guide

### Dashboard Page

The main dashboard features a **3-column layout**:

**Left Column - Interactive Map:**
- India-centered Folium map
- Color-coded yield gap markers (Red/Orange/Green)
- Click markers for farm details
- Farm selection table below map

**Middle Column - Analysis Tabs:**
- **Yield Gap Overview**: Donut chart showing attainable vs actual yields
- **Interactive Analysis**: Scatter plots and correlations
- **Yield Driver Analysis**: Feature importance from ML model

**Right Column - ML Insights:**
- Best model performance metrics
- Yield gap trend (2020-2024)
- Top 3 personalized recommendations per farm

**Top Filters:**
- Country (India)
- Region (14 states)
- Crop Type (5 crops)
- Year (2020-2024)
- Yield Gap Type

### Farm Map Page

- Full-screen India map
- Advanced filtering options
- Summary statistics
- Popup details for each farm

### Models Page

- Model performance comparison table
- R² and RMSE visualizations
- Feature importance analysis
- Download trained model

### Reports Page

- Generate farm-wise yield gap reports
- Download as CSV
- Visual analytics by region/crop
- Correlation analysis

### Data Sources Page

- Upload custom India farm data (CSV)
- Preview and search existing data
- Data quality statistics
- Download datasets

### Settings Page

- Theme preferences
- User profile configuration
- Notification settings
- Advanced model parameters

## 🤖 Machine Learning Pipeline

### Problem Framing

- **Type**: Regression
- **Target**: `Yield_Gap` (Attainable_Yield - Actual_Yield)
- **Features**: Climate (precipitation, temperature), soil (pH, quality), management (fertilizer, pest control, hybrid selection)

### Models Trained

1. **Linear Regression** (baseline)
2. **Decision Tree Regressor**
3. **Random Forest Regressor** ⭐ (expected best: ~89% R²)
4. **XGBoost Regressor**

### Evaluation Metrics

- **R² Score** (coefficient of determination)
- **MAE** (Mean Absolute Error)
- **MSE** (Mean Squared Error)
- **RMSE** (Root Mean Squared Error)

### Top 5 Feature Importances

1. **Precipitation** (Climate)
2. **N_Application** (Fertilizer Management)
3. **Soil_pH** (Soil Quality)
4. **TempMax** (Climate)
5. **Soil_Quality_Score** (Soil)

## 💡 Recommendation Engine

The platform provides **personalized intervention recommendations** based on:

### Rule-Based Logic
- **Nitrogen Efficiency**: If N application < 110 kg/ha
- **Irrigation**: If rainfed or low rainfall region
- **Soil pH**: If pH < 6.0 or > 8.0
- **Pest Control**: If pest control score < 6.5
- **Fertilizer Management**: If fertilizer management score < 6.5
- **Hybrid Selection**: If hybrid selection score < 7.0

### Example Recommendations
1. 💡 **Improve N Efficiency** - Increase nitrogen application by 20-30%
2. 💧 **Adjust Irrigation** - Implement drip irrigation system
3. 🧪 **Conduct Soil Test** - Apply lime to correct pH

## 📈 Dataset Details

### Farms Data (220+ records)

**Columns:**
- `Farm_ID`: Unique farm identifier (FARM_001 to FARM_220)
- `Country`: India (all records)
- `Region`: 14 Indian states
- `Crop_Type`: Wheat, Rice, Maize, Cotton, Sugarcane
- `Year`: 2020-2024
- `Season`: Kharif, Rabi
- `Attainable_Yield`: bu/ac
- `Actual_Yield`: bu/ac
- `Yield_Gap`: bu/ac (target variable)
- `Precipitation`: mm
- `TempMax`, `TempMin`: °C
- `N_Application`: kg/ha
- `Soil_pH`: 5.5-8.0
- `Soil_Quality_Score`: 0-100
- `Irrigation_Type`: canal, tube_well, rainfed, drip
- `Fertilizer_Mgmt_Score`: 0-10
- `Pest_Control_Score`: 0-10
- `Hybrid_Selection_Score`: 0-10
- `Latitude`, `Longitude`: Valid India coordinates

### Weather Data (70 records)
- Regional climate averages by year
- Precipitation, TempMax, TempMin

### Soil Data (70 records)
- Regional soil characteristics by year
- Soil pH, Soil Quality Score

## 🎨 UI Design

### Dark Theme
- **Background**: #0d1117 (primary), #161b22 (secondary)
- **Text**: #e6edf3 (primary), #8b949e (secondary)
- **Accent**: #58a6ff (primary), #1f6feb (secondary)
- **Status Colors**: Green (#3fb950), Orange (#d29922), Red (#f85149)

### User Profile
- **Name**: Dr. Anya Sharma
- **Role**: Lead Agronomist
- Displayed in sidebar with avatar

## 🔮 Future Enhancements

- [ ] SQLite/PostgreSQL database integration
- [ ] REST API with FastAPI
- [ ] Real-time data ingestion
- [ ] PDF report generation with charts
- [ ] Email notification system
- [ ] Multi-language support (Hindi, regional languages)
- [ ] Mobile-responsive design
- [ ] User authentication
- [ ] Historical data comparison
- [ ] Weather API integration (live data)
- [ ] Docker containerization
- [ ] Cloud deployment (AWS/Azure/GCP)

## 📸 Screenshots

### Dashboard
![Dashboard](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)

### Farm Map
![Farm Map](https://via.placeholder.com/800x400?text=Farm+Map+Screenshot)

### Models Comparison
![Models](https://via.placeholder.com/800x400?text=Models+Screenshot)

*Note: Replace placeholders with actual screenshots*

## 🐛 Troubleshooting

### Common Issues

**1. Import errors**
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --upgrade
```

**2. Model not found error**
```bash
# Solution: Train models first
python ml/train_model.py
```

**3. Map not displaying**
- Check internet connection (required for map tiles)
- Verify Folium installation: `pip install folium streamlit-folium`

**4. Port already in use**
```bash
# Solution: Use different port
streamlit run app/main.py --server.port 8502
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Lead Developer**: Agricultural Research Team
- **ML Engineer**: Data Science Division
- **Domain Expert**: Dr. Anya Sharma (Lead Agronomist)

## 📧 Contact

For questions or support:
- Email: support@agri-research.in
- GitHub Issues: [Open an issue](https://github.com/your-repo/yield-gap-analysis/issues)

## 🙏 Acknowledgments

- Indian Agricultural Research Institute (IARI)
- State Agricultural Departments across India
- Open-source community (Streamlit, scikit-learn, Plotly)

---

**Built with ❤️ for Indian farmers**

*Closing the yield gap, one farm at a time* 🌾
'''

with open('yield_gap_analysis/README.md', 'w') as f:
    f.write(readme)

print("✅ Created comprehensive README.md")
