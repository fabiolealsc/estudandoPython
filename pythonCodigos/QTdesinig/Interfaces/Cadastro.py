import PySimpleGUI as sg


# Criar as anelas e estilos(layouts)
def janela_de_entrada():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Login: '), sg.Input(key='login')],
        [sg.Text('Senha: '), sg.Input(key='senha', password_char='*')],
        [sg.Button('Entrar'), sg.Checkbox('Salvar senha'), sg.Button('Novo Usuário')]
    ]
    return sg.Window('Janela de Entrada', layout=layout, finalize=True)


def janela_de_acesso():
    sg.theme('Reddit')
    layout = [
        [sg.Button('Novo Cliente'), sg.Button('Sair')],
        [sg.Button('Acessar Cliente')],
        [sg.Button('Produtos da Loja')]
    ]
    return sg.Window('Janela de Acesso', layout=layout, finalize=True)


# criar as janelas iniciais
janela1, janela2 = janela_de_entrada(), None


# criar looping de eventos
while True:
    window, event, values = sg.read_all_windows()
    #quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    #quando ir pra proxima janela
    if window == janela1 and event == 'Entrar':
        janela1.hide()
        janela2 = janela_de_acesso()
    #quando voltar pra anterior
# criar a logica do que vai acontecer ao clicar os botoes
