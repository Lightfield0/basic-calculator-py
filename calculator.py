import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,700)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayi 1>> ')
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayı 2>> ')
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('+')
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.calc)
        
        self.btn_cıkar = QtWidgets.QPushButton(self)
        self.btn_cıkar.setText('-')
        self.btn_cıkar.move(150,170)
        self.btn_cıkar.clicked.connect(self.calc)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText('x')
        self.btn_carp.move(150,210)
        self.btn_carp.clicked.connect(self.calc)
        
        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText('/')
        self.btn_bol.move(150,250)
        self.btn_bol.clicked.connect(self.calc)

        self.btn_pow = QtWidgets.QPushButton(self)
        self.btn_pow.setText('**')
        self.btn_pow.move(150,290)
        self.btn_pow.clicked.connect(self.calc)
        
        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText('Sonuç>> ')
        self.lbl_sonuc.move(150,340)

    def calc(self):
        sender = self.sender().text()
        result = 0

        if sender == '+':
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender == '-':
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender == 'x':
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender == '/':
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        elif sender == '**':
            result = int(self.txt_sayi1.text()) ** int(self.txt_sayi2.text())    
        
        self.lbl_sonuc.setText('sonuç: '+ str(result))


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())


app()