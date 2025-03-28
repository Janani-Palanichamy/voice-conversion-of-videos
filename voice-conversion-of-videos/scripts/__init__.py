# __init__.py

from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Import routes to register them with the app
from scripts import audio_processing
from scripts import config
