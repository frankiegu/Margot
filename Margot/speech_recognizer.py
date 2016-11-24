#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import pyaudio 
import speech_recognition as sr

def recognize_speech(): 
    # Record Audio
    r = sr.Recognizer()
    m = sr.Microphone()
    '''
    with m as source: 
        r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
    '''
    with m as source:
        print("Listening...")
        audio = r.listen(source)
    text = ''
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text =  r.recognize_google(audio)
        print("You said: " + text)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return " " + text + " "
    
if __name__ == "__main__":
    recognize_speech()
   
