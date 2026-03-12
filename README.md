# Exp 1: ML Project Setup & Reproducibility

## Aim
Demonstrate that a complete ML project (data → train → model) is **reproducible** on:
- Local machine
- Google Colab
- Same code, no manual setup needed

## What You'll Learn
- Conda environment management
- Project structure best practices
- Model persistence (pickle)
- Reproducible ML workflows

## How to Reproduce (Local)

### Option A: One-command reproduction
```bash
./scripts/reproduce.sh
```

### Option B: Manual steps
```bash
# 1. Create conda environment
conda env create -f environment.yml

# 2. Activate
conda activate mlops-lab-exp1

# 3. Train model
cd src
python train.py

# 4. Evaluate
python evaluate.py
```

## Expected Output
```
[INFO] Loading Iris dataset...
[INFO] Dataset shape: (150, 4)
[INFO] Classes: 3
[INFO] Splitting data...
[INFO] Training Logistic Regression...
[RESULT] Train Accuracy: 1.0000
[RESULT] Test Accuracy: 1.0000
[SUCCESS] Model saved!
```

## Files
- `environment.yml` - Conda dependencies
- `src/train.py` - Training script
- `src/evaluate.py` - Evaluation script
- `src/config.py` - Configuration (paths, hyperparams)
- `scripts/reproduce.sh` - One-command reproduction
- `models/` - Saved models
- `data/` - Data directory (for future use)

## Next Steps
- Test in Google Colab (use `git clone` + run same commands)
- Add Exp 2 (CI/CD with GitHub Actions)