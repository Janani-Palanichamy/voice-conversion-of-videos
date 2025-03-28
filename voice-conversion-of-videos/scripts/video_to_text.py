from flask import Flask, request, render_template, redirect, url_for
import os
import subprocess
import base64
import urllib.request
import json
def video_to_text():
    app = Flask(__name__)
    UPLOAD_FOLDER = "uploads"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    def extract_audio(video_path, audio_path="temp_audio.wav"):
        print("Extracting audio...")
        command = ["ffmpeg", "-i", video_path, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", audio_path]
        try:
            subprocess.run(command, check=True)
            print(f"Audio saved as {audio_path}")
            return audio_path
        except subprocess.CalledProcessError as e:
            print(f"Error extracting audio: {e}")
            exit(1)
    def audio_to_base64(audio_path):
        with open(audio_path, "rb") as f:
            audio_content = f.read()
        return base64.b64encode(audio_content).decode("utf-8")
    def speech_to_text(audio_base64):
        print("Transcribing audio...")
        GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"  # Replace with your API key
        url = f"https://speech.googleapis.com/v1p1beta1/speech:recognize?key={GOOGLE_API_KEY}"
        data = {
            "config": {
            "encoding": "LINEAR16",
            "languageCode": "en-US"
        },
        "audio": {
            "content": audio_base64
        }
    }
        request = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})
        response = urllib.request.urlopen(request)
        result = json.loads(response.read())
        transcript = result['results'][0]['alternatives'][0]['transcript']
        print("Transcription:", transcript)
        return transcript
    
    def translate_to_english(text, source_lang="auto"):
        print("Translating to English...")
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl=en&dt=t&q={text}"
        response = urllib.request.urlopen(url)
        translation = json.loads(response.read())[0][0][0]

    #print("Translation:", translation)
    #return translation
    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html", output="")
    @app.route("/upload", methods=["POST"])
    def upload():
        if "video" not in request.files:
            return redirect(request.url)
        video_file = request.files["video"]
        if video_file.filename == "":
            return redirect(request.url)
        video_path = os.path.join(app.config["UPLOAD_FOLDER"], video_file.filename)
        video_file.save(video_path)
        audio_file = extract_audio(video_path)
        audio_base64 = audio_to_base64(audio_file)
        transcript = speech_to_text(audio_base64)
        english_translation = translate_to_english(transcript)
        with open("scripts/english_translation.txt","w")as file:
            file.write(english_translation)
        print("saved successfully")

    

    if __name__ == "__main__":
        app.run(debug=True)
    #from text_to_speech import text_to_speech


 #return render_template("index.html", output=english_translation)