from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
from playsound import playsound


# The text that you want to convert to audio
class TextToSpeech:

    def getResponse(self,text):
        # Language in which you want to convert
        language = 'en'
        
        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        myobj = gTTS(text=text, lang=language, slow=False)
        
        # Saving the converted audio in a mp3 file named
        # welcome 
        myobj.save("text.mp3")
        playsound("./text.mp3")