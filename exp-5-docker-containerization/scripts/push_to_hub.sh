#!/bin/bash
set -e

echo "=========================================="
echo "Pushing Image to Docker Hub"
echo "=========================================="

if [ -z "$1" ]; then
    echo "[ERROR] Usage: ./push_to_hub.sh <docker-username>"
    exit 1
fi

USERNAME=$1
IMAGE_NAME="mlops-inference"
IMAGE_TAG="latest"
LOCAL_IMAGE="$IMAGE_NAME:$IMAGE_TAG"
REMOTE_IMAGE="$USERNAME/$IMAGE_NAME:$IMAGE_TAG"

echo "[STEP 1] Checking Docker login..."
if ! docker info | grep -q "Username:"; then
    echo "[INFO] Not logged in. Logging in to Docker Hub..."
    docker login
fi

echo ""
echo "[STEP 2] Tagging image..."
docker tag $LOCAL_IMAGE $REMOTE_IMAGE

echo ""
echo "[STEP 3] Pushing to Docker Hub..."
docker push $REMOTE_IMAGE

echo ""
echo "=========================================="
echo "[SUCCESS] Image pushed!"
echo "=========================================="
echo ""
echo "Image: $REMOTE_IMAGE"
echo "Pull with: docker pull $REMOTE_IMAGE"
echo ""