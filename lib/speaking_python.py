import pyttsx3

class SpeakingPython:
    AVAILABLE_LANGUAGES = ('en', 'pl', 'es', 'pt', 'it', 'fr')
    
    VOICES = {
        'en': 'com.apple.speech.synthesis.voice.Alex',
        'pl': 'com.apple.speech.synthesis.voice.zosia',
        'es': 'com.apple.speech.synthesis.voice.jorge',
        'pt': 'com.apple.speech.synthesis.voice.joana',
        'it': 'com.apple.speech.synthesis.voice.alice',
        'fr': 'com.apple.speech.synthesis.voice.thomas'
    }
    
    def __init__(self, language='en'):
        if language not in self.AVAILABLE_LANGUAGES:
            raise ValueError(f"Given language is not supported! Has to be one of:\n {self.AVAILABLE_LANGUAGES}")
        
        self.language = language
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.VOICES[language])
        self.engine.setProperty('rate', 170)

    def talk(self, phrase: str):
        """Make your system say given phrase"""
        self.engine.say(phrase)
        self.engine.runAndWait()
