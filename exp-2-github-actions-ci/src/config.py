import os
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create directories
for dir_path in [DATA_DIR, MODELS_DIR, LOGS_DIR]:
    dir_path.mkdir(exist_ok=True)

# Model hyperparams
TRAIN_TEST_SPLIT = 0.2
RANDOM_STATE = 42
MODEL_NAME = "iris_classifier.pkl"
MODEL_PATH = MODELS_DIR / MODEL_NAME
LOG_FILE = LOGS_DIR / "training.log"

# CI/CD flags
CI_MODE = os.getenv("CI", "false").lower() == "true"