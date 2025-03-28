import os
from pydub import AudioSegment


from flask import Flask, render_template, request

from scripts.audio_processing import convert_audio_format
  # Import your processing function
os.environ["FFMPEG_BINARY"]=r"C:\Program Files\ffmpeg-7.1.1-essentials_build\bin"
from pydub.utils import which
print(which("ffmpeg"))


app = Flask(__name__)

UPLOAD_FOLDER = r"C:\Users\janan\OneDrive\Desktop\vs code projects\uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")  # Load the HTML page

@app.route("/upload", methods=["POST"])
def upload_audio():
    if "audio_file" not in request.files:
        return "No file uploaded"

    audio_file = request.files["audio_file"]
    if audio_file.filename == "":
        return "No selected file" # If file input is empty
    
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], audio_file.filename)
    audio_file.save(file_path)
    converted_path=file_path.rsplit(".",1)[0]+".wav"
    convert_audio_format(file_path,converted_path)
    return f"File uploaded successfully:{file_path}"
    
    
    


if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app
