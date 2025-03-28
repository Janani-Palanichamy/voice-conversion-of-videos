
import os
from pydub import AudioSegment
import librosa
import soundfile as sf
import scripts.config as config
import subprocess


def convert_audio_format(input_file, output_file, format="wav"):
    """ Convert audio to a different format (e.g., MP3 to WAV) """
    audio = AudioSegment.from_file(input_file)
    output_path = os.path.join(config.OUTPUT_AUDIO_PATH, output_file)
    audio.export(output_path, format=format)
    return f"Converted {input_file} to {format} and saved at {output_path}"

def change_audio_speed(input_file, output_file, speed_factor=config.DEFAULT_SPEED_FACTOR):
    """ Change the speed of the audio file """
    y, sr = librosa.load(input_file)
    y_fast = librosa.effects.time_stretch(y, speed_factor)
    output_path = os.path.join(config.OUTPUT_AUDIO_PATH, output_file)
    sf.write(output_path, y_fast, sr)
    return f"Speed changed for {input_file} and saved at {output_path}"

def change_audio_volume(input_file, output_file, db_change=config.DEFAULT_VOLUME_CHANGE):
    """ Increase or decrease the volume of the audio """
    audio = AudioSegment.from_file(input_file)
    audio = audio + db_change  # Increase volume by `db_change` dB
    output_path = os.path.join(config.OUTPUT_AUDIO_PATH, output_file)
    audio.export(output_path, format="wav")
    return f"Volume changed for {input_file} and saved at {output_path}"
