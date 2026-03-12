import pickle
from sklearn.datasets import load_iris
from config import MODEL_PATH, TRAIN_TEST_SPLIT, RANDOM_STATE
from sklearn.model_selection import train_test_split

def evaluate_model():
    """Load and evaluate saved model"""
    print(f"[INFO] Loading model from {MODEL_PATH}...")

    if not MODEL_PATH.exists():
        print(f"[ERROR] Model not found at {MODEL_PATH}...")
        return
    
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

        print("[INFO] Loading Iris dataset...")
        
        data = load_iris()
        
        X, y = data.data, data.target
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TRAIN_TEST_SPLIT, random_state=RANDOM_STATE)

        test_score = model.score(X_test, y_test)
        print(f"[INFO] Test Accuracy: {test_score:.4f}")

if __name__ == "__main__":
    evaluate_model()