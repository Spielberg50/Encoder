
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
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
        
    # This function returns the
    # encrypted text generated
    # with the help of the key
def encrypt_veg(string, key):
    cipher_text = []
    for i in range(len(string)):
        if(string[i]==" "):
            x=" "
        else:
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
        
    # This function decrypts the
    # encrypted text and returns
    # the original text
def decrypt_veg(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
        



# Driver code

if __name__ == "__main__":   
    string = "test de programmation de chiffrement bioinfo bonjour table salle informatique imprimante chaise miroire longueur largeur bouteille souris ajouter rechercher clavier bien trop"
    string=string.upper()
    string=string.split()
    string="".join(string)
    keyword = "BIOINF"
    
    key = generateKey(string, keyword)
    cipher_text = encrypt_veg(string,key)
    print("\ntext:",string)
    print("Ciphertext     :", cipher_text)
    print("key            :", key)
    print("Decrypted Text :", decrypt_veg("ivgn tfhlk gfyszsl zvgn vfil rrzauiwnnds xk mwakeslk rjyi lby ics xk tfsvkoak gsnoks", key),"\n") 
   
