from gtts import gTTS 
import os
import playsound
def sayinshit(shit):
    tts = gTTS(shit)
    tts.save('hello.mp3')
    playsound.playsound('hello.mp3')
    os.remove('hello.mp3')