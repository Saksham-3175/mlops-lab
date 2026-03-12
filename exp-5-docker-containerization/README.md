# Exp 5: Containerize ML API with Docker

## Aim
Package FastAPI inference API into Docker container.
- Build Docker image
- Run locally with docker-compose
- Push to Docker Hub / Container Registry
- Test containerized API
- Enable Kubernetes-ready deployment (Exp 9)

## What You'll Learn
- Dockerfile best practices (multi-stage builds)
- Docker image optimization (layer caching, size)
- docker-compose for local development
- Container security and logging
- CI/CD integration for image builds

## Prerequisites
- Trained model from Exp 1 (iris_classifier.pkl)
- FastAPI code from Exp 4
- Docker installed

## Quick Start

### 1. Copy model to this directory
```bash
cp ../exp-1-ml-project-setup/models/iris_classifier.pkl models/
```

### 2. Build Docker image
```bash
./scripts/build.sh
```

### 3. Run container locally
```bash
./scripts/run.sh
```

### 4. Test API
```bash
./scripts/test_container.sh
```

### 5. Stop container
```bash
docker stop mlops-api
```

## Docker Image Builds

### Build image
```bash
docker build -f docker/Dockerfile -t mlops-inference:latest .
```

### Run container
```bash
docker run -d \
  --name mlops-api \
  -p 8000:8000 \
  -v $(pwd)/models:/app/models \
  mlops-inference:latest
```

### View logs
```bash
docker logs mlops-api -f
```

### Push to Docker Hub
```bash
# Tag image
docker tag mlops-inference:latest gg108/mlops-inference:latest

# Push
docker push gg108/mlops-inference:latest
```

## Using docker-compose

### Start all services
```bash
docker-compose -f docker/docker-compose.yml up -d
```

### View logs
```bash
docker-compose -f docker/docker-compose.yml logs -f api
```

### Stop services
```bash
docker-compose -f docker/docker-compose.yml down
```

## Container Testing

### Run tests inside container
```bash
docker run --rm \
  -v $(pwd)/models:/app/models \
  mlops-inference:latest \
  pytest tests/ -v
```

### Load testing
```bash
# Install apache2-utils
apt-get install apache2-utils

# 100 requests, 10 concurrent
ab -n 100 -c 10 http://localhost:8000/health
```

## Image Optimization

### Check image size
```bash
docker images mlops-inference
```

### View layers
```bash
docker history mlops-inference:latest
```

## Files
- `docker/Dockerfile` - Multi-stage Docker image
- `docker/docker-compose.yml` - Local compose setup
- `docker/.dockerignore` - Exclude files from build
- `scripts/build.sh` - Build image
- `scripts/run.sh` - Run container
- `scripts/test_container.sh` - Test API in container
- `models/` - Model directory (copy from Exp 1)

## Next Steps
1. Build and run container locally
2. Test all API endpoints
3. Push to Docker Hub (optional)
4. Exp 9: Deploy to Heroku/Cloud