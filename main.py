import controller
import utils
import os
import sys

def main(file_path, title, compress_video, upload_to_youtube):
    utils.cleanup_temp_dir()

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension in [".mp3", ".wav", ".aac"]:
        video_path = controller.convert_to_video(file_path, title)
        controller.process_video(video_path, title, compress_video, upload_to_youtube)
    elif file_extension in [".mp4", ".mkv"]:
        controller.process_video(file_path, title, compress_video, upload_to_youtube)
    else:
        print("サポートされていないファイル形式です")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("ファイルパスを入力してください: ")

    title = input("タイトルを入力してください: ")
    compress_video = input("動画を圧縮しますか？ (y/n): ").lower() == "y"
    upload_to_youtube = input("YouTubeにアップロードしますか？ (y/n): ").lower() == "y"

    main(file_path, title, compress_video, upload_to_youtube)
