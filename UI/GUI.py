# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# from _typeshed import Self
import sys
sys.path.insert(1, 'D:/Etude/BSD/TP')
import Vegenere as V
import Cesar as C
import Substitution as S
import Transposition as T
import qdarkstyle


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    text=""
    keyword=""
    result=""
    key=0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char=""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 451)
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
        self.lineEdit_message = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_message.setGeometry(QtCore.QRect(130, 29, 421, 141))
        self.lineEdit_message.setText("")
        self.lineEdit_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_message.setReadOnly(True)
        self.lineEdit_message.setObjectName("lineEdit_message")
        self.lineEdit_key = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_key.setGeometry(QtCore.QRect(130, 190, 421, 20))
        self.lineEdit_key.setReadOnly(True)
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.lineEdit_result = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_result.setGeometry(QtCore.QRect(130, 229, 421, 131))
        self.lineEdit_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_result.setReadOnly(True)
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.pushButton_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Submit.setEnabled(False)
        self.pushButton_Submit.setGeometry(QtCore.QRect(260, 370, 75, 23))
        self.pushButton_Submit.setObjectName("pushButton_Submit")
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_message.setText(_translate("MainWindow", "Message"))
        self.label_key.setText(_translate("MainWindow", "Clé"))
        self.label_result.setText(_translate("MainWindow", "Résultat"))
        self.lineEdit_message.setPlaceholderText(_translate("MainWindow", "Bienvenu, vous devez choisir l\'algorithme dans le menu"))
        self.pushButton_Submit.setText(_translate("MainWindow", "Submit"))
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

        self.pushButton_Submit.clicked.connect(lambda: self.submit(self.char))

    def submit(self,char):
        if (char=="01"):
            self.cesar_enc()
        if (char=="02"):
            self.veg_enc()
        if (char=="03"):
            self.sub_enc()
        if (char=="04"):
            self.trans_enc()
        
        if (char=="11"):
            self.cesar_dec()
        if (char=="12"):
            self.veg_dec()
        if (char=="13"):
            self.sub_dec()
        if (char=="14"):
            self.trans_dec()

    def car(self,char):

        _translate = QtCore.QCoreApplication.translate
        self.char=char
        self.lineEdit_message.setReadOnly(False)
        self.lineEdit_key.setReadOnly(False)
        self.pushButton_Submit.setEnabled(True)
        self.onlyInt = QtGui.QRegExpValidator(QtCore.QRegExp("[a-z A-Z]+"))
        self.lineEdit_key.setValidator(self.onlyInt)
        self.lineEdit_message.setPlaceholderText(_translate("MainWindow", "Vous devez mettre votre text"))
        self.lineEdit_key.setPlaceholderText(_translate("MainWindow", "Vous devez mettre une chaine de caractères"))

    def num(self,char):

        _translate = QtCore.QCoreApplication.translate
        self.char= char
        self.lineEdit_message.setReadOnly(False)
        self.lineEdit_key.setReadOnly(False)
        self.pushButton_Submit.setEnabled(True)
        self.onlyInt = QtGui.QIntValidator()
        self.lineEdit_key.setValidator(self.onlyInt)
        self.lineEdit_message.setPlaceholderText(_translate("MainWindow", "Vous devez mettre votre text"))
        self.lineEdit_key.setPlaceholderText(_translate("MainWindow", "Vous devez mettre une valeur"))


    def veg_enc(self):
        
        self.text = self.lineEdit_message.text()
        self.keyword = self.lineEdit_key.text()
        print(self.text+"\n")
        print(self.keyword+"\n")
        encrypted=V.encrypt_veg(self.text,self.keyword)
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
        # key=V.generateKey(self.text,self.keyword)
        decrypted=V.decrypt_veg(self.text,self.keyword)
        self.lineEdit_result.setText(decrypted)

    def sub_dec(self):
        self.text = self.lineEdit_message.text()
        self.key = self.lineEdit_key.text()
        print(self.text+"\n")
        print(self.keyword+"\n")
        deccrypted=S.decrypt_sub(self.text,self.key,self.alphabet)
        self.lineEdit_result.setText(deccrypted)

    def trans_dec(self):
        self.text = self.lineEdit_message.text()
        self.key = int(self.lineEdit_key.text())
        print(self.text+"\n")
        print(self.keyword+"\n")
        deccrypted=T.decrypt_trans(self.text,self.key)
        self.lineEdit_result.setText(deccrypted)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    MainWindow.show()
    sys.exit(app.exec_())
