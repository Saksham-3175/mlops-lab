#!/bin/bash
set -e

echo "=========================================="
echo "Jenkins Setup for MLOps Lab"
echo "=========================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "[ERROR] Docker not found. Install Docker first."
    exit 1
fi

echo "[STEP 1] Checking Docker..."
docker --version

echo ""
echo "[STEP 2] Pulling Jenkins image..."
docker pull jenkins/jenkins:lts-jdk11

echo ""
echo "[STEP 3] Creating Jenkins container..."
docker run -d \
  --name mlops-jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp/jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts-jdk11

echo ""
echo "[STEP 4] Waiting for Jenkins to start (30s)..."
sleep 30

echo ""
echo "=========================================="
echo "[SUCCESS] Jenkins started!"
echo "=========================================="
echo ""
echo "Access Jenkins at: http://localhost:8080"
echo ""
echo "Get initial password:"
echo "  docker logs mlops-jenkins | grep 'Please use the following password'"
echo ""
echo "Stop Jenkins:"
echo "  docker stop mlops-jenkins"
echo ""
echo "Remove Jenkins:"
echo "  docker rm mlops-jenkins"
echo ""
echo "=========================================="