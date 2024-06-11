README | [English](/readme/readme_en.md) | [日本語](/readme/readme_jp.md)

## 🐧 概要

これは「Animal Sudoku App」のリポジトリです。

![About WebSite](/images/about_animal_sudoku_app_jp.png)

以下の QR コードをクリックまたはスキャンして、ウェブサイトにアクセスしてください。

[![QR-Code of WebSite](/images/qr_code_animal_sudoku_app.png)](https://animal-sudoku-app.streamlit.app/)

## 🐋Docker

- 前提：Docker がインストール済み

### デプロイ

```bash
# 実行前に.envファイルを設定してください。
docker compose up -d
```

### ビルド

```bash
# ユーザー名とタグを正しく変更してください。
docker build -t takanarishimbo/animal-sudoku-app:v1.0.0 .
```

## 🐍Conda

- 前提：Anaconda or Miniconda がインストール済み

### デプロイ

```bash
# 実行前にvenvを有効化してください。
streamlit run server.py
```

### Venv

- 仮想環境の作成

```bash
conda create -n animal_sudoku_app python=3.10
```

- 仮想環境の有効化

```bash
conda activate animal_sudoku_app
```

- ライブラリのインストール

```bash
# 実行前にvenvを有効化してください。
pip install -r requirements.txt
```
