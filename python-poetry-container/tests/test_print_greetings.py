from turtle import undobufferentries
from print_greetings.print_greetings import generate_message

def test_generate_message():
    underTest = generate_message()
    assert underTest == 'Hello world!'

def teset_generate_message_with_valid_input():
    underTest = generate_message('Jeffrey')
    assert underTest == 'Hello Jeffrey!'
