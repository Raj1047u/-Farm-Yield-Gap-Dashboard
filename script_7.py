
# Create utils/recommendations.py
utils_recommendations_code = '''"""
Intervention Recommendation Engine
Provides personalized recommendations based on farm data and ML insights
"""

import pandas as pd
import numpy as np

def get_recommendations(farm_row, feature_importance_df=None):
    """
    Generate top 3 personalized recommendations for a farm
    
    Args:
        farm_row: DataFrame row or dict with farm data
        feature_importance_df: Feature importance from ML model
    
    Returns:
        List of recommendation dicts with icon, title, description
    """
    recommendations = []
    
    # Convert to dict if DataFrame row
    if hasattr(farm_row, 'to_dict'):
        farm = farm_row.to_dict()
    else:
        farm = farm_row
    
    # Rule 1: Nitrogen Application
    if farm.get('N_Application', 0) < 110:
        recommendations.append({
            'icon': '💡',
            'title': 'Improve N Efficiency',
            'description': f"Current N application ({farm.get('N_Application', 0):.1f} kg/ha) is below optimal. Increase nitrogen fertilizer application by 20-30% and split applications for better uptake efficiency."
        })
    elif farm.get('N_Application', 0) > 160:
        recommendations.append({
            'icon': '⚖️',
            'title': 'Optimize N Application',
            'description': f"N application ({farm.get('N_Application', 0):.1f} kg/ha) may be excessive. Consider soil testing and precision application to avoid waste and environmental impact."
        })
    
    # Rule 2: Irrigation
    if farm.get('Irrigation_Type') == 'rainfed':
        recommendations.append({
            'icon': '💧',
            'title': 'Adjust Irrigation',
            'description': 'Rainfed agriculture increases yield variability. Consider supplemental irrigation during critical growth stages, especially drip or sprinkler systems for water efficiency.'
        })
    elif farm.get('Irrigation_Type') == 'canal' and farm.get('Precipitation', 0) < 600:
        recommendations.append({
            'icon': '💧',
            'title': 'Enhance Water Management',
            'description': 'Low rainfall region with canal irrigation. Implement water-saving techniques like alternate wetting and drying (AWD) or laser land leveling to improve water use efficiency.'
        })
    
    # Rule 3: Soil pH
    soil_ph = farm.get('Soil_pH', 7.0)
    if soil_ph < 6.0:
        recommendations.append({
            'icon': '🧪',
            'title': 'Conduct Soil Test - pH Too Low',
            'description': f"Soil pH ({soil_ph:.1f}) is acidic. Apply lime (calcium carbonate) at 2-3 tonnes/hectare to raise pH to 6.5-7.5 range for optimal nutrient availability."
        })
    elif soil_ph > 8.0:
        recommendations.append({
            'icon': '🧪',
            'title': 'Conduct Soil Test - pH Too High',
            'description': f"Soil pH ({soil_ph:.1f}) is alkaline. Apply gypsum or sulfur amendments to lower pH. Consider acidifying fertilizers like ammonium sulfate."
        })
    elif soil_ph < 6.5 or soil_ph > 7.5:
        recommendations.append({
            'icon': '🧪',
            'title': 'Soil pH Optimization',
            'description': f"Soil pH ({soil_ph:.1f}) is slightly out of optimal range (6.5-7.5). Regular soil testing and minor amendments can improve nutrient uptake efficiency."
        })
    
    # Rule 4: Pest Control
    if farm.get('Pest_Control_Score', 10) < 6.5:
        recommendations.append({
            'icon': '🐛',
            'title': 'Improve Pest Management',
            'description': f"Pest control score ({farm.get('Pest_Control_Score', 0):.1f}/10) indicates room for improvement. Implement integrated pest management (IPM): crop rotation, biological controls, and targeted pesticide use."
        })
    
    # Rule 5: Fertilizer Management
    if farm.get('Fertilizer_Mgmt_Score', 10) < 6.5:
        recommendations.append({
            'icon': '🌱',
            'title': 'Enhance Fertilizer Management',
            'description': f"Fertilizer management score ({farm.get('Fertilizer_Mgmt_Score', 0):.1f}/10) suggests optimization needed. Adopt balanced NPK ratios, micronutrient supplementation, and split applications based on crop growth stages."
        })
    
    # Rule 6: Hybrid Selection
    if farm.get('Hybrid_Selection_Score', 10) < 7.0:
        recommendations.append({
            'icon': '🌾',
            'title': 'Upgrade Seed Variety',
            'description': f"Hybrid selection score ({farm.get('Hybrid_Selection_Score', 0):.1f}/10) indicates potential for better varieties. Consider high-yielding, disease-resistant hybrids suitable for {farm.get('Region', 'your region')}."
        })
    
    # Rule 7: Climate-based (Low Precipitation)
    if farm.get('Precipitation', 1000) < 500 and 'Irrigation' not in [r['title'] for r in recommendations]:
        recommendations.append({
            'icon': '☔',
            'title': 'Climate Adaptation',
            'description': f"Low rainfall ({farm.get('Precipitation', 0):.0f} mm). Consider drought-tolerant varieties, mulching to retain soil moisture, and rainwater harvesting systems."
        })
    
    # Rule 8: Temperature stress
    if farm.get('TempMax', 30) > 38:
        recommendations.append({
            'icon': '🌡️',
            'title': 'Heat Stress Mitigation',
            'description': f"High temperatures ({farm.get('TempMax', 0):.1f}°C) can reduce yields. Consider shade nets, adjusting planting dates, and heat-tolerant varieties."
        })
    
    # Rule 9: Soil Quality
    if farm.get('Soil_Quality_Score', 100) < 70:
        recommendations.append({
            'icon': '🌍',
            'title': 'Improve Soil Health',
            'description': f"Soil quality score ({farm.get('Soil_Quality_Score', 0):.1f}/100) is low. Increase organic matter through compost, green manure, and crop residue incorporation. Reduce tillage to preserve soil structure."
        })
    
    # ML-based recommendation (if feature importance available)
    if feature_importance_df is not None and len(recommendations) < 3:
        top_feature = feature_importance_df.iloc[0]
        recommendations.append({
            'icon': '🤖',
            'title': 'ML-Driven Insight',
            'description': f"ML model identifies '{top_feature['Feature']}' as most important factor. Focus management practices on optimizing this parameter for maximum yield improvement."
        })
    
    # Return top 3 recommendations
    return recommendations[:3]

def get_bulk_recommendations(farms_df, feature_importance_df=None):
    """Generate recommendations for multiple farms"""
    all_recommendations = []
    
    for idx, row in farms_df.iterrows():
        farm_recs = get_recommendations(row, feature_importance_df)
        all_recommendations.append({
            'Farm_ID': row['Farm_ID'],
            'recommendations': farm_recs
        })
    
    return all_recommendations
'''

with open('yield_gap_analysis/utils/recommendations.py', 'w') as f:
    f.write(utils_recommendations_code)

print("✅ Created utils/recommendations.py")
