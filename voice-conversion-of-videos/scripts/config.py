import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),",")))


# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for input and output audio files
INPUT_AUDIO_PATH = os.path.join(BASE_DIR, "input_audio")
OUTPUT_AUDIO_PATH = os.path.join(BASE_DIR, "output_audio")

# Ensure directories exist
os.makedirs(INPUT_AUDIO_PATH, exist_ok=True)
os.makedirs(OUTPUT_AUDIO_PATH, exist_ok=True)

# Default audio processing settings
DEFAULT_AUDIO_FORMAT = "wav"  # Output format (e.g., mp3, wav, flac)
DEFAULT_SPEED_FACTOR = 1.2  # Speed adjustment factor (1.0 = original speed)
DEFAULT_VOLUME_CHANGE = 5  # Volume increase/decrease in dB

# API Keys (if using external services like Google Text-to-Speech)
GOOGLE_CLOUD_API_KEY = "your-google-api-key"

# Debug Mode
DEBUG = True
