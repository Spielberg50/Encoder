#import pyperclip
'''
def main():
    myMessage = 'cryptographie'
    myKey = 5
    ciphertext = encrypt_trans(myKey, myMessage)
    print(type(myKey))
    print("Cipher Text is")
    print(ciphertext + '|')
    #pyperclip.copy(ciphertext)
'''
def encrypt_trans(text, key):
    ciphertext = [''] * key
   
    for col in range(key):
        position = col
        while position < len(text):
            ciphertext[col] += text[position]
            position += key
    return ''.join(ciphertext) #Cipher text

def decrypt_trans(text, key):
    pass
'''
if __name__ == '__main__':
    main()
'''