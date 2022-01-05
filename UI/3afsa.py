from PyQt5 import QtWidgets, uic ,QtGui,QtCore
import sys
import qdarkstyle
sys.path.insert(1, 'D:/Etude/BSD/TP')
import Vegenere_min as V
import Cesar as C
import Substitution as S
import Transposition as T
class Ui(QtWidgets.QMainWindow):
    
   
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('GUI.ui', self)
        self.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encoder"))
        self.label_message.setText(_translate("MainWindow", "Message"))
        self.label_key.setText(_translate("MainWindow", "Clé"))
        self.label_result.setText(_translate("MainWindow", "Résultat"))
        self.TextEdit_message.setPlaceholderText(_translate("MainWindow", "Bienvenu, vous devez choisir l\'algorithme dans le menu"))
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
        self.TextEdit_message.setReadOnly(False)
        self.LineEdit_key.setReadOnly(False)
        self.pushButton_Submit.setEnabled(True)
        self.onlyInt = QtGui.QRegExpValidator(QtCore.QRegExp("[a-z A-Z]+"))
        self.LineEdit_key.setValidator(self.onlyInt)
        self.TextEdit_message.setPlaceholderText(_translate("MainWindow", "Vous devez mettre votre text"))
        self.LineEdit_key.setPlaceholderText(_translate("MainWindow", "Vous devez mettre une chaine de caractères"))

    def num(self,char):

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
        print(self.text+"\n")
        print(self.keyword+"\n")
        deccrypted=T.decrypt_trans(self.text,self.key)
        self.TextEdit_result.setText(deccrypted)

if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        window = Ui()
        app.exec_()