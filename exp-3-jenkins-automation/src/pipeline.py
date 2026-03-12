import pickle
import logging
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from config import MODEL_PATH, LOG_FILE, TRAIN_TEST_SPLIT, RANDOM_STATE, JENKINS_BUILD_ID

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
    """End-to-end training pipeline triggered by Jenkins"""
    logger.info("=" * 60)
    logger.info("Jenkins ML Training Pipeline")
    logger.info(f"Build ID: {JENKINS_BUILD_ID}")
    logger.info("=" * 60)
    
    try:
        # Load data
        logger.info("[STEP 1] Loading Iris dataset...")
        data = load_iris()
        X, y = data.data, data.target
        logger.info(f"Dataset loaded: shape={X.shape}, classes={len(set(y))}")
        
        # Split
        logger.info("[STEP 2] Splitting data (train/test)...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TRAIN_TEST_SPLIT, random_state=RANDOM_STATE
        )
        logger.info(f"Train samples: {len(X_train)}, Test samples: {len(X_test)}")
        
        # Train
        logger.info("[STEP 3] Training Logistic Regression model...")
        model = LogisticRegression(max_iter=200, random_state=RANDOM_STATE)
        model.fit(X_train, y_train)
        logger.info("Model training complete")
        
        # Evaluate
        logger.info("[STEP 4] Evaluating model...")
        y_pred = model.predict(X_test)
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted'),
            'recall': recall_score(y_test, y_pred, average='weighted'),
            'f1': f1_score(y_test, y_pred, average='weighted')
        }
        
        logger.info("=" * 60)
        logger.info("EVALUATION METRICS")
        logger.info("=" * 60)
        for metric, value in metrics.items():
            logger.info(f"{metric.upper()}: {value:.4f}")
        
        # Save model
        logger.info(f"[STEP 5] Saving model to {MODEL_PATH}...")
        with open(MODEL_PATH, 'wb') as f:
            pickle.dump(model, f)
        logger.info("[SUCCESS] Model saved!")
        logger.info("=" * 60)
        
        return model, metrics
        
    except Exception as e:
        logger.error(f"[ERROR] Pipeline failed: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    train_pipeline()