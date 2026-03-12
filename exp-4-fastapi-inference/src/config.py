import os
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create directories
MODELS_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# Model
MODEL_NAME = "iris_classifier.pkl"
MODEL_PATH = MODELS_DIR / MODEL_NAME

# Server
HOST = os.getenv("API_HOST", "0.0.0.0")
PORT = int(os.getenv("API_PORT", 8000))
DEBUG = os.getenv("API_DEBUG", "False").lower() == "true"
WORKERS = int(os.getenv("API_WORKERS", 4))

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Class mapping
CLASS_NAMES = {0: "setosa", 1: "versicolor", 2: "virginica"}