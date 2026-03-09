
# Install xgboost
import subprocess
subprocess.run(['pip', 'install', 'xgboost', '-q'], check=True)
print("✅ Installed XGBoost")

# Now run training
exec(open('ml/train_model.py').read())
