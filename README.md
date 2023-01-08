# Jarvis GPT
A Python project which listens to user's speech and answers his/her questions using openai chat GPT API.

# Usage
First create a virtual environment and install all the requirements.

```
$ python3 -m venv venv
$ venv/bin/activate \
(venv)$ pip install -r requirements.txt
```

Configure .env file by creating it in the root directory of the project (or duplicate .env.example) and put your api key in it.
```
OPENAI_API_KEY="MY_EXAMPLE_API_KEY_HERE"
```

Now you're ready to go!
Run the script passing lang flage for the language that you want to talk in and see how it goes.

Example usage:
```
$ python3 main.py --lang pl
```

## Available languages
To see which languages are supported open `speaking_python` module and read `AVAILABLE_LANGUAGES` and `VOICES`.
Those are just a couple of languages out of many that could be used. If you need any other, simply add it to the list following rules of imported modules and packages.

```
    # ...
    AVAILABLE_LANGUAGES = ('en', 'pl', 'es', 'pt', 'it', 'fr')
    
    VOICES = {
        'en': 'com.apple.speech.synthesis.voice.Alex',
        'pl': 'com.apple.speech.synthesis.voice.zosia',
        'es': 'com.apple.speech.synthesis.voice.jorge',
        'pt': 'com.apple.speech.synthesis.voice.joana',
        'it': 'com.apple.speech.synthesis.voice.alice',
        'fr': 'com.apple.speech.synthesis.voice.thomas'
    }
    # ...
```
