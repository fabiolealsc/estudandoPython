########################################################
#       Projeto Franguigs Interface Gráfica            #
#   Autor: Fabio Leal Schmitz                          #
#   Data Inicio: 21/06/2021                            #
#   Data Ultima Alterção: 23/06/2021                   #
########################################################

from PyQt5 import uic, QtWidgets, QtGui 
import sqlite3
from template.settings import Settings
app = QtWidgets.QApplication([])


# Sistema de fechamento e abertura das interfaces
def chama_tela_estoque():
    tela_estoque.show()
    tela_pedido.close()

def chama_tela_pedido():
    tela_pedido.show()
    tela_estoque.close()

def chama_tela_franguigs():
    tela_pedido.close()
    tela_estoque.close()
    tela_login.close()
    tela_franguigs.show()
    Settings.carregaDados(tela_franguigs)

def chama_tela_opcoes():
    tela_opcoes.show()

def conclui_carrinho():
    tela_opcoes.close()

def verificar():
    usuario = tela_login.leUsuario.text()
    senha = tela_login.leSenha.text()

    if usuario == 'admin' and senha == 'adm':
        chama_tela_franguigs()
    else:
        tela_login.errou.setText('Senha Ou usuário Incorreto!')
        tela_login.titulo.setPixmap(QtGui.QPixmap('ProjetoFinal/icons/mascote.png'))

def salvar_pedido():
    n_pedido = tela_estoque.lineEdit_4.text()
    cliente = tela_pedido.lineEdit.text()
    wats = tela_pedido.lineEdit_2.text()
    prazo = tela_pedido.lineEdit_3.text()

    try:
        banco = sqlite3.connect('banco_pedidos.db')
        cursor = banco.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS pedidos (npedido text, cliente text, wats text, prazo text)')
        cursor.execute("INSERT INTO pedidos VALUES ('"+n_pedido+"','"+cliente+"', '"+wats+"','"+prazo+"')")
        banco.commit()
        banco.close()
        print('Dados cadastrados!')
        tela_pedido.lineEdit.setText('')
        tela_pedido.lineEdit_2.setText('')
        tela_pedido.lineEdit_3.setText('')
        tela_pedido.lineEdit_4.setText('')
    
    except sqlite3.Error as erro:
        print('Erro ao inserir',erro)


# Carregando os arquivos UI
tela_franguigs = uic.loadUi('guis/principal.ui')
tela_estoque = uic.loadUi('guis/estoque.ui')
tela_pedido = uic.loadUi('guis/novopedido.ui')
tela_opcoes = uic.loadUi('guis/itens.ui')
tela_login = uic.loadUi('guis/login.ui')

# Chamando as propriedades de cada tela
Settings.propriedades_tela_franguigs(tela_franguigs, chama_tela_estoque, chama_tela_pedido)
Settings.propriedades_tela_pedido(tela_pedido, chama_tela_franguigs, chama_tela_opcoes, salvar_pedido)
Settings.propriedades_tela_opcoes(tela_opcoes, conclui_carrinho)
Settings.propriedades_tela_login(tela_login, verificar)

# Iniciando o programa
tela_login.show()
app.exec()
