import pytest
import pickle
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from config import MODEL_PATH, TRAIN_TEST_SPLIT, RANDOM_STATE

class TestTrainingPipeline:
    """Unit tests for training pipeline"""
    
    def test_data_loading(self):
        """Test that data loads correctly"""
        data = load_iris()
        assert data.data.shape[0] == 150
        assert data.data.shape[1] == 4
        assert len(set(data.target)) == 3
    
    def test_train_test_split(self):
        """Test data splitting"""
        data = load_iris()
        X, y = data.data, data.target
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TRAIN_TEST_SPLIT, random_state=RANDOM_STATE
        )
        
        assert len(X_train) + len(X_test) == len(X)
        assert len(X_train) == int(150 * (1 - TRAIN_TEST_SPLIT))
        assert len(X_test) == int(150 * TRAIN_TEST_SPLIT)
    
    def test_model_training(self):
        """Test that model trains without errors"""
        data = load_iris()
        X, y = data.data, data.target
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TRAIN_TEST_SPLIT, random_state=RANDOM_STATE
        )
        
        model = LogisticRegression(max_iter=200, random_state=RANDOM_STATE)
        model.fit(X_train, y_train)
        
        assert model is not None
        assert hasattr(model, 'predict')
        assert len(model.classes_) == 3
    
    def test_model_accuracy(self):
        """Test that model achieves reasonable accuracy"""
        data = load_iris()
        X, y = data.data, data.target
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TRAIN_TEST_SPLIT, random_state=RANDOM_STATE
        )
        
        model = LogisticRegression(max_iter=200, random_state=RANDOM_STATE)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        
        assert score > 0.8  # Model should achieve >80% accuracy
    
    def test_model_persistence(self):
        """Test that model can be saved and loaded"""
        data = load_iris()
        X, y = data.data, data.target
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TRAIN_TEST_SPLIT, random_state=RANDOM_STATE
        )
        
        model = LogisticRegression(max_iter=200, random_state=RANDOM_STATE)
        model.fit(X_train, y_train)
        
        # Save
        MODEL_PATH.parent.mkdir(exist_ok=True)
        with open(MODEL_PATH, 'wb') as f:
            pickle.dump(model, f)
        
        assert MODEL_PATH.exists()
        
        # Load
        with open(MODEL_PATH, 'rb') as f:
            loaded_model = pickle.load(f)
        
        assert loaded_model.score(X_test, y_test) == model.score(X_test, y_test)