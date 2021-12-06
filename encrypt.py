class Message:

    #constructer
    def __init__(self,text,cle):
        self.text=text
        self.cle=cle
    
    #cesar
    def cesar(self,text,cle):
        result = ""
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
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
    def cesar_list(self,text,cle):
        result=""
        words=[]
        encrypteds=[]
        words=self.text.split()
        for word in words:
            encrypteds.append(self.cesar(word,self.cle))
        for i in encrypteds:
            result+=" "+i
        return result
    
    #decrypt cesar
    def cesar_dec(self,text,cle):
        result = ""
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
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

    def vegenere(self,message,cle):
        result=""
        return result

    def vegenere_dec(self,message,cle):
        result=""
        return result

    # Python code to implement
# Vigenere Cipher
 
# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
     
# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
     
# Driver code
if __name__ == "__main__":
    string = "HELLOWORLD"
    keyword = "AYUSH"
    key = generateKey(string, keyword)
    cipher_text = cipherText(string,key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :",
           originalText(cipher_text, key))