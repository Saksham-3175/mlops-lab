import logging
from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

from config import HOST, PORT, DEBUG, CLASS_NAMES
from schemas import (
    PredictionRequest, PredictionResponse,
    BatchPredictionRequest, BatchPredictionResponse,
    HealthResponse, ModelInfoResponse
)
from model_loader import model_loader

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(name)s - %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI(
    title="MLOps ML Inference API",
    description="Production-grade ML inference API for Iris classification",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    """Load model on startup"""
    logger.info("[STARTUP] Initializing API...")
    try:
        model_loader.load_model()
        logger.info("[STARTUP] Model loaded successfully")
    except Exception as e:
        logger.error(f"[STARTUP] Failed to initialize: {str(e)}")
        raise

@app.get("/health", response_model=HealthResponse, status_code=200)
async def health_check():
    """Health check endpoint"""
    logger.info("[HEALTH] Health check requested")
    return HealthResponse(
        status="ok",
        timestamp=datetime.now()
    )

@app.get("/model/info", response_model=ModelInfoResponse, status_code=200)
async def model_info():
    """Get model information"""
    logger.info("[INFO] Model info requested")
    try:
        info = model_loader.get_model_info()
        return ModelInfoResponse(**info)
    except Exception as e:
        logger.error(f"[ERROR] Failed to get model info: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve model information"
        )

@app.post("/predict", response_model=PredictionResponse, status_code=200)
async def predict(request: PredictionRequest):
    """Make single prediction"""
    logger.info(f"[PREDICT] Prediction requested")
    
    try:
        model = model_loader.get_model()
        
        # Prepare features
        features = np.array([[
            request.feature1,
            request.feature2,
            request.feature3,
            request.feature4
        ]])
        
        # Predict
        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]
        confidence = float(np.max(probabilities))
        class_name = CLASS_NAMES.get(prediction, "unknown")
        
        logger.info(f"[PREDICT] Prediction: {class_name} (confidence: {confidence:.4f})")
        
        return PredictionResponse(
            prediction=int(prediction),
            confidence=confidence,
            class_name=class_name,
            timestamp=datetime.now()
        )
    
    except Exception as e:
        logger.error(f"[ERROR] Prediction failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Prediction failed"
        )

@app.post("/batch-predict", response_model=BatchPredictionResponse, status_code=200)
async def batch_predict(request: BatchPredictionRequest):
    """Make batch predictions"""
    logger.info(f"[BATCH] Batch prediction requested ({len(request.samples)} samples)")
    
    try:
        model = model_loader.get_model()
        
        # Convert to numpy array
        features = np.array(request.samples)
        
        # Predict
        predictions = model.predict(features)
        probabilities = model.predict_proba(features)
        confidence_scores = [float(np.max(probs)) for probs in probabilities]
        
        logger.info(f"[BATCH] Batch prediction complete ({len(predictions)} samples)")
        
        return BatchPredictionResponse(
            predictions=predictions.tolist(),
            confidence_scores=confidence_scores,
            count=len(predictions)
        )
    
    except Exception as e:
        logger.error(f"[ERROR] Batch prediction failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Batch prediction failed"
        )

@app.get("/", status_code=200)
async def root():
    """Root endpoint"""
    return {
        "message": "MLOps ML Inference API",
        "docs": "/docs",
        "health": "/health",
        "model_info": "/model/info",
        "endpoints": {
            "predict": "POST /predict",
            "batch_predict": "POST /batch-predict"
        }
    }

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.error(f"[ERROR] Unhandled exception: {str(exc)}", exc_info=True)
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Internal server error"
    )

if __name__ == "__main__":
    import uvicorn
    logger.info(f"[START] Starting server on {HOST}:{PORT}")
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=DEBUG,
        workers=1 if DEBUG else 4,
        log_level="info"
    )