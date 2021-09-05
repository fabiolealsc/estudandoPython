from PyQt5 import uic, QtWidgets
import sqlite3


def chama_janela_1():
    janela1.label_4.setText("")
    nome_usuario = janela1.lineEdit.text()
    senha = janela1.lineEdit_2.text()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()

    try:
        cursor.execute(f"SELECT senha FROM cadastro WHERE login = '{nome_usuario}'")
        senha_bd = cursor.fetchall()
        cursor.execute(f"SELECT nome FROM cadastro WHERE login = '{nome_usuario}'")
        nome_bd = cursor.fetchall()

    except:
        print("Erro ao validar o login!")

    if senha == senha_bd[0][0]:
        janela1.close()
        janela2.show()
        janela2.label.setText(f"Bem vindo, {nome_bd[0][0]}!")
    else:
        janela1.label_4.setText("Senha ou Usuário Incorretos!")

    banco.close()


def logout():
    janela2.close()
    cadastro.close()
    janela1.show()


def abre_tela_cadastro():
    janela1.close()
    cadastro.show()


def cadastrar():
    nome = cadastro.lineEdit.text()
    login = cadastro.lineEdit_2.text()
    senha = cadastro.lineEdit_3.text()
    c_senha = cadastro.lineEdit_4.text()
    cadastro.label_2.setText('')

    if senha == c_senha:

        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text, login text, senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('" + nome + "', '" + login + "','" + senha + "')")

            banco.commit()
            banco.close()
            cadastro.label.setText('Usuario cadastrado com sucesso!')

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)

    else:
        cadastro.label_2.setText('As senhas digitadas estão diferentes!')


# Acões:
app = QtWidgets.QApplication([])
janela1 = uic.loadUi('janela-1.ui')
janela2 = uic.loadUi('janela-2.ui')
cadastro = uic.loadUi('cadastro.ui')
janela1.pushButton.clicked.connect(chama_janela_1)
janela2.pushButton.clicked.connect(logout)
janela1.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
janela1.pushButton_2.clicked.connect(abre_tela_cadastro)
cadastro.pushButton_2.clicked.connect(logout)
cadastro.pushButton.clicked.connect(cadastrar)

janela1.show()
app.exec()
