# Exp 4: FastAPI for ML Inference

## Aim
Build production-grade ML inference API using FastAPI.
- Load trained model
- Serve predictions via REST API
- Input validation (Pydantic)
- Error handling & logging
- Compare FastAPI vs Flask performance

## What You'll Learn
- FastAPI basics (routing, validation, async)
- Pydantic schemas (request/response)
- Model serving best practices
- API testing and documentation
- Uvicorn server

## Prerequisites
- Trained model from Exp 1 (iris_classifier.pkl)
- FastAPI, Uvicorn installed

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Copy model from Exp 1
```bash
cp ../exp-1-ml-project-setup/models/iris_classifier.pkl models/
```

### 3. Start server
```bash
python src/main.py
# OR
uvicorn src.main:app --reload
```

Server runs at: http://localhost:8000

### 4. Test API
```bash
# Health check
curl http://localhost:8000/health

# Get model info
curl http://localhost:8000/model/info

# Make prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"feature1": 5.1, "feature2": 3.5, "feature3": 1.4, "feature4": 0.2}'
```

## API Endpoints

### GET /health
Health check endpoint
```json
Response: {"status": "ok", "timestamp": "2024-01-01T12:00:00"}
```

### GET /model/info
Model information
```json
Response: {
  "model_type": "LogisticRegression",
  "trained_on": "Iris dataset",
  "classes": [0, 1, 2],
  "n_features": 4
}
```

### POST /predict
Make prediction
```json
Request: {
  "feature1": 5.1,
  "feature2": 3.5,
  "feature3": 1.4,
  "feature4": 0.2
}

Response: {
  "prediction": 0,
  "confidence": 0.95,
  "class_name": "setosa"
}
```

### POST /batch-predict
Batch prediction
```json
Request: {
  "samples": [
    [5.1, 3.5, 1.4, 0.2],
    [7.0, 3.2, 4.7, 1.4]
  ]
}

Response: {
  "predictions": [0, 1],
  "confidence_scores": [0.95, 0.88]
}
```

## Auto-generated Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Files
- `src/main.py` - FastAPI application
- `src/config.py` - Configuration
- `src/model_loader.py` - Model loading & caching
- `src/schemas.py` - Pydantic request/response models
- `scripts/run_server.sh` - Start server
- `scripts/test_api.sh` - Test endpoints
- `requirements.txt` - Dependencies

## Testing

### Run unit tests
```bash
pytest tests/ -v
```

### Load testing (requires apache2-utils)
```bash
ab -n 100 -c 10 http://localhost:8000/health
```

## Next Steps
1. Start server locally
2. Test all endpoints
3. Move to Exp 5 (Dockerize)
4. Exp 9: Deploy to Heroku/Cloud