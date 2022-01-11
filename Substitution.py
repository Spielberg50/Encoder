def encrypt_sub(text,key,alphabet):
    result = ""
    for letter in text:
        if letter.lower() in alphabet:
            result += key[alphabet.find(letter.lower())]
        else:
            result += letter
    return result

def decrypt_sub(text,key,alphabet):
    result = ""
    for letter in text:
        if letter == " ":
            result += " "
        if letter.lower()in key:
            result += alphabet[key.find(letter.lower())]
    return result

'''
alphabet = "abcdefghijklmnopqrstuvwxyz"
key =      "fcpevqkzgmtrayonujdlwhbxsi"
text = "TEST DE PROGRAMMATION DE CHIFFREMENT BIOINFO"
'''
'''
encrypted = encrypt_sub(text,key,alphabet)
print(encrypted)

decrypted = decrypt_sub(encrypted,key,alphabet)
print(decrypted)
'''