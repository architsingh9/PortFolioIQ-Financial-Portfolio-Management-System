# Datasets

This project keeps **all CSVs in the repo** under `data/`.

## Layout conventions
- Time-partitioned snapshots  
  `data/holdings/<YYYY>/<MM>/<filename>.csv`  
  e.g. `data/holdings/2024/02/holdings_2024-02-01.csv`
- Reference lookups  
  `data/reference/*.csv`
- Add more subfolders under `data/` as needed (prices, trades, etc.).

## Required columns for holdings CSV
`portfolio_code, symbol, quantity, price, asof`  
- `asof` should be ISO date (e.g., `2024-02-01`).

## ADF usage (GitHub → ADLS or Synapse staging)
Use the pipeline parameters:
- `repo_owner`: `architsingh9`
- `repo_name`: `PortFolioIQ-Financial-Portfolio-Management-System`
- `branch`: `main`
- `file_path`: path under this repo, e.g.  
  `data/holdings/2024/02/holdings_2024-02-01.csv`

### ADLS sink (suggested)
- Container: `raw`
- Folder: `portfolioiq/holdings/<yyyy>/<MM>`
- File: `holdings_<yyyy-MM-dd>.csv`

## Local development (no Azure required)
1) Create a virtual env and install:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   pip install -e .

