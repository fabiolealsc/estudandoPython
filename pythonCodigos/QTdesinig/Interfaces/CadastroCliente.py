import PySimpleGUI

class TelaPython:
    def __init__(self):
        #layout
        layout = [[sg.Text('Nome:', size=(5, 0)), sg.Input(size=(25, 0), key='nome')],
                  [sg.Text('Idade:', size=(5, 0)), sg.Input(size=(25, 0), key='idade')],
                  [sg.Text('Aceita Cartão?')],
                  [sg.Radio('Sim', 'cartoes', key='aceitacartao'), sg.Radio('Não', 'cartoes', key='naoaceitacartao')],
                  [sg.Text('Quais Rede Sociais?')],
                  [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Facebook', key='facebook'), sg.Checkbox('Instagram', key='instagram')],
                  [sg.Button('Enviar Dados')]
        ]
        #janela
        janela = sg.Window('Dados do Usuário').layout(layout)
        #Extrair os dados da tela
        self.button, self.valeus = janela.Read()

    def Iniciar(self):
        nome = self.valeus['nome']
        idade = self.valeus['idade']
        tem_gmail = self.valeus['gmail']
        tem_outlook = self.valeus['outlook']
        tem_facebook = self.valeus['facebook']
        tem_instagram = self.valeus['instagram']
        aceita_cartao = self.valeus['aceitacartao']
        nao_aceita_cartao = self.valeus['naoaceitacartao']
        print(f'nome: {nome}')
        print(f'idade: {idade}')
        print(f'Tem Gmail: {tem_gmail}')
        print(f'Tem Outlook: {tem_outlook}')
        print(f'Tem Facebook: {tem_facebook}')
        print(f'Tem Instagram: {tem_instagram}')
        print(f'Aceita cartão: {aceita_cartao}')
        print(f'Não aceita cartão: {nao_aceita_cartao}')
tela = TelaPython()
tela.Iniciar()