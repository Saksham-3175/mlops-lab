#!/bin/bash

echo "=========================================="
echo "Starting FastAPI ML Inference Server"
echo "=========================================="

# Check if model exists
if [ ! -f "models/iris_classifier.pkl" ]; then
    echo "[ERROR] Model not found at models/iris_classifier.pkl"
    echo "[INFO] Copy model from Exp 1:"
    echo "      cp ../exp-1-ml-project-setup/models/iris_classifier.pkl models/"
    exit 1
fi

echo "[INFO] Model found!"
echo ""

# Install dependencies
echo "[STEP] Installing dependencies..."
pip install -r src/requirements.txt -q

echo ""
echo "[STEP] Starting server..."
cd src
python main.py

echo ""
echo "=========================================="
echo "Server running at: http://localhost:8000"
echo "Documentation: http://localhost:8000/docs"
echo "=========================================="