import string
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    new_txt = text[:0]
    key_list = []
    for char in range(len(text)): # 0 - 18
        key_idx = char % len(key) #0 % 4
        newkey = alphabet_position(key[key_idx])   # stores the current key index
        key_list.append(newkey)                    # adds current key index to key_list as an item in list
                                                   #
        if not str(text[char]).isalpha():          #tests if current character is Not alphabetical order
            key_list.insert(char, " ")             #inserts space
        new_txt += rotate_character(text[char], key_list[char]) # calls change_character function to add new_text string
    return new_txt

def main():
    user_string = input("Type a message:")
    user_key = input("Encryption key:")
    print(encrypt(user_string, user_key))


# def main():
#     vigstring = "This is a miracle"
#     vigkey = "holywow"
#     print(encrypt(vigstring, vigkey))

if __name__ == '__main__':
    main()
