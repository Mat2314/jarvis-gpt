import speech_recognition as sr

r = sr.Recognizer()

def speech_to_text(language: str):
    """Language reference: https://gist.github.com/msikma/8912e62ed866778ff8cd"""
    
    print("Talk now")
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.listen(source)
    
    # convert speech to text
    print("Converting...")
    text = r.recognize_google(audio_data, language=language)
    return text