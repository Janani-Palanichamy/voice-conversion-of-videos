from gtts import gTTS
import os



# Get text and language from the user
#text = input("Enter the text you want to convert to audio: ")
def text_to_speech(text):
    
    language = input("Enter the language code (e.g., 'en' for English, 'hi' for Hindi, 'ta' for Tamil): ")
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        output_file = "output_audio.mp3"
        tts.save(output_file)
        os.system(f"start {output_file}")  # Use 'start' on Windows, 'open' on macOS, and 'xdg-open' on Linux
        print(f"Audio file saved as {output_file} and is playing now.")
    except Exception as e:
        print(f"An error occurred: {e}")

with open ("scripts/english_translation.txt","r") as file:
    text=file.read()
text_to_speech(text)   
