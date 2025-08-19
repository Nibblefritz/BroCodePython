import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters # this helps us add all the chars we want from string without having to put them all in ourselves
chars = list(chars)
key = chars.copy() # we copy the chars list so we can shuffle it without changing the original
random.shuffle(key) # this shuffles the key list so we can use it to encrypt and decrypt

# print(f"chars: {chars}")
# print(f"key: {key}")

# Encryption
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""
for char in plain_text:
    if char in chars:
        index = chars.index(char) # find the index of the character in chars
        cipher_text += key[index] # find the corresponding character in key

print(f"Original text: {plain_text}")
print(f"Encrypted text: {cipher_text}")

# Decryption
cipher_text = input("Enter the text to decrypt: ")
decrypted_text = ""
for char in cipher_text:
    if char in key:
        index = key.index(char) # find the index of the character in key
        decrypted_text += chars[index] # find the corresponding character in chars

print(f"Decrypted text: {decrypted_text}")