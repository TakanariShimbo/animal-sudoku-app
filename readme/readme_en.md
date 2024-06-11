README | [English](/readme/readme_en.md) | [日本語](/readme/readme_jp.md)

## 🐧About

This is repository of "Animal Sudoku App"

![About WebSite](/images/about_animal_sudoku_app_en.png)

Click or scan the bellow QR-Code to access web site

[![QR-Code of WebSite](/images/qr_code_animal_sudoku_app.png)](https://animal-sudoku-app.streamlit.app/)

## 🐋Docker

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

## 🐍Conda

- conda or miniconda is required

### Deploy

```bash
# Please activate venv before executing it.
streamlit run server.py
```

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
