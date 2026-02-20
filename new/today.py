from gtts import gTTS
from playsound import playsound
import os
from pydub import AudioSegment
import threading

def player(text):
    mp3_file = "speech.mp3"
    wav_file = "speech.wav"

    # Generate MP3
    tts = gTTS(text=text, lang='en')
    tts.save(mp3_file)

    # Convert to WAV (more stable for Windows)
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")
    os.remove(mp3_file)  # delete MP3

    def play_and_delete():
        playsound(wav_file)
        os.remove(wav_file)

    threading.Thread(target=play_and_delete).start()

