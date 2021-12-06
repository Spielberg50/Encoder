#cesar
def encrypt(text,cle):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        if(char=="\n"):
            result+="\n"
        else:
            #Ignore the space
            if (char==" "):
                result += " "
            else:
                # Encrypt uppercase characters in plain text
                if (char.isupper()):
                    result += chr((ord(char) + cle-65) % 26 + 65)
                # Encrypt lowercase characters in plain text
                else:
                    result += chr((ord(char) + cle - 97) % 26 + 97)
    return result
    
    #cesar with lists
def cesar_list(text,cle):
    result=""
    words=[]
    encrypteds=[]
    words=text.split()
    for word in words:
        encrypteds.append(encrypt(word,cle))
    for i in encrypteds:
        result+=" "+i
    return result
    
    #decrypt cesar
def decrypt(text,cle):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        if(char=="\n"):
            result+="\n"
        else:
            #ignore the space
            if (ord(char)==32):
                result += " "
            else:
                # Encrypt uppercase characters in plain text
                if (char.isupper()):
                    result += chr((ord(char) - cle-65) % 26 + 65)
                # Encrypt lowercase characters in plain text
                else:
                    result += chr((ord(char) - cle - 97) % 26 + 97)
    return result

