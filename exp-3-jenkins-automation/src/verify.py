import pickle
import logging
from pathlib import Path
from config import MODEL_PATH, LOG_FILE

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def verify_model():
    """Verify that model was saved correctly"""
    logger.info("[VERIFY] Checking model artifact...")
    
    if not MODEL_PATH.exists():
        logger.error(f"[ERROR] Model not found at {MODEL_PATH}")
        raise FileNotFoundError(f"Model missing: {MODEL_PATH}")
    
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        logger.info(f"[SUCCESS] Model loaded successfully")
        logger.info(f"Model type: {type(model).__name__}")
        logger.info(f"Model file size: {MODEL_PATH.stat().st_size} bytes")
        
        # Check log file
        if LOG_FILE.exists():
            logger.info(f"[SUCCESS] Log file exists: {LOG_FILE}")
        
        logger.info("[SUCCESS] All artifacts verified!")
        return True
        
    except Exception as e:
        logger.error(f"[ERROR] Verification failed: {str(e)}")
        raise

if __name__ == "__main__":
    verify_model()