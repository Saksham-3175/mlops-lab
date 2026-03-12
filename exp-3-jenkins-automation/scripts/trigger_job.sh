#!/bin/bash

# Manual trigger script for Jenkins job (requires curl)
# Usage: ./trigger_job.sh <jenkins-url> <job-name> <username> <token>

JENKINS_URL=${1:-"http://localhost:8080"}
JOB_NAME=${2:-"mlops-exp3-training"}
USERNAME=${3:-"admin"}
TOKEN=${4:-"your-api-token"}

echo "[INFO] Triggering Jenkins job: $JOB_NAME"
echo "[INFO] Jenkins URL: $JENKINS_URL"

curl -X POST \
  -u "$USERNAME:$TOKEN" \
  "$JENKINS_URL/job/$JOB_NAME/build"

echo ""
echo "[SUCCESS] Job triggered!"
echo "View progress at: $JENKINS_URL/job/$JOB_NAME"