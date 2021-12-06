# ======= VIGENERE ======#
def generateKey(msg, cle):
    newKey = ""
    j = 0

    for i in range(len(msg)):
        if msg[i] == " ":
            # ignoring space
            newKey += " "
        else:
            if j < len(cle):
                newKey += cle[j]
                j += 1
            else:
                j = 0
                newKey += cle[j]
                j += 1
    return newKey

def encrypt_veg(resVigenere, nvCle):
    nvCle = generateKey(resVigenere, nvCle)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    orig_msg = ""
    for i in range(len(resVigenere)):
        if resVigenere[i].isalpha():
            val = (alphabet.find(resVigenere[i]) + alphabet.find(nvCle[i])) % 26
            orig_msg += alphabet[val]
        else:
            orig_msg += resVigenere[i]
    return orig_msg

def decrypt_veg(resVigenere, nvCle):
    nvCle = generateKey(resVigenere, nvCle)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    orig_msg = ""
    for i in range(len(resVigenere)):
        if resVigenere[i].isalpha():
            val = (alphabet.find(resVigenere[i]) - alphabet.find(nvCle[i])) % 26
            orig_msg += alphabet[val]
        else:
            orig_msg += resVigenere[i]
    return orig_msg

if __name__ == "__main__":   
    string = "cest notre premier test pour lalgorithme de vigenere avec une cle de cryptage petite"
    keyword = "depart"   
    
    cipher_text = encrypt_veg(string,keyword)
    print("\ntext:",string)
    print("Ciphertext     :", cipher_text)
    print("key            :", keyword)
    print("Decrypted Text :", decrypt_veg("fiht ehwvt pixpmtr kxvx eolk oeagfklxwmv wh zxgvghvt amxf yce teh ht cirsxpgv ihxxtv", "depart"),"\n") 

    #je suis tres mais tres heureuse de vous retrouvez avec moi aujourdhui parceque jai finis mes etudes et je vais rester a la maison mais cest clair parceque tout le monde est comme ca