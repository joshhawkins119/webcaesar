import string

def alphabet_position(letter): # This takes a letter and returns the new letter index (number)
    letter = letter.lower()
    return string.ascii_letters.index(letter)

def rotate_character(char, rot):
    if char == " ":
        return char
    if char.islower():
        newidx = alphabet_position(char) + int(rot)
        return string.ascii_letters[newidx].lower()
    if char.isupper():
        newidx = alphabet_position(char) + int(rot)
        return string.ascii_letters[newidx].upper()
    else:
        return char

def encrypt(message, rot):
    newstring = ""
    for letter in message:
        newstring += str(rotate_character(letter, rot))
    return newstring
