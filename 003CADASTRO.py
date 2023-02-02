import PySimpleGUI as sg
from time import sleep
layout = [
    [sg.Text('Bem vindo ao paypague, o que deseja hoje?')],
    [sg.Button('         Entrar         '),sg.Button('         Cadastrar         ')],
]

janela = sg.Window('paypague',layout=layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == '         Entrar         ':
        layout = [
            [sg.Text('Usuário ou email:')],
            [sg.Input(key='usuario')],
            [sg.Text('Digite sua senha:')],
            [sg.Input(key=('senha'))],
            [sg.Button('Entrar')],
            [sg.Text('', key='mensagem')]
        ]

        janela = sg.Window('paypague', layout=layout)

        while True:
            eventos, valores = janela.read()
            if eventos == sg.WIN_CLOSED:
                break
            elif eventos == 'Entrar':
                usuario = valores['usuario']
                senha = valores['senha']
                listacon = []
                listacon2 = []
                conte = 0
                with open('DADOS1.txt', 'r') as arquivo3:
                    for c in arquivo3:
                        if str(c.strip()) == usuario:
                            listacon.append(conte)
                            conte = 0

                with open('DADOS1.txt', 'r') as arquivo3:
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
                    janela['mensagem'].update('Login correto!')
                else:
                    janela['mensagem'].update('Login incorreto!')
                sleep(2)
                email = valores['usuario']
                conte = 0
                lista1 = []
                lista2 = []
                with open(f'{email}.txt', 'r') as arquivo3:
                    for c in arquivo3:
                        lista2.append(c)

                layout = [
                    [sg.Text(f'{lista2[0].title()}')],
                    [sg.Text(f'R$ {lista2[1]}', key='mensagem2')],
                    [sg.Button(' VER SALDO      ')],
                    [sg.Button('OCUTAR SALDO')],
                    [sg.Button('         PIX            ')],
                    [sg.Button(' GUARDAR  ')],
                ]

                janela = sg.Window('paypague', layout=layout)

                while True:
                    eventos, valores = janela.read()
                    if eventos == sg.WIN_CLOSED:
                        break

                    if eventos == ' VER SALDO      ':
                        if len(lista1) == 0:
                            janela['mensagem2'].update(f'R$ {lista2[1]}')
                    if eventos == 'OCUTAR SALDO':
                        janela['mensagem2'].update('*****')
                        continue
                    elif eventos == '         PIX            ':
                        layout = [
                            [sg.Button('Nova transferência pix')],
                        ]
                        janela = sg.Window('paypague', layout=layout)
                        while True:
                            eventos, valores = janela.read()
                            if eventos == sg.WIN_CLOSED:
                                break
                            elif eventos == 'Nova transferência pix':
                                cont = 0
                                b = 0
                                contt = 0
                                lista4 = []
                                lista3 = []
                                lista2 = []
                                lista1 = []
                                layout = [
                                    [sg.Text('Qual valor?')],
                                    [sg.Input(key='VALOR')],
                                    [sg.Text('Chave pix')],
                                    [sg.Input(key='chavepix')],
                                    [sg.Button('Enviar pix')],
                                    [sg.Text(f'', key='mensagem')]
                                ]
                                janela = sg.Window('paypague', layout=layout)
                                while True:
                                    eventos, valores = janela.read()
                                    if eventos == sg.WIN_CLOSED:
                                        break
                                    elif eventos == 'Enviar pix':
                                        with open(f'{email}.txt', 'r') as arquivo3:
                                            for c in arquivo3:
                                                lista4.append(c)
                                        for c in lista4:
                                            if contt == 1:
                                                b += int(c)
                                            contt += 1

                                        if b >= int(valores['VALOR']):
                                            with open(f'{valores["chavepix"]}.txt', 'r') as arquivo3:
                                                for c in arquivo3:
                                                    lista2.append(c)
                                            lista1.append(valores['VALOR'])
                                            a = (int(lista2[1]) + int(lista1[0]))
                                            for c in lista2:
                                                if cont != 1:
                                                    lista3.append(c)
                                                if cont == 1:
                                                    lista3.append(a)
                                                cont += 1
                                            with open(f'{valores["chavepix"]}.txt', 'w') as arquivo4:
                                                for c in lista3:
                                                    arquivo4.write((str(c)))
                                            janela['mensagem'].update('Enviado com sucesso!')
                                        else:
                                            janela['mensagem'].update('Saldo insuficiênte!')

                                        lista1.clear()
                                        lista2.clear()
                                        lista3.clear()
                                        lista4.clear()

                                        cont = 0
                                        lista = []
                                        lista0 = []
                                        lista1a = []
                                        with open(f'{email}.txt', 'r') as arquivo3:
                                            for c in arquivo3:
                                                lista0.append(c)
                                        lista.append(valores['VALOR'])
                                        a1 = (int(lista0[1]) - int(lista[0]))
                                        for c in lista0:
                                            if cont != 1:
                                                lista1a.append(c)
                                            if cont == 1:
                                                lista1a.append(a1)
                                            cont += 1
                                        with open(f'{email}.txt', 'w') as arquivo4:
                                            for c in lista1a:
                                                arquivo4.write((str(c)))

    elif eventos == '         Cadastrar         ':
        layout = [
            [sg.Text('Digite seu nome completo:')],
            [sg.Input(key=('nome'))],
            [sg.Text('', key='mensagem3')],
            [sg.Text('Crie um email:')],
            [sg.Input(key=('email'))],
            [sg.Text('', key='mensagem1')],
            [sg.Text('Crie uma senha de 8 digitos:')],
            [sg.Input(key=('senha'))],
            [sg.Text('', key='mensagem2')],
            [sg.Button('Entrar')],
            [sg.Text('', key='mensagem')],
        ]

        janela = sg.Window('paypague', layout=layout)
        listadados = []
        cont = 0
        while True:
            eventos, valores = janela.read()
            if eventos == sg.WIN_CLOSED:
                break
            elif eventos == 'Entrar':
                email = valores['email']
                with open('DADOS1.txt', 'r') as arquivo3:
                    for c in arquivo3:
                        listadados.append(c)
                        if str(c.strip()) == email:
                            cont += 1
                        else:
                            cont = 0
                if cont >= 1:
                    janela['mensagem1'].update('Esse email já esta em uso, por favor digite outro email')
                elif cont == 0:
                    janela['mensagem1'].update('')

                senha = valores['senha']
                contee = 0
                with open('DADOS1.txt', 'r') as arquivo3:
                    for c in arquivo3:
                        listadados.append(c)
                        if str(c.strip()) == senha:
                            contee += 1
                        else:
                            contee = 0
                if contee >= 1:
                    janela['mensagem2'].update('Senha fraca')
                elif len(senha) < 8:
                    janela['mensagem2'].update('Senha muito curta')
                elif contee == 0 and cont == 0:
                    janela['mensagem2'].update('Dados cadastrados, aguarde alguns segundos!')
                with open(f'{valores["email"]}.txt', 'a') as arquivo4:
                    arquivo4.write((str(valores['nome'] + '\n')))
                    arquivo4.write((str('500')))
                with open('DADOS1.txt', 'a') as arquivo4:
                    arquivo4.write((str(valores['email'] + '\n')))
                    arquivo4.write((str(valores['senha'] + '\n')))
                sleep(2)
                email = valores['email']
                conte = 0
                lista1 = []
                lista2 = []
                with open(f'{email}.txt', 'r') as arquivo3:
                    for c in arquivo3:
                        lista2.append(c)

                layout = [
                    [sg.Text(f'{lista2[0].title()}')],
                    [sg.Text(f'R$ {lista2[1]}', key='mensagem2')],
                    [sg.Button(' VER SALDO      ')],
                    [sg.Button('OCUTAR SALDO')],
                    [sg.Button('         PIX            ')],
                    [sg.Button(' GUARDAR  ')],
                ]

                janela = sg.Window('paypague', layout=layout)

                while True:
                    eventos, valores = janela.read()
                    if eventos == sg.WIN_CLOSED:
                        break

                    if eventos == ' VER SALDO      ':
                        if len(lista1) == 0:
                            janela['mensagem2'].update(f'R$ {lista2[1]}')
                    if eventos == 'OCUTAR SALDO':
                        janela['mensagem2'].update('*****')
                        continue
                    elif eventos == '         PIX            ':
                        layout = [
                            [sg.Button('Nova transferência pix')],
                        ]
                        janela = sg.Window('paypague', layout=layout)
                        while True:
                            eventos, valores = janela.read()
                            if eventos == sg.WIN_CLOSED:
                                break
                            elif eventos == 'Nova transferência pix':
                                cont = 0
                                b = 0
                                contt = 0
                                lista4 = []
                                lista3 = []
                                lista2 = []
                                lista1 = []
                                layout = [
                                    [sg.Text('Qual valor?')],
                                    [sg.Input(key='VALOR')],
                                    [sg.Text('Chave pix')],
                                    [sg.Input(key='chavepix')],
                                    [sg.Button('Enviar pix')],
                                    [sg.Text(f'', key='mensagem')]
                                ]
                                janela = sg.Window('paypague', layout=layout)
                                while True:
                                    eventos, valores = janela.read()
                                    if eventos == sg.WIN_CLOSED:
                                        break
                                    elif eventos == 'Enviar pix':
                                        with open(f'{email}.txt', 'r') as arquivo3:
                                            for c in arquivo3:
                                                lista4.append(c)
                                        for c in lista4:
                                            if contt == 1:
                                                b += int(c)
                                            contt += 1

                                        if b >= int(valores['VALOR']):
                                            with open(f'{valores["chavepix"]}.txt', 'r') as arquivo3:
                                                for c in arquivo3:
                                                    lista2.append(c)
                                            lista1.append(valores['VALOR'])
                                            a = (int(lista2[1]) + int(lista1[0]))
                                            for c in lista2:
                                                if cont != 1:
                                                    lista3.append(c)
                                                if cont == 1:
                                                    lista3.append(a)
                                                cont += 1
                                            with open(f'{valores["chavepix"]}.txt', 'w') as arquivo4:
                                                for c in lista3:
                                                    arquivo4.write((str(c)))
                                            janela['mensagem'].update('Enviado com sucesso!')
                                        else:
                                            janela['mensagem'].update('Saldo insuficiênte!')

                                        lista1.clear()
                                        lista2.clear()
                                        lista3.clear()
                                        lista4.clear()

                                        cont = 0
                                        lista = []
                                        lista0 = []
                                        lista1a = []
                                        with open(f'{email}.txt', 'r') as arquivo3:
                                            for c in arquivo3:
                                                lista0.append(c)
                                        lista.append(valores['VALOR'])
                                        a1 = (int(lista0[1]) - int(lista[0]))
                                        for c in lista0:
                                            if cont != 1:
                                                lista1a.append(c)
                                            if cont == 1:
                                                lista1a.append(a1)
                                            cont += 1
                                        with open(f'{email}.txt', 'w') as arquivo4:
                                            for c in lista1a:
                                                arquivo4.write((str(c)))

# criar parte onde é necessário senha pra fazr o pix
#Tratar erros
