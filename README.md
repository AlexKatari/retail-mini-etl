# Retail Mini ETL

A small beginner-friendly Python project that transforms sample retail sales data.

## Run the project

From the repository root, run these commands in PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/etl.py
python -m pytest
```

The script writes the processed sample data to `data/processed/clean_sales.csv`.