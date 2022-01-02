import math


def main():
    myMessage = 'cryptographie '
    myKey = 5
    ciphertext = encrypt_trans(myMessage, myKey)
    print("Cipher Text is :",ciphertext + '|')
    plaintext=decrypt_trans(ciphertext,myKey)
    print("plaintext :",plaintext+"|")
    


def encrypt_trans(text, key):
    ciphertext = [''] * key
    
    for col in range(key):
        position = col
        while position < len(text):
            ciphertext[col] += text[position]
            position += key
    return ''.join(ciphertext) #Cipher text

def decrypt_trans(text, key):
    numOfColumns = math.ceil(len(text) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(text)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
    for symbol in text:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0 
            row += 1 
    return ''.join(plaintext)

# if __name__ == '__main__':
#     main()
