########################################################
#       Projeto Franguigs Interface Gráfica            #
#   Autor: Fabio Leal Schmitz                          #
#   Data Inicio: 21/06/2021                            #
#   Data Ultima Alterção: 23/06/2021                   #
########################################################

from PyQt5 import uic, QtWidgets
import sqlite3
app = QtWidgets.QApplication([])


# Característica e funções de cada elemento nas interfaces#
def propriedades_tela_franguigs():
    tela_franguigs.tableWidget.setColumnWidth(0, 60)
    tela_franguigs.tableWidget.setColumnWidth(1, 150)
    tela_franguigs.tableWidget.setColumnWidth(2, 130)
    tela_franguigs.tableWidget.setColumnWidth(3, 500)
    tela_franguigs.tableWidget.setColumnWidth(4, 130)
    tela_franguigs.tableWidget.setColumnWidth(5, 60)
    tela_franguigs.btnEstoque.clicked.connect(chama_tela_estoque)
    tela_franguigs.btnNovoPedido.clicked.connect(chama_tela_pedido)
def propriedades_tela_pedido():
    tela_pedido.btnCancelar.clicked.connect(chama_tela_franguigs)
    tela_pedido.btnCarrinho.clicked.connect(chama_tela_opcoes)
    tela_pedido.btnSalvar.clicked.connect(salvar_pedido)
def propriedades_tela_opcoes():
    tela_opcoes.btnConcluir.clicked.connect(conclui_carrinho)



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
def chama_tela_opcoes():
    tela_opcoes.show()
def conclui_carrinho():
    tela_opcoes.close()
def salvar_pedido():
    cliente = tela_pedido.lineEdit.text()
    wats = tela_pedido.lineEdit_2.text()
    prazo = tela_pedido.lineEdit_3.text()

    try:
        banco = sqlite3.connect('banco_pedidos.db')
        cursor = banco.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS pedidos (cliente text, wats text, prazo text)')
        cursor.execute("INSERT INTO pedidos VALUES ('"+cliente+"', '"+wats+"','"+prazo+"')")
        banco.commit()
        banco.close()
        print('Dados cadastrados!')
        tela_pedido.lineEdit.setText('')
        tela_pedido.lineEdit_2.setText('')
        tela_pedido.lineEdit_3.setText('')
    
    except sqlite3.Error as erro:
        print('Erro ao inserir',erro)
    
# Carregando os arquivos UI
tela_franguigs = uic.loadUi('franguigs.ui')
tela_estoque = uic.loadUi('estoque.ui')
tela_pedido = uic.loadUi('pedido.ui')
tela_opcoes = uic.loadUi('opcoes.ui')

# Chamando as propriedades de cada tela
propriedades_tela_franguigs()
propriedades_tela_pedido()
propriedades_tela_opcoes()

# Iniciando o programa
tela_franguigs.show()
app.exec()