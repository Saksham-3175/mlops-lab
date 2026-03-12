#!/bin/bash

echo "=========================================="
echo "Testing Containerized ML API"
echo "=========================================="

BASE_URL="http://localhost:8000"
CONTAINER_NAME="mlops-api"

# Check if container is running
if ! docker ps --format '{{.Names}}' | grep -q $CONTAINER_NAME; then
    echo "[ERROR] Container $CONTAINER_NAME not running"
    echo "[INFO] Start container with: ./scripts/run.sh"
    exit 1
fi

echo "[STEP 1] Health check"
curl -s -X GET "$BASE_URL/health" | python3 -m json.tool
echo ""

echo "[STEP 2] Model info"
curl -s -X GET "$BASE_URL/model/info" | python3 -m json.tool
echo ""

echo "[STEP 3] Single prediction"
curl -s -X POST "$BASE_URL/predict" \
    -H "Content-Type: application/json" \
    -d '{
        "feature1": 5.1,
        "feature2": 3.5,
        "feature3": 1.4,
        "feature4": 0.2
    }' | python3 -m json.tool
echo ""

echo "[STEP 4] Batch prediction"
curl -s -X POST "$BASE_URL/batch-predict" \
    -H "Content-Type: application/json" \
    -d '{
        "samples": [
            [5.1, 3.5, 1.4, 0.2],
            [7.0, 3.2, 4.7, 1.4],
            [6.3, 3.3, 6.0, 2.5]
        ]
    }' | python3 -m json.tool
echo ""

echo "=========================================="
echo "[SUCCESS] Container tests complete!"
echo "=========================================="
echo ""
echo "Container logs:"
docker logs $CONTAINER_NAME --tail 20