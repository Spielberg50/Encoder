
import sys
import os
path = os.path.split(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, path[0])
import Vegenere as V
import Cesar as C
import Substitution as S
import Transposition as T
import crack_fonctions as crack
import KNN as DES
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from PyQt5 import QtCore

from flask import Flask, request,current_app
from handler import validate_encrypt_request
import requests
import netifaces
import json
class Server_Worker(QtCore.QObject):
    res = QtCore.pyqtSignal(dict)
    app = Flask(__name__)

    def __init__(self):
        super().__init__()
    

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"
    

    @app.route('/encrypt', methods=['POST'])
    def encrypt():
        requestJson = request.get_json()
        validate_encrypt_request(requestJson)
        sender = requestJson['sender']
        algorithm = requestJson['algorithm']
        message = requestJson['message']
        key = requestJson['key']
        typed = requestJson['type']
        current_app.config['obj'].res.emit(requestJson)

        return requestJson

    def run(self):
        self.app.config['obj'] = self
        self.app.run(host="0.0.0.0",port=3000)

class Ui_MainWindow(object):
    text=""
    keyword=""
    result=""
    key=0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char=""
    list_dict={}
    btn_clicked=""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_message = QtWidgets.QLabel(self.centralwidget)
        self.label_message.setGeometry(QtCore.QRect(20, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_message.setFont(font)
        self.label_message.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.setObjectName("label_message")
        self.label_key = QtWidgets.QLabel(self.centralwidget)
        self.label_key.setGeometry(QtCore.QRect(20, 190, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_key.setFont(font)
        self.label_key.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_key.setAlignment(QtCore.Qt.AlignCenter)
        self.label_key.setObjectName("label_key")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(20, 290, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_result.setFont(font)
        self.label_result.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.TextEdit_message = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit_message.setGeometry(QtCore.QRect(130, 29, 421, 141))
        self.TextEdit_message.setText("")
        self.TextEdit_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.TextEdit_message.setReadOnly(True)
        self.TextEdit_message.setObjectName("TextEdit_message")
        font_2 = QtGui.QFont()
        font_2.setPointSize(12)
        self.TextEdit_message.setFont(font_2)
        self.LineEdit_key = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_key.setGeometry(QtCore.QRect(130, 190, 421, 20))
        self.LineEdit_key.setReadOnly(True)
        self.LineEdit_key.setObjectName("LineEdit_key")
        self.TextEdit_result = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit_result.setGeometry(QtCore.QRect(130, 229, 421, 131))
        self.TextEdit_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.TextEdit_result.setReadOnly(True)
        self.TextEdit_result.setObjectName("TextEdit_result")
        self.TextEdit_result.setFont(font_2)
        self.pushButton_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Submit.setEnabled(False)
        self.pushButton_Submit.setGeometry(QtCore.QRect(260, 370, 75, 23))
        self.pushButton_Submit.setObjectName("pushButton_Submit")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(398, 460, 121, 22))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 21))
        self.menubar.setObjectName("menubar")
        self.menuCryptage = QtWidgets.QMenu(self.menubar)
        self.menuCryptage.setObjectName("menuCryptage")
        self.menuBasiques = QtWidgets.QMenu(self.menuCryptage)
        self.menuBasiques.setObjectName("menuBasiques")
        self.menuSym_triques = QtWidgets.QMenu(self.menuCryptage)
        self.menuSym_triques.setObjectName("menuSym_triques")
        self.menuAsym_triques = QtWidgets.QMenu(self.menuCryptage)
        self.menuAsym_triques.setObjectName("menuAsym_triques")
        self.menuDecryptage = QtWidgets.QMenu(self.menubar)
        self.menuDecryptage.setObjectName("menuDecryptage")
        self.menuBasiques_2 = QtWidgets.QMenu(self.menuDecryptage)
        self.menuBasiques_2.setObjectName("menuBasiques_2")
        self.menuSym_triques_2 = QtWidgets.QMenu(self.menuDecryptage)
        self.menuSym_triques_2.setObjectName("menuSym_triques_2")
        self.menuAsym_triques_2 = QtWidgets.QMenu(self.menuDecryptage)
        self.menuAsym_triques_2.setObjectName("menuAsym_triques_2")
        self.menuCrack = QtWidgets.QMenu(self.menubar)
        self.menuCrack.setObjectName("menuCrack")
        self.menuBasiques_3 = QtWidgets.QMenu(self.menuCrack)
        self.menuBasiques_3.setObjectName("menuBasiques_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSymetriques_3 = QtWidgets.QAction(MainWindow)
        self.actionSymetriques_3.setObjectName("actionSymetriques_3")
        self.actionAsym_triques_3 = QtWidgets.QAction(MainWindow)
        self.actionAsym_triques_3.setObjectName("actionAsym_triques_3")
        self.actionCesar = QtWidgets.QAction(MainWindow)
        self.actionCesar.setObjectName("actionCesar")
        self.actionVegenere = QtWidgets.QAction(MainWindow)
        self.actionVegenere.setObjectName("actionVegenere")
        self.actionSubstitution = QtWidgets.QAction(MainWindow)
        self.actionSubstitution.setObjectName("actionSubstitution")
        self.actionTransposition = QtWidgets.QAction(MainWindow)
        self.actionTransposition.setObjectName("actionTransposition")
        self.actionCesar_2 = QtWidgets.QAction(MainWindow)
        self.actionCesar_2.setObjectName("actionCesar_2")
        self.actionVegenere_2 = QtWidgets.QAction(MainWindow)
        self.actionVegenere_2.setObjectName("actionVegenere_2")
        self.actionSubstitution_2 = QtWidgets.QAction(MainWindow)
        self.actionSubstitution_2.setObjectName("actionSubstitution_2")
        self.actionTransposition_2 = QtWidgets.QAction(MainWindow)
        self.actionTransposition_2.setObjectName("actionTransposition_2")
        self.actionVegenere3 = QtWidgets.QAction(MainWindow)
        self.actionVegenere3.setObjectName("actionVegenere3")
        self.actionDES = QtWidgets.QAction(MainWindow)
        self.actionDES.setObjectName("actionDES")
        self.actionRSA = QtWidgets.QAction(MainWindow)
        self.actionRSA.setObjectName("actionRSA")
        self.actionDES_2 = QtWidgets.QAction(MainWindow)
        self.actionDES_2.setObjectName("actionDES_2")
        self.actionRSA_2 = QtWidgets.QAction(MainWindow)
        self.actionRSA_2.setObjectName("actionRSA_2")
        self.menuBasiques.addAction(self.actionCesar)
        self.menuBasiques.addAction(self.actionVegenere)
        self.menuBasiques.addAction(self.actionSubstitution)
        self.menuBasiques.addAction(self.actionTransposition)
        self.menuSym_triques.addAction(self.actionDES)
        self.menuAsym_triques.addAction(self.actionRSA)
        self.menuCryptage.addAction(self.menuBasiques.menuAction())
        self.menuCryptage.addSeparator()
        self.menuCryptage.addAction(self.menuSym_triques.menuAction())
        self.menuCryptage.addSeparator()
        self.menuCryptage.addAction(self.menuAsym_triques.menuAction())
        self.menuBasiques_2.addAction(self.actionCesar_2)
        self.menuBasiques_2.addAction(self.actionVegenere_2)
        self.menuBasiques_2.addAction(self.actionSubstitution_2)
        self.menuBasiques_2.addAction(self.actionTransposition_2)
        self.menuSym_triques_2.addAction(self.actionDES_2)
        self.menuAsym_triques_2.addAction(self.actionRSA_2)
        self.menuDecryptage.addAction(self.menuBasiques_2.menuAction())
        self.menuDecryptage.addSeparator()
        self.menuDecryptage.addAction(self.menuSym_triques_2.menuAction())
        self.menuDecryptage.addSeparator()
        self.menuDecryptage.addAction(self.menuAsym_triques_2.menuAction())
        self.menuBasiques_3.addAction(self.actionVegenere3)
        self.menuCrack.addAction(self.menuBasiques_3.menuAction())
        self.menuCrack.addSeparator()
        self.menuCrack.addAction(self.actionSymetriques_3)
        self.menuCrack.addSeparator()
        self.menuCrack.addAction(self.actionAsym_triques_3)
        self.menubar.addAction(self.menuCryptage.menuAction())
        self.menubar.addAction(self.menuDecryptage.menuAction())
        self.menubar.addAction(self.menuCrack.menuAction())

        self.pushButton_Envoye = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Envoye.setGeometry(QtCore.QRect(420, 500, 75, 23))
        self.pushButton_Envoye.setObjectName("pushButton_Envoye")
        self.pushButton_request = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_request.setGeometry(QtCore.QRect(300, 460, 75, 23))
        self.pushButton_request.setObjectName("pushButton_request")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.server_worker = Server_Worker()
        self.thread = QtCore.QThread()
        self.server_worker.moveToThread(self.thread)
        self.thread.started.connect(self.server_worker.run)
        self.server_worker.res.connect(self.p)
        self.thread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encoder"))
        self.label_message.setText(_translate("MainWindow", "Message"))
        self.label_key.setText(_translate("MainWindow", "Clé"))
        self.label_result.setText(_translate("MainWindow", "Résultat"))
        self.TextEdit_message.setPlaceholderText(_translate("MainWindow", "Bienvenu, vous devez choisir l\'algorithme dans le menu"))
        self.pushButton_Submit.setText(_translate("MainWindow", "Executer"))
        self.pushButton_Envoye.setText(_translate("MainWindow", "Envoyer"))
        self.pushButton_request.setText(_translate("MainWindow", "Liste"))
        self.menuCryptage.setTitle(_translate("MainWindow", "Cryptage"))
        self.menuBasiques.setTitle(_translate("MainWindow", "Basiques"))
        self.menuSym_triques.setTitle(_translate("MainWindow", "Symétriques"))
        self.menuAsym_triques.setTitle(_translate("MainWindow", "Asymétriques"))
        self.menuDecryptage.setTitle(_translate("MainWindow", "Décryptage"))
        self.menuBasiques_2.setTitle(_translate("MainWindow", "Basiques"))
        self.menuSym_triques_2.setTitle(_translate("MainWindow", "Symétriques"))
        self.menuAsym_triques_2.setTitle(_translate("MainWindow", "Asymétriques"))
        self.menuCrack.setTitle(_translate("MainWindow", "Crack"))
        self.menuBasiques_3.setTitle(_translate("MainWindow", "Basiques"))
        self.actionSymetriques_3.setText(_translate("MainWindow", "Symétriques"))
        self.actionAsym_triques_3.setText(_translate("MainWindow", "Asymétriques"))
        self.actionCesar.setText(_translate("MainWindow", "César"))
        self.actionVegenere.setText(_translate("MainWindow", "Vegenère"))
        self.actionSubstitution.setText(_translate("MainWindow", "Substitution"))
        self.actionTransposition.setText(_translate("MainWindow", "Transposition"))
        self.actionCesar_2.setText(_translate("MainWindow", "César"))
        self.actionVegenere_2.setText(_translate("MainWindow", "Vegenère"))
        self.actionSubstitution_2.setText(_translate("MainWindow", "Substitution"))
        self.actionTransposition_2.setText(_translate("MainWindow", "Transposition"))
        self.actionVegenere3.setText(_translate("MainWindow", "Vegenère"))
        self.actionDES.setText(_translate("MainWindow", "DES"))
        self.actionRSA.setText(_translate("MainWindow", "RSA"))
        self.actionDES_2.setText(_translate("MainWindow", "DES"))
        self.actionRSA_2.setText(_translate("MainWindow", "RSA"))

        self.actionCesar.triggered.connect(lambda: self.num("01"))
        self.actionVegenere.triggered.connect(lambda: self.car("02"))
        self.actionSubstitution.triggered.connect(lambda: self.car("03"))
        self.actionTransposition.triggered.connect(lambda: self.num("04"))

        self.actionCesar_2.triggered.connect(lambda: self.num("11"))
        self.actionVegenere_2.triggered.connect(lambda: self.car("12"))
        self.actionSubstitution_2.triggered.connect(lambda: self.car("13"))
        self.actionTransposition_2.triggered.connect(lambda: self.num("14"))

        self.actionDES.triggered.connect(lambda: self.car("05"))
        self.actionDES_2.triggered.connect(lambda: self.car("15"))


        self.actionVegenere3.triggered.connect(lambda: self.num("21"))
        self.pushButton_Submit.clicked.connect(lambda: self.submit(self.char))
        
        self.pushButton_Envoye.clicked.connect(self.send)
        self.pushButton_request.clicked.connect(self.req)

    def p(self,val):
    # add this in your QMainWindow class and write UI changes here the val varible is what result of the post request
        print(val)
        self.show_popup_qst("vous avez reçu un message depuis "+val["sender"]+"\n"+"voulez vous accepter")
        if(self.btn_clicked=="Yes"):
            self.TextEdit_result.setText(str(val))
            self.TextEdit_message.setText(val["message"])
            decrypted=""

            _translate = QtCore.QCoreApplication.translate

            if(val["algorithm"]=="ceasar"):
                self.onlyInt = QtGui.QIntValidator()
                self.LineEdit_key.setValidator(self.onlyInt)
                self.LineEdit_key.setText(str(val["key"]))
                decrypted=C.decrypt(val["message"],val["key"])

            if(val["algorithm"]=="vigenere"):
                self.LineEdit_key.setText(str(val["key"]))
                self.onlyInt = QtGui.QRegExpValidator(QtCore.QRegExp("[a-z A-Z]+"))
                self.LineEdit_key.setValidator(self.onlyInt)
                decrypted=V.decrypt_veg(val["message"],val["key"])

            if(val["algorithm"]=="substitution"):
                self.LineEdit_key.setText(str(val["key"]))
                self.onlyInt = QtGui.QRegExpValidator(QtCore.QRegExp("[a-z A-Z]+"))
                self.LineEdit_key.setValidator(self.onlyInt)
                decrypted=S.decrypt_sub(val["message"],val["key"],self.alphabet) 

            if(val["algorithm"]=="transposition"):
                self.onlyInt = QtGui.QIntValidator()
                self.LineEdit_key.setValidator(self.onlyInt)
                self.LineEdit_key.setText(str(val["key"]))
                decrypted=T.decrypt_trans(val["message"],val["key"])

            if(val["algorithm"]=="des"):
                self.onlyInt = QtGui.QRegExpValidator(QtCore.QRegExp("[a-z A-Z]+"))
                self.LineEdit_key.setValidator(self.onlyInt)
                self.LineEdit_key.setText(str(val["key"]))
                if len(str(val["key"]))==8:
                    decrypted=DES.decrypt_des(val["message"],val["key"])
                else:
                    self.show_popup_error('La longueur de la clé doit etre 8\nvous avez mis une cle de taille '+str(len(self.keyword)))
            self.TextEdit_result.setText(decrypted)
        if(self.btn_clicked=="No"):
            pass


        

    def send(self):
        # data = json.loads(self.TextEdit_result.toPlainText())
        # data = dict(self.textEdit_2.toPlainText())
        message=self.TextEdit_result.toPlainText()
        kay=self.LineEdit_key.text()
        if (self.char=="01"):
            algo="ceasar"
            kay=int(kay)
        if (self.char=="02"):
            algo="vigenere"
        if (self.char=="03"):
            algo="substitution"
        if (self.char=="04"):
            algo="transposition"
            kay=int(kay)
        if (self.char=="05"):
            algo="des"


        code=self.send_data( self.list_dict[self.comboBox.currentText()],"SOUKEUR",algo,message,kay)
        if code==200:
            print("Message sent")
            self.show_popup_info("Message envoyé")
        else:
            self.show_popup_error('Le message n a pas été envoyé \navec code '+str(code))
            print("error")

    
    def request(self,name,state=True):
        data = {'name':name,'active':state}
        try:
                x = requests.post(f"http://{self.get_gatway_ip()}:3000/get-peers",json=data)
                if x.status_code == 200:
                        return self.extract_list_of_users(x.json())
                else:
                        return {}
        except:
                return {}

    def extract_list_of_users(self,peer_data):
        temp_list = {}
        if len(peer_data) == []:
                return temp_list
        else:
                for user in peer_data:
                        if user['active'] == True:
                                temp_list[user['ip']] = user['name']
        return temp_list

    def send_data(self,ip,sender,algo,msg,key):
            data = {"sender": sender ,"algorithm": algo ,"message": msg ,"key": key ,"type": "encrypt"}
            url = f'http://{ip}:3000/encrypt'
            try:
                    x = requests.post(url, json=data)
                    return x.status_code
            except:
                    return -1

    def get_gatway_ip(self):
        try:
                gateways = netifaces.gateways()
                defaults = gateways.get("default")
                return defaults[2][0]
        except:
                raise Exception('make sure you are online...')
    def req(self):
        # lv=str(self.request("sifou",True))
        # self.TextEdit_message.setText(lv)

        liste=self.request("SOUKEUR",True)
        for i in liste.keys():
            self.list_dict[liste[i]]=i

        self.comboBox.clear()
        self.comboBox.addItems(self.list_dict.keys())




    def submit(self,char):
        if (char=="01"):
            self.cesar_enc()
        if (char=="02"):
            self.veg_enc()
        if (char=="03"):
            self.sub_enc()
        if (char=="04"):
            self.trans_enc()
        if (char=="05"):
            self.des_enc()
        
        if (char=="11"):
            self.cesar_dec()
        if (char=="12"):
            self.veg_dec()
        if (char=="13"):
            self.sub_dec()
        if (char=="14"):
            self.trans_dec()
        if (char=="15"):
            self.des_dec()

        if (char=="21"):
            self.crack_veg()
        

    def car(self,char):
        self.show_popup_info('Vous devez donner le text et la clé "caractères"')
        _translate = QtCore.QCoreApplication.translate
        self.char=char
        self.TextEdit_message.setReadOnly(False)
        self.LineEdit_key.setReadOnly(False)
        self.pushButton_Submit.setEnabled(True)
        self.onlyInt = QtGui.QRegExpValidator(QtCore.QRegExp("[a-z A-Z]+"))
        self.LineEdit_key.setValidator(self.onlyInt)
        self.TextEdit_message.setPlaceholderText(_translate("MainWindow", "Vous devez mettre votre text"))
        self.LineEdit_key.setPlaceholderText(_translate("MainWindow", "Vous devez mettre une chaine de caractères"))

    def num(self,char):
        self.show_popup_info('Vous devez donner le text et la clé "numeric"')
        _translate = QtCore.QCoreApplication.translate
        self.char= char
        self.TextEdit_message.setReadOnly(False)
        self.LineEdit_key.setReadOnly(False)
        self.pushButton_Submit.setEnabled(True)
        self.onlyInt = QtGui.QIntValidator()
        self.LineEdit_key.setValidator(self.onlyInt)
        self.TextEdit_message.setPlaceholderText(_translate("MainWindow", "Vous devez mettre votre text"))
        self.LineEdit_key.setPlaceholderText(_translate("MainWindow", "Vous devez mettre une valeur"))


    def veg_enc(self):
        
        self.text = self.TextEdit_message.toPlainText()
        self.keyword = self.LineEdit_key.text()
        self.text=self.text.lower()
        print(self.text+"\n")
        print(self.keyword+"\n")
        encrypted=V.encrypt_veg(self.text,self.keyword)
        self.TextEdit_result.setText(encrypted)

    def cesar_enc(self):

        self.text = self.TextEdit_message.toPlainText()
        self.key = int(self.LineEdit_key.text())
        print(self.text+"\n")
        print(str(self.key)+"\n")
        encrypted=C.encrypt(self.text,self.key)
        self.TextEdit_result.setText(encrypted)

    def sub_enc(self):

        self.text = self.TextEdit_message.toPlainText()
        self.key = self.LineEdit_key.text()
        print(self.text+"\n")
        print(self.keyword+"\n")
        encrypted=S.encrypt_sub(self.text,self.key,self.alphabet)
        self.TextEdit_result.setText(encrypted)

    def trans_enc(self):

        self.text = self.TextEdit_message.toPlainText()
        self.key = int(self.LineEdit_key.text())
        print(self.text+"\n")
        print(str(self.key)+"\n")
        encrypted=T.encrypt_trans(self.text,self.key)
        self.TextEdit_result.setText(encrypted)

    def cesar_dec(self):
        self.text = self.TextEdit_message.toPlainText()
        self.key = int(self.LineEdit_key.text())
        print(self.text+"\n")
        print(str(self.key)+"\n")
        decrypted=C.decrypt(self.text,self.key)
        self.TextEdit_result.setText(decrypted)

    def veg_dec(self):
        self.text = self.TextEdit_message.toPlainText()
        self.text=self.text.lower()
        self.keyword = self.LineEdit_key.text()
        print(self.text+"\n")
        print(str(self.key)+"\n")
        # key=V.generateKey(self.text,self.keyword)
        decrypted=V.decrypt_veg(self.text,self.keyword)
        self.TextEdit_result.setText(decrypted)

    def sub_dec(self):
        self.text = self.TextEdit_message.toPlainText()
        self.key = self.LineEdit_key.text()
        print(self.text+"\n")
        print(self.keyword+"\n")
        encrypted=S.decrypt_sub(self.text,self.key,self.alphabet)
        self.TextEdit_result.setText(encrypted)

    def trans_dec(self):
        self.text = self.TextEdit_message.toPlainText()
        self.key = int(self.LineEdit_key.text())
        # print(self.text+"\n")
        # print(self.key+"\n")
        decrypted=T.decrypt_trans(self.text,self.key)
        self.TextEdit_result.setText(decrypted)

    def crack_veg(self):
        print("hi")
        self.text = self.TextEdit_message.toPlainText()
        self.key = int(self.LineEdit_key.text())
        print(self.text+"\n")
        print(str(self.key)+"\n")
        result= crack.crack(self.text,self.key)
        # print(result)
        intermediaire=""
        final_result=""
        for i in range(len(result)):
            intermediaire="texte : "+result[i][0]+" | clé :"+result[i][1]+"\n"
            final_result+=intermediaire
            final_result+="################################\n"
            # print("###########################")
            # print("text :",result[i][0],"| key :",result[i][1])
        self.TextEdit_result.setText(final_result)

    def des_enc(self):
        self.text = self.TextEdit_message.toPlainText()
        self.keyword = self.LineEdit_key.text()
        print(self.text+"\n")
        print(self.keyword+"\n")
        if len(self.keyword)==8:
            encrypted=DES.encrypt_des(self.text,self.keyword)
            self.TextEdit_result.setText(encrypted)
        else:
            self.show_popup_error('La longueur de la clé doit etre 8\nvous avez mis une cle de taille '+str(len(self.keyword)))

    def des_dec(self):
        self.text = self.TextEdit_message.toPlainText()
        self.keyword = self.LineEdit_key.text()
        if len(self.keyword)==8:
            print(self.text+"\n")
            print(self.keyword+"\n")
            decrypted=DES.decrypt_des(self.text,self.keyword)
            plain_text=bytearray.fromhex(decrypted).decode()
            plain_text=plain_text.replace("#","")
            self.TextEdit_result.setText(plain_text)
        else:
            self.show_popup_error('La longueur de la clé doit etre 8\nvous avez mis une cle de taille '+str(len(self.keyword)))


    def show_popup_info(self,str):
        msg = QMessageBox()
        msg.setWindowTitle("Indication")
        msg.setText(str)
        msg.setIcon(QMessageBox.Information)
        x=msg.exec_()

    def show_popup_qst(self,str):
        msg = QMessageBox()
        msg.setWindowTitle("Question")
        msg.setText(str)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # msg.buttonClicked.connect(self.btn_clicked)
        x=msg.exec_()
        if x == QMessageBox.Yes:
            print('Yes clicked',x)
            self.btn_clicked="Yes"
        if x == QMessageBox.No:
            print('No clicked',x)
            self.btn_clicked="No"

    def show_popup_error(self,str):
        msg = QMessageBox()
        msg.setWindowTitle("Erreur")
        msg.setText(str)
        msg.setIcon(QMessageBox.Critical)
        x=msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    MainWindow.show()
    sys.exit(app.exec_())
