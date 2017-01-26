
from sys import argv, exit
import string
from helpers import alphabet_position, rotate_character


def encrypt(text, rot):
    newstring = ""
    for letter in text:
        newstring += str(rotate_character(letter, rot))
    return newstring

def user_input_is_valid(cl_args):
    if len(cl_args) == 1:
        return False
    if cl_args[1].isalpha():
        return False
    if cl_args[1].isdigit():
        return True
    else:
        return False

def main():
    if user_input_is_valid(argv) == False:
        print("usage: python3 caesar.py n")
        exit()
    message = input("Type a message:")
    print(encrypt(message, argv[1]))

if __name__ == '__main__':
    main()
