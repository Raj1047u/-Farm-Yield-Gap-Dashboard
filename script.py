
import os
import pandas as pd
import numpy as np

# Create project structure
project_dirs = [
    'yield_gap_analysis/app',
    'yield_gap_analysis/ml',
    'yield_gap_analysis/data',
    'yield_gap_analysis/utils',
    'yield_gap_analysis/assets'
]

for directory in project_dirs:
    os.makedirs(directory, exist_ok=True)
    
print("✅ Project structure created successfully!")
print("\nDirectories created:")
for d in project_dirs:
    print(f"  - {d}")
