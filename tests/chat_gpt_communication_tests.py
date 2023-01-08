import pytest
from lib.chat_gpt_communication import ChatGPTCommunication

@pytest.fixture
def chat_gpt():
    return ChatGPTCommunication()

@pytest.mark.parametrize("text, expected", (
    ("\n\nHello world!\n\n", "Hello world!"),
    ("\n\nHi my friend\n\nAre you okay?", "Hi my friend\n\nAre you okay?")
))
def test_remove_first_and_last_newline_characters(chat_gpt, text, expected):
    assert chat_gpt._remove_first_and_last_newline_characters(text) == expected

@pytest.mark.parametrize("text, expected", (
    ("\n\nHello world!\n\n", "Hello world!"),
    ("\n\nHi my friend\n\nAre you okay?", "Hi my friend. Are you okay?")
))
def test_text_cleaning(chat_gpt, text, expected):
    assert chat_gpt._clean_text(text) == expected