# Encrypts and decrypts a text.
# Try with the following line:
# L'yh ehhq wuBlq' wr fdoo / L'yh ehhq rq pB rzq iru orqj hqrxjk / PdBeh Brx fdq vkrz ph krz wr oryh, pdBeh

import getpass
import string


def encrypt_char(char):
    characters = list(string.ascii_letters + string.digits)
    if char in characters:
        index = characters.index(char)
        character_count = len(characters)
        return characters[(index + 3) % character_count]
    else:
        return char


def encrypt(plain_text):
    encrypted_characters = [encrypt_char(char) for char in plain_text]
    return ''.join(encrypted_characters)


def decrypt(encrypted_text):
    return "I cannot decrypt this text :("


choice = input("(E)ncrypt or (D)ecrypt: ")
if choice in ['e', 'E']:
    text = getpass.getpass("Enter text to encrypt: ")
    print(encrypt(text))
elif choice in ['d', 'D']:
    text = input("Enter encrypted text: ")
    print(decrypt(text))
