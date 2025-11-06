Smishing Attack Detection (SMS Phishing)

Overview
This project detects smishing (SMS phishing) using machine learning. It includes dataset download, preprocessing, a baseline model (TF-IDF + Logistic Regression), and simple inference.

Project layout
```
smishing_attack_detection/
├─ data/
│  ├─ raw/            # downloaded datasets
│  └─ processed/      # cleaned/split datasets
├─ models/            # saved models and vectorizers
├─ notebooks/         # exploratory notebooks
├─ scripts/           # CLI scripts (download/train/infer)
├─ src/               # reusable modules
├─ logs/              # logs
├─ requirements.txt
└─ README.md
```

Quickstart (Windows PowerShell)
1) Create and activate venv
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

3) Download dataset (Hugging Face MOZ-Smishing)
```
python scripts/download_dataset.py --dataset MOZNLP/MOZ-Smishing --split test --out data/raw/moz_smishing.csv
```

4) Train baseline model
```
python scripts/train.py --input data/raw/moz_smishing.csv --text-col text --label-col label
```

5) Run inference
```
python scripts/infer.py --text "Parabéns! Você ganhou um prêmio. Clique no link."
```

Notes
- The default dataset is `MOZNLP/MOZ-Smishing` (Portuguese). You can swap datasets if you have another CSV with `--text-col` and `--label-col`.
- Models are saved under `models/`.


