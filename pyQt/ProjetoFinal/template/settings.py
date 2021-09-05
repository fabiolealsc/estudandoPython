from PyQt5 import uic, QtWidgets, QtGui 
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
    def propriedades_tela_pedido(ui, ctf, cto, sp):
        ui.btnCancelar.clicked.connect(ctf)
        ui.btnCarrinho.clicked.connect(cto)
        ui.btnSalvar.clicked.connect(sp)
    def propriedades_tela_opcoes(ui, cc):
        ui.btnConcluir.clicked.connect(cc)
    def propriedades_tela_login(ui, ver):
        ui.btnEntrar.clicked.connect(ver)

