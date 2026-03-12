#!/bin/bash
set -e

echo "=========================================="
echo "Building Docker Image for ML API"
echo "=========================================="

# Check if model exists
if [ ! -f "models/iris_classifier.pkl" ]; then
    echo "[ERROR] Model not found at models/iris_classifier.pkl"
    echo "[INFO] Copy model from Exp 1:"
    echo "      cp ../exp-1-ml-project-setup/models/iris_classifier.pkl models/"
    exit 1
fi

echo "[SUCCESS] Model found!"
echo ""

IMAGE_NAME="mlops-inference"
IMAGE_TAG="latest"
FULL_IMAGE="$IMAGE_NAME:$IMAGE_TAG"

echo "[STEP 1] Building image: $FULL_IMAGE"
docker build -f docker/Dockerfile -t $FULL_IMAGE .

echo ""
echo "[STEP 2] Image created successfully!"
docker images $IMAGE_NAME

echo ""
echo "[STEP 3] Image history (layers):"
docker history $FULL_IMAGE

echo ""
echo "=========================================="
echo "[SUCCESS] Build complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "  Run container:  ./scripts/run.sh"
echo "  Test API:       ./scripts/test_container.sh"
echo "  Push to Hub:    docker push gg108/$FULL_IMAGE"
echo ""