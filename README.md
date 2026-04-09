# dle-solver

Automation scripts to solve multiple "-dle" guessing games using Selenium.

## Requirements

- macOS (tested)
- Python 3.10+
- Firefox installed
- geckodriver available at `/opt/homebrew/bin/geckodriver`

Install geckodriver (Homebrew example):

```bash
brew install geckodriver
```

## First-time setup

From the project root:

```bash
chmod +x start.sh load.sh
```

Both scripts will:

- create `myenv` if missing
- activate `myenv`
- install dependencies from `requirements.txt`

## Main workflows

### 1) Run solver

```bash
./start.sh
```

You will see a list of URL IDs and can input multiple IDs like:

```text
1 2 4
```

Behavior:

- valid IDs are used
- invalid IDs are ignored
- empty input runs all URLs
- before solving, it shows the last modified time of each database file

### 2) Refresh/load databases

```bash
./load.sh
```

You will see the same URL ID list and can choose which databases to refresh.

Behavior:

- valid IDs are loaded
- invalid IDs are ignored
- empty input loads all URLs

## Optional direct commands

Run solver directly:

```bash
python3 main.py 1 2
```

Refresh databases directly:

```bash
python3 load.py 1 2
```

Run all by omitting IDs:

```bash
python3 main.py
python3 load.py
```

## Troubleshooting

- If Selenium fails to start Firefox, verify geckodriver path in `utils.py`.
- If a database file is missing, run `./load.sh` first.
- If dependencies are missing, rerun `./start.sh` or `./load.sh` to reinstall requirements.
