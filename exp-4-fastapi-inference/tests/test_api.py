import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import app

client = TestClient(app)

class TestAPIEndpoints:
    """Test FastAPI endpoints"""
    
    def test_health_check(self):
        """Test health endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "timestamp" in data
    
    def test_model_info(self):
        """Test model info endpoint"""
        response = client.get("/model/info")
        assert response.status_code == 200
        data = response.json()
        assert data["model_type"] == "LogisticRegression"
        assert data["n_features"] == 4
        assert len(data["classes"]) == 3
    
    def test_single_prediction_valid(self):
        """Test single prediction with valid input"""
        response = client.post("/predict", json={
            "feature1": 5.1,
            "feature2": 3.5,
            "feature3": 1.4,
            "feature4": 0.2
        })
        assert response.status_code == 200
        data = response.json()
        assert "prediction" in data
        assert "confidence" in data
        assert "class_name" in data
        assert 0 <= data["confidence"] <= 1
        assert data["prediction"] in [0, 1, 2]
    
    def test_single_prediction_invalid(self):
        """Test single prediction with invalid input"""
        response = client.post("/predict", json={
            "feature1": "invalid",
            "feature2": 3.5,
            "feature3": 1.4,
            "feature4": 0.2
        })
        assert response.status_code == 422  # Validation error
    
    def test_batch_prediction_valid(self):
        """Test batch prediction with valid input"""
        response = client.post("/batch-predict", json={
            "samples": [
                [5.1, 3.5, 1.4, 0.2],
                [7.0, 3.2, 4.7, 1.4]
            ]
        })
        assert response.status_code == 200
        data = response.json()
        assert len(data["predictions"]) == 2
        assert len(data["confidence_scores"]) == 2
        assert data["count"] == 2
    
    def test_batch_prediction_empty(self):
        """Test batch prediction with empty input"""
        response = client.post("/batch-predict", json={
            "samples": []
        })
        assert response.status_code == 422  # Validation error
    
    def test_batch_prediction_wrong_features(self):
        """Test batch prediction with wrong feature count"""
        response = client.post("/batch-predict", json={
            "samples": [[5.1, 3.5, 1.4]]  # Only 3 features, needs 4
        })
        assert response.status_code == 422  # Validation error
    
    def test_root_endpoint(self):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "endpoints" in data
