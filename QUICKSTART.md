# 🚀 Quick Start Guide

## Installation (5 minutes)

### Step 1: Navigate to Project
```bash
cd yield_gap_analysis
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Train ML Models
```bash
python ml/train_model.py
```

Expected output:
```
🌾 AI Farm Yield Gap Analysis - Model Training Pipeline
  ✓ Loaded 220 farm records from India
  ✓ Prepared 16 features
  🏆 Best Model: Random Forest Regressor (R² ~89%)
  ✅ Training complete!
```

### Step 4: Launch Application
```bash
streamlit run app/main.py
```

The app will open at `http://localhost:8501`

---

## First Time Using the App

### 1. **Dashboard Page** (Default)
- Use the **5 top filters** to select data:
  - Country: India (default)
  - Region: Choose any Indian state
  - Crop Type: Wheat, Rice, Maize, Cotton, Sugarcane
  - Year: 2020-2024
  - Yield Gap Type: Attainable vs. Actual

### 2. **Explore the 3-Column Layout**

**Left Column:**
- Interactive India map with color-coded farms
- Click markers to see farm details
- Farm selection table below

**Middle Column:**
- 3 tabs: Overview, Interactive Analysis, Yield Driver
- Donut chart showing yield distribution
- Feature importance from ML model

**Right Column:**
- ML model performance (~89% R²)
- Yield gap trend (2020-2024)
- Top 3 intervention recommendations

### 3. **Navigate Other Pages**
- **🗺️ Farm Map**: Full-screen India map
- **🤖 Models**: Compare ML models and download trained model
- **📄 Reports**: Generate and download CSV reports
- **🗄️ Data Sources**: Upload custom data or explore existing
- **⚙️ Settings**: Configure preferences

---

## Key Features to Try

1. **Filter by Region**: Select "Punjab" to see high-yield wheat farms
2. **View Recommendations**: Check personalized intervention suggestions
3. **Download Report**: Go to Reports page → Download CSV
4. **Explore Feature Importance**: Models page → See which factors matter most
5. **Upload Custom Data**: Data Sources page → Upload your own CSV

---

## Troubleshooting

**App won't start?**
```bash
# Check if port 8501 is available
streamlit run app/main.py --server.port 8502
```

**Maps not showing?**
- Ensure internet connection (maps need tile data)
- Check firewall settings

**Import errors?**
```bash
pip install -r requirements.txt --upgrade
```

---

## Next Steps

- Explore different crop types and regions
- Generate reports for specific years
- Try uploading custom India farm data
- Download the trained model for external use

---

**Need help?** Check README.md for detailed documentation.
