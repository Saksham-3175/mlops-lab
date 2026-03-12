import pickle
import logging
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from config import MODEL_PATH, LOG_FILE, TRAIN_TEST_SPLIT, RANDOM_STATE, CI_MODE

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def train_pipeline():
    """End-to-end training pipeline"""
    logger.info("=" * 50)
    logger.info("Starting ML Training Pipeline")
    logger.info(f"CI Mode: {CI_MODE}")
    logger.info("=" * 50)
    
    try:
        # Load data
        logger.info("Loading Iris dataset...")
        data = load_iris()
        X, y = data.data, data.target
        logger.info(f"Dataset shape: {X.shape}, Classes: {len(set(y))}")
        
        # Split
        logger.info("Splitting data...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TRAIN_TEST_SPLIT, random_state=RANDOM_STATE
        )
        logger.info(f"Train: {X_train.shape[0]}, Test: {X_test.shape[0]}")
        
        # Train
        logger.info("Training Logistic Regression...")
        model = LogisticRegression(max_iter=200, random_state=RANDOM_STATE)
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted'),
            'recall': recall_score(y_test, y_pred, average='weighted'),
            'f1': f1_score(y_test, y_pred, average='weighted')
        }
        
        logger.info("=" * 50)
        logger.info("METRICS:")
        for metric, value in metrics.items():
            logger.info(f"{metric.upper()}: {value:.4f}")
        logger.info("=" * 50)
        
        # Save model
        logger.info(f"Saving model to {MODEL_PATH}...")
        with open(MODEL_PATH, 'wb') as f:
            pickle.dump(model, f)
        logger.info("[SUCCESS] Model saved!")
        
        return model, metrics
        
    except Exception as e:
        logger.error(f"[FAILED] Pipeline error: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    train_pipeline()