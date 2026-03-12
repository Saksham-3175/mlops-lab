#!/bin/bash

echo "=========================================="
echo "Cleaning Docker Resources"
echo "=========================================="

CONTAINER_NAME="mlops-api"
IMAGE_NAME="mlops-inference"

echo "[STEP 1] Stopping container..."
if docker ps --format '{{.Names}}' | grep -q $CONTAINER_NAME; then
    docker stop $CONTAINER_NAME
    echo "[SUCCESS] Container stopped"
else
    echo "[INFO] Container not running"
fi

echo ""
echo "[STEP 2] Removing container..."
if docker ps -a --format '{{.Names}}' | grep -q $CONTAINER_NAME; then
    docker rm $CONTAINER_NAME
    echo "[SUCCESS] Container removed"
else
    echo "[INFO] Container doesn't exist"
fi

echo ""
echo "[STEP 3] Removing image..."
if docker images --format '{{.Repository}}' | grep -q $IMAGE_NAME; then
    docker rmi $IMAGE_NAME:latest
    echo "[SUCCESS] Image removed"
else
    echo "[INFO] Image doesn't exist"
fi

echo ""
echo "=========================================="
echo "[SUCCESS] Cleanup complete!"
echo "=========================================="