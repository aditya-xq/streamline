import os
import logging
from pytube import YouTube
from moviepy.editor import AudioFileClip
from pytube.exceptions import PytubeError

def download_youtube_audio(video_url, output_path="./", delete_original=True):
    try:
        logging.info("Starting download...")
        video = YouTube(video_url, on_progress_callback=progress_callback)
        audio = video.streams.get_audio_only()
        if not audio:
            logging.error("No audio stream found")
            raise ValueError("No audio stream found")

        download_path = audio.download(output_path=output_path)
        logging.info("Converting to MP3...")
        base_name = os.path.splitext(os.path.basename(download_path))[0]
        base_name = base_name.replace(' ', '_')
        mp3_file = os.path.join(output_path, f"{base_name}.mp3")

        with AudioFileClip(download_path) as video_clip:
            video_clip.write_audiofile(mp3_file, logger='bar')

        if delete_original and os.path.exists(download_path):
            os.remove(download_path)

        logging.info(f"Audio downloaded and converted to MP3 successfully: {mp3_file}")
        return mp3_file
    except (PytubeError, ValueError, Exception) as e:
        logging.error(f"Error in download or conversion process: {e}")
        raise

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    logging.info(f"Download progress: {percentage_of_completion:.2f}%")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("YouTube Audio Downloader")
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_audio(video_url)
