import os 
from pathlib import Path 

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
MODELS_DIR = PROJECT_ROOT / 'models'

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

# model hyperparameters
TRAIN_TEST_SPLIT = 0.2
RANDOM_STATE = 42
MODEL_NAME = 'iris_classifier.pkl'
MODEL_PATH = MODELS_DIR / MODEL_NAME