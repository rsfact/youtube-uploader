# YouTube Uploader

```bash
choco install -y ffmpeg
```

```bash
python -m venv .venv
source .venv/Script/activate
pip install -r requirements.txt
```

RSfactのGoogle Cloud Console内、YouTubeUploaderプロジェクトから、認証情報シークレットをダウンロードし、`secrets/client_secret.json` として配置する。

```bash
python main.py sample/sample.mp4
```

`run.sh`のショートカットをデスクトップに置くと便利。
