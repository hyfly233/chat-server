import speech_recognition as sr
from gtts import gTTS
import os
import io

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
    return None

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    os.system(f"start {output_file}")

def audio_to_stream(file_path):
    with open(file_path, "rb") as audio_file:
        audio_stream = io.BytesIO(audio_file.read())
    return audio_stream
