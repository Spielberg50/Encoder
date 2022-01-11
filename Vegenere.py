def encrypt_veg(message, key):
    key = generateKey(message, key)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = ""
    for i in range(len(message)):
        if message[i].isalpha():
            val = (alphabet.find(message[i]) + alphabet.find(key[i])) % 26
            cipher_text += alphabet[val]
        else:
            cipher_text += message[i]
    return cipher_text

def decrypt_veg(message, key):
    key = generateKey(message, key)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""
    for i in range(len(message)):
        if message[i].isalpha():
            val = (alphabet.find(message[i]) - alphabet.find(key[i])) % 26
            decrypted += alphabet[val]
        else:
            decrypted += message[i]
    return decrypted

def generateKey(message, key):

    long_key = ""
    j = 0

    for i in range(len(message)):
        if message[i] == " ":
            # ignoring spaces
            long_key += " "
        else:
            if j < len(key):
                long_key += key[j]
                j += 1
            else:
                j = 0
                long_key += key[j]
                j += 1
                
    return long_key

def main():   
    string = "cest notre premier test pour lalgorithme de vigenere avec une cle de cryptage petite"
    keyword = "depart"   
    
    cipher_text = encrypt_veg(string,keyword)
    print("\ntext:",string)
    print("Ciphertext     :", cipher_text)
    print("key            :", keyword)
    print("Decrypted Text :", decrypt_veg("fiht ehwvt pixpmtr kxvx eolk oeagfklxwmv wh zxgvghvt amxf yce teh ht cirsxpgv ihxxtv", "depart"),"\n") 

if __name__ == "__main__":
    main()
    #je suis tres mais tres heureuse de vous retrouvez avec moi aujourdhui parceque jai finis mes etudes et je vais rester a la maison mais cest clair parceque tout le monde est comme ca