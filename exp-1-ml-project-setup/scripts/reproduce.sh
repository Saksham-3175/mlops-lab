#!/bin/bash
set -e

echo "=========================================="
echo "Exp 1: ML Project Setup & Reproducibility"
echo "=========================================="

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "[ERROR] Conda not found. Install Miniconda first."
    exit 1
fi

echo "[STEP 1] Creating conda environment..."
conda env create -f environment.yml --force -q
echo "[SUCCESS] Environment created: mlops-lab-exp1"

echo ""
echo "[STEP 2] Activating environment..."
source activate mlops-lab-exp1

echo ""
echo "[STEP 3] Running training..."
cd src
python train.py
cd ..

echo ""
echo "[STEP 4] Evaluating model..."
cd src
python evaluate.py
cd ..

echo ""
echo "=========================================="
echo "[SUCCESS] Exp 1 Complete!"
echo "Model saved at: models/iris_classifier.pkl"
echo "=========================================="