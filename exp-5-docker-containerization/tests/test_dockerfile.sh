#!/bin/bash
set -e

echo "=========================================="
echo "Testing Dockerfile Build"
echo "=========================================="

IMAGE_NAME="mlops-inference:test"

echo "[STEP 1] Building image..."
docker build -f docker/Dockerfile -t $IMAGE_NAME .

echo ""
echo "[STEP 2] Running container for testing..."
CONTAINER_ID=$(docker run -d \
    -v "$(pwd)/models:/app/models" \
    $IMAGE_NAME \
    sleep 60)

echo "Container ID: $CONTAINER_ID"

echo ""
echo "[STEP 3] Testing imports..."
docker exec $CONTAINER_ID python -c "
import sys
print(f'Python: {sys.version}')
from fastapi import FastAPI
print('✓ FastAPI imported')
from sklearn.linear_model import LogisticRegression
print('✓ scikit-learn imported')
import numpy
print('✓ NumPy imported')
"

echo ""
echo "[STEP 4] Checking model file..."
docker exec $CONTAINER_ID ls -lh /app/models/

echo ""
echo "[STEP 5] Cleaning up..."
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID
docker rmi $IMAGE_NAME

echo ""
echo "=========================================="
echo "[SUCCESS] Dockerfile tests passed!"
echo "=========================================="