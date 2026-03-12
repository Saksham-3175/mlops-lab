#!/bin/bash
set -e

echo "=========================================="
echo "Running ML API Container"
echo "=========================================="

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "[ERROR] Docker daemon not running"
    exit 1
fi

CONTAINER_NAME="mlops-api"
IMAGE_NAME="mlops-inference:latest"
PORT="8000"

echo "[STEP 1] Checking if container already running..."
if docker ps --format '{{.Names}}' | grep -q $CONTAINER_NAME; then
    echo "[INFO] Container $CONTAINER_NAME already running"
    docker stop $CONTAINER_NAME
fi

echo "[STEP 2] Starting container..."
docker run -d \
    --name $CONTAINER_NAME \
    -p $PORT:$PORT \
    -v "$(pwd)/models:/app/models" \
    -v "$(pwd)/logs:/app/logs" \
    -e API_HOST=0.0.0.0 \
    -e API_PORT=$PORT \
    -e LOG_LEVEL=INFO \
    --restart unless-stopped \
    $IMAGE_NAME

echo "[SUCCESS] Container started: $CONTAINER_NAME"
echo ""

# Wait for container to be ready
echo "[STEP 3] Waiting for API to be ready (10s)..."
sleep 10

echo ""
echo "=========================================="
echo "[SUCCESS] ML API running!"
echo "=========================================="
echo ""
echo "Access points:"
echo "  API:           http://localhost:$PORT"
echo "  Swagger UI:    http://localhost:$PORT/docs"
echo "  ReDoc:         http://localhost:$PORT/redoc"
echo "  Health:        http://localhost:$PORT/health"
echo ""
echo "Commands:"
echo "  View logs:     docker logs $CONTAINER_NAME -f"
echo "  Stop:          docker stop $CONTAINER_NAME"
echo "  Remove:        docker rm $CONTAINER_NAME"
echo ""