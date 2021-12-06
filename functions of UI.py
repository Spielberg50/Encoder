# pyuic5 -x GUI.ui -o GUI.py

import sys
sys.path.insert(1, 'D:/Etude/BSD/TP')
import Vegenere as V
import Cesar as C
import Substitution as S
import Transposition as T

text=""
keyword=""
result=""
key=0
alphabet = "abcdefghijklmnopqrstuvwxyz"

# self.onlyInt = QtGui.QIntValidator()
# self.lineEdit_key.setValidator(self.onlyInt)

self.actionCesar.triggered.connect(self.cesar_enc)
self.actionVegenere.triggered.connect(self.veg_enc)
self.actionSubstitution.triggered.connect(self.sub_enc)
self.actionTransposition.triggered.connect(self.trans_enc)

self.actionC_sar_2.triggered.connect(self.cesar_dec)
self.actionVegen_re_2.triggered.connect(self.veg_dec)
self.actionSubstitution_2.triggered.connect(self.sub_dec)

self.pushButton_Submit.clicked.connect(lambda: self.sub_dec())

def veg_enc(self):
    
    self.text = self.lineEdit_message.text()
    self.keyword = self.lineEdit_key.text()
    print(self.text+"\n")
    print(self.keyword+"\n")
    self.text=self.text.split()
    self.text="".join(self.text)
    key= V.generateKey(self.text,self.keyword)
    encrypted=V.encrypt_veg(self.text,key)
    self.lineEdit_result.setText(encrypted)

def cesar_enc(self):

    self.text = self.lineEdit_message.text()
    self.key = int(self.lineEdit_key.text())
    print(self.text+"\n")
    print(str(self.key)+"\n")
    encrypted=C.encrypt(self.text,self.key)
    self.lineEdit_result.setText(encrypted)

def sub_enc(self):
    self.text = self.lineEdit_message.text()
    self.key = self.lineEdit_key.text()
    print(self.text+"\n")
    print(self.keyword+"\n")
    encrypted=S.encrypt_sub(self.text,self.key,self.alphabet)
    self.lineEdit_result.setText(encrypted)

def trans_enc(self):

    self.text = self.lineEdit_message.text()
    self.key = int(self.lineEdit_key.text())
    print(self.text+"\n")
    print(str(self.key)+"\n")
    encrypted=T.encrypt_trans(self.text,self.key)
    self.lineEdit_result.setText(encrypted)

def cesar_dec(self):
    self.text = self.lineEdit_message.text()
    self.key = int(self.lineEdit_key.text())
    print(self.text+"\n")
    print(str(self.key)+"\n")
    decrypted=C.decrypt(self.text,self.key)
    self.lineEdit_result.setText(decrypted)

def veg_dec(self):
    self.text = self.lineEdit_message.text()
    self.keyword = self.lineEdit_key.text()
    print(self.text+"\n")
    print(str(self.key)+"\n")
    key=V.generateKey(self.text,self.keyword)
    decrypted=V.decrypt_veg(self.text,key)
    self.lineEdit_result.setText(decrypted)

def sub_dec(self):
    self.text = self.lineEdit_message.text()
    self.key = self.lineEdit_key.text()
    print(self.text+"\n")
    print(self.keyword+"\n")
    encrypted=S.decrypt_sub(self.text,self.key,self.alphabet)
    self.lineEdit_result.setText(encrypted)

def trans_dec(self):
    pass