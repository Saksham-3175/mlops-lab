# Exp 3: Jenkins for Local Automation

## Aim
Automate ML training job using Jenkins locally.
- Trigger: Manual job or scheduled (cron)
- Runs: Training pipeline with logging
- Output: Model + logs + Jenkins artifacts

## What You'll Learn
- Jenkins installation & setup (local)
- Jenkinsfile (declarative pipeline)
- Trigger training jobs programmatically
- Job logs and artifact management

## How Jenkins Works

### Local Jenkins Setup
1. Install Jenkins
2. Create job from Jenkinsfile
3. Trigger job manually or on schedule
4. View logs in Jenkins UI
5. Download artifacts (model + logs)

## Prerequisites
- Docker (for Jenkins container) OR Java + Jenkins binary
- 8GB RAM minimum

## Setup Options

### Option A: Docker (Recommended)
```bash
./scripts/jenkins_setup.sh
```

### Option B: Manual Install
1. Install Java 11+
2. Download Jenkins WAR
3. Run: `java -jar jenkins.war`
4. Access: http://localhost:8080

## Local Setup Steps

### 1. Start Jenkins
```bash
./scripts/jenkins_setup.sh
```

Jenkins runs at: http://localhost:8080

### 2. Get Initial Admin Password
```bash
docker logs jenkins
# Look for: "Please use the following password to proceed to installation:"
```

### 3. Create Job
- Go to Jenkins UI
- New Item → Pipeline
- Name: `mlops-exp3-training`
- Pipeline → Definition: Pipeline script from SCM
- SCM: Git
- Repository URL: `https://github.com/Saksham-3175/mlops-lab.git`
- Script Path: `exp-3-jenkins-automation/Jenkinsfile`
- Save

### 4. Run Job
- Click "Build Now"
- View logs in real-time
- Download artifacts

## Files
- `Jenkinsfile` - Pipeline definition
- `src/train.py` - Training script
- `src/config.py` - Configuration
- `scripts/jenkins_setup.sh` - Jenkins setup script
- `scripts/trigger_job.sh` - Trigger job from CLI

## Expected Output
```
[INFO] Starting ML Training Job
[INFO] Loading data...
[INFO] Training model...
[RESULT] Accuracy: 0.95
[INFO] Model saved
[SUCCESS] Job completed
```

## Next Steps
1. Run `./scripts/jenkins_setup.sh`
2. Access Jenkins UI
3. Create job and run
4. Move to Exp 4 (FastAPI inference)