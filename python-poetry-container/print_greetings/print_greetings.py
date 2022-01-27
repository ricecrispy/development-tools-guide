#!/usr/bin/python

import sys

'''Return message'''
def generate_message(name=''):
    greeter = name if name else "world"
    return f"Hello {greeter}!"

user_input = ''
if len(sys.argv) > 1:
    user_input = sys.argv[1]

print(generate_message(user_input))
