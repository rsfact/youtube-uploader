#!/bin/bash

# 現在のディレクトリを取得
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 仮想環境をアクティベート
source .venv/Scripts/activate

# main.pyを実行（引数があれば渡す）
if [ $# -gt 0 ]; then
    python main.py "$@"
else
    python main.py
fi

# 実行後にターミナルを開いたままにする
read -p "処理が完了しました。Enterキーを押して終了してください..."
