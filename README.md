# YouTube Uploader

動画・音声ファイルを圧縮してYouTubeに自動アップロードするツールです。

## 機能

- ffmpegで動画を圧縮（settings.pyで圧縮率設定可能）
- YouTubeに限定公開設定で動画を自動アップロード
- 音声ファイル（mp3, wav, aac）を動画に変換してアップロード
- ファイル名とタイトルの管理
- アップロード完了時のテンプレートメッセージ表示
- 前回実行時のファイルは次回実行時にクリーンアップ
- YouTubeにアップロードしない場合はtempディレクトリを自動で開く
- コマンドライン引数でファイルパス指定可能

## 環境構築

### 1. 必要なソフトウェアのインストール

#### Python
Python 3.7以上が必要です。

#### ffmpeg
動画・音声処理にffmpegが必要です。

**Windows:**
```bash
# Chocolateyを使用する場合
choco install ffmpeg

# または公式サイトからダウンロード
# https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 2. Pythonパッケージのインストール

```bash
pip install -r requirements.txt
```

### 3. Google Cloud Console設定

1. [Google Cloud Console](https://console.cloud.google.com/)にアクセス
2. 新しいプロジェクトを作成または既存のプロジェクトを選択
3. YouTube Data API v3を有効化
4. 認証情報を作成：
   - 「認証情報を作成」→「OAuth 2.0 クライアント ID」
   - アプリケーションの種類：「デスクトップアプリケーション」
   - 名前：任意（例：YouTube Uploader）
5. 作成されたクライアント IDのJSONファイルをダウンロード
6. ダウンロードしたファイルを `secrets/client_secret.json` として配置

### 4. ディレクトリ構造

```
youtube-uploader/
├── main.py
├── controller.py
├── utils.py
├── settings.py
├── requirements.txt
├── README.md
├── .gitignore
├── assets/
│   └── sound-only.jpg
├── secrets/
│   └── client_secret.json  # 手動で配置
├── services/
│   ├── ffmpeg.py
│   └── youtube.py
├── templates/
│   └── uploaded.txt
└── temp/  # 自動作成される
```

## 設定

### settings.py
動画圧縮の設定を変更できます：

```python
# 動画圧縮設定
VIDEO_CRF = 23  # 0-51の範囲、低いほど高品質（18-28が推奨）
AUDIO_BITRATE = "128k"  # 音声ビットレート

# 動画エンコーダー設定
VIDEO_CODEC = "libx264"
AUDIO_CODEC = "aac"
```

## 使用方法

### 基本的な使用方法
```bash
python main.py
```

### ファイルパスを引数で指定
```bash
python main.py "path/to/video.mp4"
```

### 実行手順
1. ファイルパスを入力（引数で指定していない場合）
2. タイトルを入力
3. YouTubeアップロードの可否を選択（y/n）

## 処理フロー

1. **音声ファイルの場合**：
   - `assets/sound-only.jpg`と音声を合成して動画を作成
   - 動画を圧縮
   - YouTubeにアップロード（選択した場合）

2. **動画ファイルの場合**：
   - 動画を圧縮
   - YouTubeにアップロード（選択した場合）

## 注意事項

- 初回YouTube認証時はブラウザが開きます
- 認証情報は `secrets/token.pickle` に保存されます
- 前回実行時の一時ファイルは次回実行時に自動削除されます
- アップロードされた動画は限定公開設定になります
- YouTubeにアップロードしない場合、tempディレクトリが自動で開きます
- 圧縮設定は `settings.py` で変更可能です
