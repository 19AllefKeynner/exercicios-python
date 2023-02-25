import PySimpleGUI as sg

# Criar opção de ver a senha enquanto digita, em ambas as telas!
# Opção lembrar de me!
# Opção de esqueci a senha!
# Add imagens!

brecar = 0
while brecar < 1:
    brecar = 1
    sg.theme('DarkPurple7')
    layout = [
        [sg.Text('                         '), sg.Image(filename='avatar150.png')],
        [sg.Text('Usuário ou email:')],
        [sg.Input(key='usuario')],
        [sg.Text('')],
        [sg.Text('Digite sua senha:')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Text('')],
        [sg.Button('Entrar'), sg.Button('Cadastrar'), sg.Text('                                          '),
         sg.Button('Sair')],
        [sg.Text('', key='mensagem')],
    ]

    janela1 = sg.Window('Login', layout=layout, scaling=2)

    while True:
        eventos, valores = janela1.read()
        if eventos == sg.WIN_CLOSED:
            break
        elif eventos == 'Entrar':
            usuario = valores['usuario']
            senha = valores['senha']
            listacon = []
            listacon2 = []
            conte = 0
            with open('DADOS2.txt', 'r') as arquivo3:
                for usu in arquivo3:
                    if str(usu.strip()) == usuario:
                        listacon.append(conte)
                    conte += 1
                conte = 0

            with open('DADOS2.txt', 'r') as arquivo3:
                for c in arquivo3:
                    if str(c.strip()) == senha:
                        listacon2.append(conte)
                        break
                    conte += 1
            a = 0
            b = 0
            for c in listacon:
                a += (c)
            for c in listacon2:
                b += (c)

            if int(a) + 1 == b:
                janela1['mensagem'].update('Login correto!')
            else:
                janela1['mensagem'].update('Login incorreto!')

        elif eventos == 'Sair':
            janela1.close()
            brecar += 1

        elif eventos == 'Cadastrar':
            janela1.close()
            sg.theme('DarkPurple7')
            layout = [
                [sg.Text('                         '), sg.Image(filename='avatar150.png')],
                [sg.Text('', key='mensagem3')],
                [sg.Text('Crie um email:')],
                [sg.Input(key=('email'))],
                [sg.Text('', key='mensagem1')],
                [sg.Text('')],
                [sg.Text('Crie uma senha de 8 digitos:')],
                [sg.Input(key='senha', password_char='*')],
                [sg.Text('', key='mensagem2')],
                [sg.Text('')],
                [sg.Button('Entrar'), sg.Text('                                            '), sg.Button('Voltar'),
                 sg.Button('Sair')],
                [sg.Text('', key='mensagem')],
            ]

            janela = sg.Window('Cadastro', layout=layout, scaling=2)
            listadados = []

            while True:
                eventos, valores = janela.read()
                if eventos == sg.WIN_CLOSED:
                    janela1.close()
                    break

                elif eventos == 'Entrar':
                    contee = 0
                    cont = 0
                    email = valores['email']
                    with open('DADOS2.txt', 'r') as arquivo3:
                        for c in arquivo3:
                            listadados.append(c)
                            if str(c.strip()) == email:
                                cont += 1

                    senha = valores['senha']
                    with open('DADOS2.txt', 'r') as arquivo3:
                        for c in arquivo3:
                            listadados.append(c)
                            if str(c.strip()) == senha:
                                contee += 1

                    if cont >= 1:
                        janela['mensagem1'].update('Esse email já está em uso, por favor digite outro email')

                    if cont == 0:
                        janela['mensagem1'].update('')

                    if contee >= 1:
                        janela['mensagem2'].update('Senha fraca')

                    if contee == 0:
                        janela['mensagem2'].update('')

                    if len(senha) < 8:
                        janela['mensagem2'].update('Senha muito curta')

                    if contee == 0 and cont == 0 and len(senha) >= 8:
                        janela['mensagem2'].update('Dados cadastrados, clique em voltar e entre!')
                        with open('DADOS2.txt', 'a') as arquivo4:
                            arquivo4.write((str(valores['email'] + '\n')))
                            arquivo4.write((str(valores['senha'] + '\n')))

                    contee = 0
                    cont = 0

                elif eventos == 'Sair':
                    janela.close()

                elif eventos == 'Voltar':
                    janela.close()
                    brecar = 0
                    break
