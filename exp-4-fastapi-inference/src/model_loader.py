import pickle
import logging
from pathlib import Path
from config import MODEL_PATH

logger = logging.getLogger(__name__)

class ModelLoader:
    """Load and cache ML model"""
    
    _instance = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelLoader, cls).__new__(cls)
        return cls._instance
    
    def load_model(self):
        """Load model from disk (singleton)"""
        if self._model is not None:
            logger.info("[CACHE] Model already loaded")
            return self._model
        
        if not MODEL_PATH.exists():
            logger.error(f"[ERROR] Model not found at {MODEL_PATH}")
            raise FileNotFoundError(f"Model missing: {MODEL_PATH}")
        
        try:
            logger.info(f"[LOAD] Loading model from {MODEL_PATH}...")
            with open(MODEL_PATH, 'rb') as f:
                self._model = pickle.load(f)
            logger.info("[SUCCESS] Model loaded!")
            return self._model
        
        except Exception as e:
            logger.error(f"[ERROR] Failed to load model: {str(e)}")
            raise
    
    def get_model(self):
        """Get loaded model"""
        if self._model is None:
            return self.load_model()
        return self._model
    
    def get_model_info(self):
        """Get model metadata"""
        model = self.get_model()
        return {
            "model_type": type(model).__name__,
            "trained_on": "Iris dataset",
            "classes": list(model.classes_),
            "n_features": model.n_features_in_,
            "model_path": str(MODEL_PATH)
        }

# Singleton instance
model_loader = ModelLoader()