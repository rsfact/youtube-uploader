import subprocess
import settings

def compress_video(input_path, output_path):
    cmd = [
        'ffmpeg', '-i', input_path,
        '-c:v', 'libx264', '-crf', str(settings.VIDEO_CRF),
        '-c:a', 'aac', '-b:a', settings.AUDIO_BITRATE,
        '-y', output_path
    ]
    subprocess.run(cmd, check=True)

def create_video_from_audio(audio_path, image_path, output_path):
    cmd = [
        'ffmpeg', '-loop', '1', '-i', image_path,
        '-i', audio_path,
        '-c:v', 'libx264', '-c:a', 'aac',
        '-shortest', '-y', output_path
    ]
    subprocess.run(cmd, check=True)
