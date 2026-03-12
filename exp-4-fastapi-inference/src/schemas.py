from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime

class PredictionRequest(BaseModel):
    """Single prediction request"""
    feature1: float = Field(..., ge=0, le=10, description="Sepal length")
    feature2: float = Field(..., ge=0, le=10, description="Sepal width")
    feature3: float = Field(..., ge=0, le=10, description="Petal length")
    feature4: float = Field(..., ge=0, le=10, description="Petal width")
    
    class Config:
        schema_extra = {
            "example": {
                "feature1": 5.1,
                "feature2": 3.5,
                "feature3": 1.4,
                "feature4": 0.2
            }
        }

class PredictionResponse(BaseModel):
    """Single prediction response"""
    prediction: int
    confidence: float = Field(..., ge=0, le=1)
    class_name: str
    timestamp: datetime

class BatchPredictionRequest(BaseModel):
    """Batch prediction request"""
    samples: List[List[float]] = Field(..., description="List of feature arrays")
    
    @validator('samples')
    def validate_samples(cls, v):
        if not v:
            raise ValueError("samples cannot be empty")
        if any(len(sample) != 4 for sample in v):
            raise ValueError("Each sample must have 4 features")
        return v

class BatchPredictionResponse(BaseModel):
    """Batch prediction response"""
    predictions: List[int]
    confidence_scores: List[float]
    count: int

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    timestamp: datetime

class ModelInfoResponse(BaseModel):
    """Model information response"""
    model_type: str
    trained_on: str
    classes: List[int]
    n_features: int
    model_path: str