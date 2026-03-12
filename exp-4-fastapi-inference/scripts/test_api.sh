#!/bin/bash

BASE_URL="http://localhost:8000"

echo "=========================================="
echo "Testing FastAPI ML Inference API"
echo "=========================================="

echo ""
echo "[TEST 1] Health check"
curl -s -X GET "$BASE_URL/health" | python -m json.tool

echo ""
echo "[TEST 2] Model info"
curl -s -X GET "$BASE_URL/model/info" | python -m json.tool

echo ""
echo "[TEST 3] Single prediction"
curl -s -X POST "$BASE_URL/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "feature1": 5.1,
    "feature2": 3.5,
    "feature3": 1.4,
    "feature4": 0.2
  }' | python -m json.tool

echo ""
echo "[TEST 4] Batch prediction"
curl -s -X POST "$BASE_URL/batch-predict" \
  -H "Content-Type: application/json" \
  -d '{
    "samples": [
      [5.1, 3.5, 1.4, 0.2],
      [7.0, 3.2, 4.7, 1.4],
      [6.3, 3.3, 6.0, 2.5]
    ]
  }' | python -m json.tool

echo ""
echo "[TEST 5] Invalid input (should fail)"
curl -s -X POST "$BASE_URL/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "feature1": "invalid",
    "feature2": 3.5,
    "feature3": 1.4,
    "feature4": 0.2
  }' | python -m json.tool

echo ""
echo "=========================================="
echo "Tests complete!"
echo "=========================================="