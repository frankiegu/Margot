# from os import system
#  
# def speak(msg):
#     print(msg)
#     system('say '+msg)
    
    
from gtts import gTTS
import subprocess
  
def speak(msg):
    print("Margot: "+msg)
    tts = gTTS(text=msg, lang='en-au')
    tts.save("good.mp3")
    subprocess.call(["afplay", "good.mp3"])

# import subprocess
#  
# def speak(text):
#     subprocess.call('say ' + text, shell=True)

# if __name__ == '__main__':
#     speak("Nasty women")
    
