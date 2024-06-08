## About

Animal Sudoku App

## Docker

- docker is required

### Deploy

```bash
# Please set the .env file before executing it.
docker compose up -d
```

### Build

```bash
# Please change the username and tag correctly.
docker build -t takanarishimbo/animal-sudoku-app:v1.0.0 .
```

## Conda

- conda or miniconda is required

### Venv

- create venv

```bash
conda create -n animal_sudoku_app python=3.10
```

- activate venv

```bash
conda activate animal_sudoku_app
```

- install libs

```bash
# Please activate venv before executing it.
pip install -r requirements.txt
```

### Deploy

```bash
# Please activate venv before executing it.
streamlit run server.py
```

## ToDo

- Add Introduce Page
- Add Chenge Table
