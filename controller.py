import os
import utils
from services import youtube, ffmpeg


def convert_to_video(audio_path, title):
    filename = "_converted_" + utils.sanitize_filename(title) + ".mp4"
    video_path = utils.get_temp_file_path(filename)
    image_path = os.path.join(os.path.dirname(__file__), "assets", "sound-only.jpg")
    ffmpeg.create_video_from_audio(audio_path, image_path, video_path)
    return video_path

def process_video(video_path, title, compress_video, upload_to_youtube):
    if compress_video:
        filename = utils.sanitize_filename(title) + ".mp4"
        compressed_path = utils.get_temp_file_path(filename)

        ffmpeg.compress_video(video_path, compressed_path)
        print(f"動画を圧縮しました: {compressed_path}")

    if upload_to_youtube:
        youtube.authenticate()
        print("アップロード中...")
        url = youtube.upload_video(compressed_path, title)
        message = utils.format_upload_message(title, url)
        print(message)

    utils.open_temp_dir()
