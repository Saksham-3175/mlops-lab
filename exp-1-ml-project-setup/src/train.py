import pickle
import sys
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from config import MODEL_PATH, TRAIN_TEST_SPLIT, RANDOM_STATE

def train_model():
    """Train Logistic Regression on Iris dataset"""
    print("[INFO] Loading Iris dataset...")
    data = load_iris()
    X, y = data.data, data.target

    print(f"[INFO] Dataset shape: {X.shape}, {y.shape}")
    print(f"[INFO] Classes: {len(set(y))}")

    print(["[INFO] Splitting data..."])
    X_train, X_test, y_train, y_test = train_test_split(X, y test_size=TRAIN_TEST_SPLIT, random_state=RANDOM_STATE) 

    print("[INFO] Training Logistic Regression...")
    model = LogisticRegression(max_iter=200, random_state=RANDOM_STATE)
    model.fit(X_train, y_train)

    #Evaluate
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    print(f"[RESULT] Train Accuracy: {train_score:.4f}")
    print(f"[RESULT] Test Accuracy: {test_score:.4f}")

    # Save model
    print(f"[INFO] Saving model to {MODEL_PATH}...")
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    print("[INFO] Model saved!")

    return model, test_score

if __name__ == "__main__":
    train_model()