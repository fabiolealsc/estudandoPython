import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from win32api import GetSystemMetrics
from PyQt5 import QtGui

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.height = 600
        self.width = 900

        self.x = int(((GetSystemMetrics(1)) / 2) - self.height // 2) 
        self.y = int(((GetSystemMetrics(0)) / 2) - self.width // 2)
        
        self.title = 'Primeira Janela'
        
        self.textBox = QLineEdit(self)
        self.textBox.move(700, 520)
        self.textBox.resize(150, 30)

        btnBox = QPushButton('Code', self)
        btnBox.move(630, 520)
        btnBox.resize(50, 30)
        btnBox.setStyleSheet('QPushButton {background-color: rgb(150, 150, 150); font-size: 20px}')
        btnBox.clicked.connect(self.show_code)

        btn1 = QPushButton('Python', self)
        btn1.move(self.width/2 - 155, self.height - 80)
        btn1.resize(150, 50)
        btn1.setStyleSheet('QPushButton {background-color: #6065E6; font-size: 20px}')
        btn1.clicked.connect(self.btn1_click)
        
        btn2 = QPushButton('C#', self)
        btn2.move(self.width/2, self.height - 80)
        btn2.resize(150, 50)
        btn2.setStyleSheet('QPushButton {background-color: #99498F; font-size: 20px}')
        btn2.clicked.connect(self.btn2_click)
        
        self.lbl1 = QLabel('Aperte Um Botão', self)
        self.lbl1.move(self.width/2 - 200, 400)
        self.lbl1.resize(500, 60)
        self.lbl1.setStyleSheet('QLabel {font-size: 50px}')

        self.lblCode = QLabel('', self)
        self.lblCode .move(700, 200)
        self.lblCode .resize(200, 60)
        self.lblCode .setStyleSheet('QLabel {font-size: 30px}')

        self.python = QLabel(self)
        
        

        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(self.y, self.x, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def btn1_click(self):
        self.lbl1.setText('Python Selecionado!')
        self.lbl1.setStyleSheet('QLabel {color: #366B8E; font-size: 50px}')
        self.python.move(200, 10)
        self.python.setPixmap(QtGui.QPixmap('Aula01\Python.jpg'))
        self.python.resize(600, 350)
    
    def btn2_click(self):
        self.lbl1.setText('C# Selecionado!')
        self.lbl1.setStyleSheet('QLabel {color: #83368C; font-size: 50px}')
        self.python.move(300, 10)
        self.python.setPixmap(QtGui.QPixmap('Aula01\C#.png'))
        self.python.resize(600, 300)

    def show_code(self):
        code = self.textBox.text()
        self.lblCode.setText("Code: "+code)
app = QApplication(sys.argv)
w = window()
sys.exit(app.exec_())