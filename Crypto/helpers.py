import string

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

def alphabet_position(letter): # This takes a letter and returns the new letter index (number)
    letter = letter.lower()
    return string.ascii_letters.index(letter)

#This takes a letter and rotation number and gives you the actual new encrypted letter back

if __name__ == '__main__':
    main()
