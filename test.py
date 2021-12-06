import Cesar as C
import Vegenere as V

#test cesar
#encrypt
import Cesar as C
text="TEST DE PROGRAMMATION DE \n CHIFREMENT BIOINFO"
key=16
cipher=C.encrypt(text,key)
print("Message: "+ text + '\nClé: ' + str(key) + "\nencrypted:" + cipher)

#decrypt
text="JUIJ TU FHEWHQCCQJYED TU SXYVHUCUDJ RYEYDVE"
key=16
print("\nMessage: "+ cipher + '\nClé: ' + str(key) + "\ndecrypted:" + C.decrypt(cipher,key))

# #test vegenere
# #encrypt
# import Vegenere as V
# text="TEST DE PROGRAMMATION DE CHIFFREMENT BIOINFO"
# keyword="DEPTINFO"
# key=""
# text=text.split()
# text="".join(text)

# key = V.generateKey(text,keyword)
# cipher_text =V.encrypt_veg(text,key)

# print("\nMessage:   "+ text + 
#         '\nClé:       ' + key + 
#         "\nencrypted: " + cipher_text+"\n")

# #decrypt
# import Vegenere as V
# print("Decrypted Text :", V.decrypt_veg("WIHMLRUFRKGTUZFHLSCWMPMWIJGXURSHEMDBVST", "DEPTINFO"),"\n")

# #substitution
# #encrypt
# import Substitution as S
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# key =      "fcpevqkzgmtrayonujdlwhbxsi"
# text = "TEST DE PROGRAMMATION DE CHIFFREMENT BIOINFO"

# # def encrypt_sub(message,key,alphabet):
# #     result = ""
# #     for letter in text:
# #         if letter.lower() in alphabet:
# #             result += key[alphabet.find(letter.lower())]
# #         else:
# #             result += letter
# #     return result

# print(S.encrypt_sub(text,key,alphabet))

# #transposition
# #encrypt
# import Transposition as T
# text='cryptographie'
# key=5
# print(T.encrypt_trans(text,key))
