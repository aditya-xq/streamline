from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort
import os
import logging
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from download import download_youtube_audio

load_dotenv()  # Load environment variables from a .env file

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

DOWNLOAD_FOLDER = os.getenv('DOWNLOAD_FOLDER', './downloads')
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)
app.config['DOWNLOAD_FOLDER'] = os.path.abspath(DOWNLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        if video_url:
            try:
                file_path = download_youtube_audio(video_url, app.config['DOWNLOAD_FOLDER'])
                filename = os.path.basename(file_path)
                # safe_filename = secure_filename(filename)
                # logging.info(f"File to download: {filename}, after secure_filename: {safe_filename}")
                return redirect(url_for('download_file', filename=filename))
            except Exception as e:
                logging.error(f"Error downloading/converting video: {e}")
                error_message = "Failed to download and convert the video. Please try again later."
                return render_template('index.html', error=error_message)
    return render_template('index.html')

@app.route('/downloads/<filename>')
def download_file(filename):
    logging.info(f"Attempt to download file: {filename}")
    try:
        return send_from_directory(directory=app.config['DOWNLOAD_FOLDER'], path=filename, as_attachment=True)
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)  # Set to False for production use
