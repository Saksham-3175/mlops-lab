# Exp 2: CI/CD with GitHub Actions

## Aim
Automate ML training and testing on every push/PR using GitHub Actions.
- Trigger: git push
- Runs: tests + training + metrics logging
- Artifact: trained model + logs

## What You'll Learn
- GitHub Actions workflows (YAML)
- Pytest for ML code
- CI/CD best practices
- Automated model training in cloud

## How GitHub Actions Works

### Workflow Trigger
```
You push code → GitHub Actions detects → Runs ci.yml → Trains model + logs metrics
```

### Workflow File
See: `.github/workflows/ci.yml`

Steps:
1. Checkout code
2. Set up Python 3.10
3. Install dependencies
4. Run tests (pytest)
5. Train model
6. Upload artifacts (model + logs)

## Local Testing (Before pushing)

### Run tests locally
```bash
cd exp-2-github-actions-ci
pytest tests/ -v
```

### Run pipeline locally
```bash
cd exp-2-github-actions-ci
python src/pipeline.py
```

## What Happens on GitHub

1. Push to `main` or `develop` branch
2. GitHub Actions workflow starts automatically
3. All steps execute in Ubuntu environment
4. Results logged in GitHub UI
5. Model artifact stored for 7 days
6. Failed tests block PR merge (optional)

## Files
- `.github/workflows/ci.yml` - GitHub Actions workflow
- `src/pipeline.py` - ML training pipeline
- `src/config.py` - Configuration
- `tests/test_train.py` - Unit tests (pytest)
- `requirements.txt` - Python dependencies

## Expected CI Output
```
✓ Checkout code
✓ Set up Python
✓ Install dependencies
✓ Run tests (5/5 passed)
✓ Train model
  - Accuracy: 1.0000
  - Precision: 1.0000
  - Recall: 1.0000
  - F1: 1.0000
✓ Upload artifacts
✓ CI/CD Pipeline completed successfully
```

## Next Steps
1. Push this to GitHub
2. Check "Actions" tab in GitHub
3. Watch workflow run automatically
4. Download model from artifacts

## Debugging
- View workflow logs in GitHub Actions tab
- Check `.logs/training.log` in artifacts
- Failed test? Check test output in CI logs