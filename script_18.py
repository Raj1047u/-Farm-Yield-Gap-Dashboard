
# Change to project directory and run ML training
import os
os.chdir('yield_gap_analysis')

# Run the training pipeline
exec(open('ml/train_model.py').read())
