from PyQt5 import uic, QtWidgets
import sqlite3



def cadastrar():
    codigo = formulario.lineEdit.text()
    descricao = formulario.lineEdit_2.text()
    preco = formulario.lineEdit_3.text()
    categoria = ""
    if formulario.radioButton.isChecked():
        categoria = "Alimento"
    elif formulario.radioButton_2.isChecked():
        categoria = "Eletrônico"
    elif formulario.radioButton_3.isChecked():
        categoria = "Eletrodomestico"
    elif formulario.radioButton_4.isChecked():
        categoria = "Informática"
    elif formulario.radioButton_5.isChecked():
        categoria = "Roupa"
    try:
        banco = sqlite3.connect('banco.bd.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS produtos (codigo int, descricao text, preco int, categoria text)")
        cursor.execute("INSERT INTO produtos VALUES ('"+codigo+"', '"+descricao+"', '"+preco+"', '"+categoria+"')")

        banco.commit()
        banco.close()
        formulario.label_6.setText('Produto cadastrado com sucesso!')
    except sqlite3.Error as erro:
        print("Erro ao cadastrar: ", erro)


def lista():
    banco = sqlite3.connect('banco.bd.db')
    cursor = banco.cursor().execute(f'SELECT preco FROM produtos')
    dados = cursor.fetchall()
    banco.close()
    formulario.close()
    listaui.show()
    print(dados)
    listaui.listView.connect = dados


app = QtWidgets.QApplication([])
formulario = uic.loadUi('formulario.ui')
listaui = uic.loadUi('lista.ui')

formulario.pushButton.clicked.connect(cadastrar)
formulario.pushButton_2.clicked.connect(lista)
formulario.show()
app.exec()
