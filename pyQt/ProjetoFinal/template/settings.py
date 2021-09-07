from PyQt5 import uic, QtWidgets, QtGui 
import sqlite3
# Característica e funções de cada elemento nas interfaces#

class Settings():
    
    def propriedades_tela_franguigs(ui,cte, ctp):
        ui.tableWidget.setColumnWidth(0, 60)
        ui.tableWidget.setColumnWidth(1, 150)
        ui.tableWidget.setColumnWidth(2, 130)
        ui.tableWidget.setColumnWidth(3, 500)
        ui.tableWidget.setColumnWidth(4, 130)
        ui.tableWidget.setColumnWidth(5, 60)
        ui.btnEstoque.clicked.connect(cte)
        ui.btnNovoPedido.clicked.connect(ctp)
        ui.label_5.setPixmap(QtGui.QPixmap('ProjetoFinal/icons/franguigs_titulo.png'))
    def carregaDados(ui):
        try:
            banco = sqlite3.connect('banco_pedidos.db')
            cur = banco.cursor()
            sqlquery = "SELECT * FROM pedidos"
            tableRow = 0
            for row in cur.execute(sqlquery):
                ui.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
                ui.tableWidget.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
                ui.tableWidget.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
                ui.tableWidget.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(row[3]))
                tableRow += 1
                print(row)
        except:
            pass

    def propriedades_tela_pedido(ui, ctf, cto, sp):
        ui.btnCancelar.clicked.connect(ctf)
        ui.btnCarrinho.clicked.connect(cto)
        ui.btnSalvar.clicked.connect(sp)
    
    def propriedades_tela_opcoes(ui, cc):
        ui.btnConcluir.clicked.connect(cc)
    
    def propriedades_tela_login(ui, ver):
        ui.btnEntrar.clicked.connect(ver)

