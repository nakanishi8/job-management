# streamlit-job-manager

Streamlitを使用した長時間処理対応のジョブ管理システム

## 概要

このアプリケーションは、長時間実行されるジョブを非同期で実行し、その進捗とステータスを管理するWebシステムです。

### 主な機能

- **ジョブ実行**: 入力値を設定してジョブを非同期実行
- **ジョブ一覧**: 全ジョブのステータスを一覧表示
- **結果表示**: 完了したジョブの入出力を確認

## 必要環境

- Python 3.13以上
- [UV](https://docs.astral.sh/uv/) パッケージマネージャ

## セットアップ

```bash
# 依存関係のインストール
uv sync --all-groups
```

## 起動方法

```bash
streamlit run src/job_management/main.py
```

ブラウザで http://localhost:8501 にアクセス

## 使い方

1. **ジョブ実行ページ**で値`a`と`b`を入力し、保存名を設定して「実行」ボタンをクリック
2. **ジョブ一覧ページ**でジョブのステータス（RUNNING/COMPLETED/FAILED）を確認
3. **結果ページ**で完了したジョブの入力データと計算結果を確認

## 開発

```bash
# リンター・フォーマッター実行
ruff check . --fix
ruff format .

# テスト実行
pytest

# カバレッジ付きテスト
pytest --cov=src/job_management
```

## アーキテクチャ

```
src/
└── job_management/
    ├── main.py              # エントリーポイント（Streamlitナビゲーション）
    ├── db.py                # データベース層（SQLAlchemy + SQLite）
    ├── job.py               # ジョブ実行オーケストレーション
    ├── problem.py           # ドメインロジック（Pydanticモデル）
    ├── outputs/             # ジョブ出力ディレクトリ（SQLite DB + JSONファイル）
    │   └── {job_id}/       # ジョブごとの出力（input.json, output.json）
    └── pages/               # StreamlitのUIページ
        ├── job_execution.py # ジョブ作成フォーム
        ├── job_list.py      # ジョブ一覧テーブル
        └── result.py        # ジョブ結果表示
```

### データフロー

1. ユーザーが入力値を送信
2. `execute_job()`がマルチプロセスで実行
3. ジョブステータス: RUNNING → COMPLETED/FAILED
4. 入出力データは`src/job_management/outputs/{job_id}/`に保存

## ライセンス

MIT
