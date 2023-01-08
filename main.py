
import click
from lib.chat_gpt_communication import ChatGPTCommunication

@click.command()
@click.option('--lang', default='en', type=click.Choice(['en','fr','es','pl','pt','it']), help='A language that Jarvis will expect')
def ask_jarvis(lang):
    chat_gpt = ChatGPTCommunication()
    chat_gpt.voice_ask(lang)

if __name__ == '__main__':
    ask_jarvis()