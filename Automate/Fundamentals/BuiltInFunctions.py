import sys, os, math
import pyperclip
# Makes all functions available, but clearer if appended with function
from random import *

randint(1, 5)

# Pyperclip module to copy and past things to clipboard
# pyperclip.copy('Hello World')
# pyperclip.paste('Goodbye')

def hello(name): 
    return 'Hello ' + name

greet = hello('David')

print(greet)