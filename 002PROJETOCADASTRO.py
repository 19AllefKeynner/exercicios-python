from time import sleep

#Deixar mais bonito!
#loop pra nn precisar!
#Validar se o email existe!


listaguardadados = []
conte = 0
contt = 0
b = 0
print('\033[1;33m='*19)
print('  PYTHON PROJETOS')
print('='*19), print('\033[m')
opcao1 = str(input('\033[1;33m [1] QUERO ME CADASTRAR\n [2] QUERO VER MEUS DADOS\n [3] QUERO ADD INFORMAÇÕES\n Em que podemos te ajudar hoje?\033[m'))
print('')
if opcao1 == '1':
    nome = str(input('\033[1;33mDigite seu primeiro nome: \033[m')).strip().title()
    if nome.isalpha() == False:
        print('\033[1;31mERRO, digite apenas seu nome!\033[m')
        while nome.isalpha() == False:
            nome = str(input('\033[1;33mDigite seu nome: ')).strip().title()
            if nome.isalpha():
                break
            else:
                print('\033[1;31mERRO, digite seu nome completo!\033[m')

    email = str(input('\033[1;33mDigite seu email: ')).strip()
    if email == '':
        print('\033[1;31mERRO, por favor digite seu email!\033[m')
        while email == '':
            email = str(input('\033[1;33mDigite seu email: ')).strip()
            if email != '':
                break
            else:
                print('\033[1;31mERRO, por favor digite seu email!\033[m')

    senha = str(input('\033[1;33mCrie uma senha de 8 digitos: ')).strip()
    if len(senha) < 8 or senha.isalnum() == False:
        print('\033[1;31mERRO, senha inválida!\033[m')
        print('\033[1;31m ATENÇÃO, use letras e números!')
        while True:
            senha = str(input('\033[1;33mCrie uma senha de 8 digitos: ')).strip()
            if len(senha) >= 8 and senha.isalnum() == False:
                break
            else:
                print('\033[1;31m ATENÇÃO, use letras e números!')
                print('\033[1;31mERRO, senha inválida!\033[m')

    with open('DADOS.txt','r') as arquivo1:
        for valor in arquivo1:
            listaguardadados.append(valor)
            conte += 1

    if len(listaguardadados) < 1:
        with open('DADOS.txt', 'a') as arquivo2:
                arquivo2.write((str(email) + '\n' ))
                arquivo2.write((str(senha) + '\n' ))
        print('\033[1;32mDados cadastrados com sucesso!\033[m')

    else:
        for item in listaguardadados:
            if item[0:len(item)-1] == email:
                contt += 1
        if contt == 1:
            print('\033[1;31mERRO, esse email já existe!\033[m')
            while True:
                conttt = 0
                email = str(input('\033[1;33mDigite outro email: ')).strip()
                for item in listaguardadados:
                    if item[0:len(item)-1] == email:
                        conttt += 1

                if conttt < 1 :
                    with open('DADOS.txt', 'a') as arquivo3:
                        arquivo3.write((str(email) + '\n'))
                        arquivo3.write((str(senha) + '\n'))
                    print('\033[1;32mDados cadastrados com sucesso!\033[m')
                    break
                else:
                    print('\033[1;31mERRO, por favor digite seu email!\033[m')
        else:
            with open('DADOS.txt', 'a') as arquivo4:
                arquivo4.write((str(email) + '\n'))
                arquivo4.write((str(senha) + '\n'))
            print('\033[1;32mDados cadastrados com sucesso!\033[m')
    sleep(2)
    print('\033[1;33m=' * 9)
    print('  LOGIN')
    print('=' * 9), print('\033[m')
    login = str(input('\033[1;33mDigite seu login para comfirmação: (É SEU EMAIL CADASTRADO) \033[m'))
    if login != email:
        while True:
            print('\033[1;31mERRO, login incorreto!\033[m')
            login = str(input('\033[1;33mDigite seu login: \033[m'))
            if login == email:
                print('\033[1;32mLogin comfirmado!\033[m')
                break

    sleep(1)
    print('')
    print('\033[1;33mAgora você quer adicionar alguns dados seus para ficar guardados?\033[m')

    verdados = str(input('\033[1;33m[1] para SIM\n[2] para NÃO\n \033[m')).strip()

    if verdados == '1':
        with open(f'{login}', 'a') as arqui4:
            arqui4.write(str(f'Senhor {nome}') + '\n')
        while True:
            dados = str(input('\033[1;33mDigite seus dados: \033[m'))
            with open(f'{login}', 'a') as arqui4:
                arqui4.write(str(dados) + '\n')
            op = str(input('\033[1;33mQuer adicionar mais dados? S/N \033[m')).strip().upper()
            if op == 'N':
                break
        print('\033[1;32mDADOS GUARDADOS!\033[m')
    if verdados == '2':
        with open(f'{login}', 'a') as arqui4:
            arqui4.write(str(f'Senhor {nome}') + '\n')
        print('\033[1;32mOK, até mais...')

elif opcao1 == '3':
    conte12 = 0
    conte11 = 0
    listaemail = []
    listasenha = []
    email = str(input('\033[1;33mDigite seu email cadastrado: \033[1;33m')).strip()
    with open('DADOS.txt', 'r') as arquivo5:
        for valor in arquivo5:
            if conte12 % 2 != 0:
                listasenha.append(valor)
            if conte12 % 2 == 0:
                listaemail.append(valor)
            conte12 += 1
    contlinha = 0
    linha = []
    for c in listaemail:
        if c.strip() == email:
            conte11 += 1
            linha.append(contlinha+1)
        contlinha += 2
    if conte11 > 0:
        correta = []
        lost = []
        lost1 = []
        senha10 = str(input('\033[1;33mDigite sua senha: \033[m')).strip()
        conter = 0
        for a in listasenha:
            for item in a:
                lost.append(item)
            for s in senha10:
                lost1.append(s)
            lost1.append('\n')
            if lost1 == lost:
                correta.append(conter + 1)
            lost1.clear()
            lost.clear()
            conter += 2
        if correta == linha:
            print('\033[1;32mTudo certo com seus dados!')
            print('')
            while True:
                dados = str(input('\033[1;33mDigite seus dados que deseja guardar: '))
                with open(f'{email}', 'a') as arqui5:
                    arqui5.write((str(dados) + '\n'))
                op = str(input('Quer adicionar mais dados? S/N ')).strip().upper()
                if op == 'N':
                    break
            print('\033[1;32mDADOS GUARDADOS!')

        else:
            while True:
                print('\033[1;31mERRO, senha inválida!\033[m')
                senha11 = str(input('\033[1;33mDigite sua senha:\033[m')).strip()
                correta = []
                conter = 0
                lost = []
                lost1 = []
                for a in listasenha:
                    for item in a:
                        lost.append(item)
                    for s in senha11:
                        lost1.append(s)
                    lost1.append('\n')
                    if lost1 == lost:
                        correta.append(conter + 1)
                    lost1.clear()
                    lost.clear()
                    conter += 2
                if correta == linha:
                    print('\033[1;32mTudo certo com seus dados!')
                    print('')

                    while True:
                        dados = str(input('\033[1;33mDigite seus dados que deseja guardar: '))
                        with open(f'{email}', 'a') as arqui75:
                            arqui75.write((str(dados) + '\n'))
                        op = str(input('Quer adicionar mais dados? S/N ')).strip().upper()
                        if op == 'N':
                            break
                    print('\033[1;32mDADOS GUARDADOS!')
                    b += 1
                if b > 0:
                    break

    else:
        while True:
            print('\033[1;31mERRO, email inválido!\033[m')
            email3 = str(input('\033[1;33mDigite outro email:\033[m')).strip()
            contlinha = 0
            linha = []
            for c in listaemail:
                if c.strip() == email3:
                    conte11 += 1
                    linha.append(contlinha + 1)
                contlinha += 2
            if conte11 > 0:
                break
        correta = []
        senha3 = str(input('\033[1;33mDigite sua senha: \033[m')).strip()
        conter = 0
        for a in listasenha:
            if str(a.strip()) == senha3:
                correta.append(conter + 2)
            conter += 2
            if correta == linha[0] + 1:
                print('\033[1;32mTudo certo com seus dados!')
                while True:
                    dados = str(input('\033[1;33mDigite seus dados que deseja guardar: '))
                    with open(f'{email3}', 'a') as arqui4:
                        arqui4.write(str(dados) + '\n')
                    op = str(input('Quer adicionar mais dados? S/N ')).strip().upper()
                    if op == 'N':
                        break
                print('\033[1;32mDADOS GUARDADOS!')

            else:
                while True:
                    print('\033[1;31mERRO, senha inválida!\033[m')
                    senha15 = str(input('\033[1;33mDigite sua senha:\033[m')).strip()
                    correta = []
                    conter = 0
                    lost = []
                    lost1 = []
                    for a in listasenha:
                        for item in a:
                            lost.append(item)
                        for s in senha15:
                            lost1.append(s)
                        lost1.append('\n')
                        if lost1 == lost:
                            correta.append(conter + 1)
                        lost1.clear()
                        lost.clear()
                        conter += 2
                        if correta == linha:
                            print('\033[1;32mTudo certo com seus dados!')
                            guardar = []
                            while True:
                                dados = str(input('\033[1;33mDigite seus dados que deseja guardar: '))
                                with open(f'{email3}', 'a') as arqui55:
                                    arqui55.write((str(dados) + '\n'))
                                op = str(input('Quer adicionar mais dados? S/N ')).strip().upper()
                                if op == 'N':
                                    break
                            print('\033[1;32mDADOS GUARDADOS!')
                            b += 1
                    if b > 0:
                        break

elif opcao1 == '2':
    conte12 = 0
    conte11 = 0
    listaemail = []
    listasenha = []
    email = str(input('\033[1;33mDigite seu email cadastrado: \033[1;33m')).strip()
    with open('DADOS.txt', 'r') as arquivo5:
        for valor in arquivo5:
            if conte12 % 2 != 0:
                listasenha.append(valor)
            if conte12 % 2 == 0:
                listaemail.append(valor)
            conte12 += 1
    contlinha = 0
    linha = []
    for c in listaemail:
        if c.strip() == email:
            conte11 += 1
            linha.append(contlinha+1)
        contlinha += 2

    if conte11 > 0:
        correta = []
        lost = []
        lost1 = []
        senha10 = str(input('\033[1;33mDigite sua senha: \033[m')).strip()
        conter = 0
        for a in listasenha:
            for item in a:
                lost.append(item)
            for s in senha10:
                lost1.append(s)
            lost1.append('\n')
            if lost1 == lost:
                correta.append(conter + 1)
            lost1.clear()
            lost.clear()
            conter += 2

        if correta == linha:
            print('\033[1;32mTudo certo com seus dados!\033[m')
            print('')
            with open(f'{email}', 'r') as arqui15:
                for valor in arqui15:
                    print(f'{valor}',end='')
            print('')
            print('\033[1;34mObrigado por usar nosso app, esperamos ter ajudado; \033[m')

        else:
            while True:
                print('\033[1;31mERRO, senha inválida!\033[m')
                senha11 = str(input('\033[1;33mDigite sua senha:\033[m')).strip()
                correta = []
                conter = 0
                lost = []
                lost1 = []
                for a in listasenha:
                    for item in a:
                        lost.append(item)
                    for s in senha11:
                        lost1.append(s)
                    lost1.append('\n')
                    if lost1 == lost:
                        correta.append(conter + 1)
                    lost1.clear()
                    lost.clear()
                    conter += 2

                if correta == linha:
                    print('\033[1;32mTudo certo com seus dados!\033[m')
                    print('')

                    with open(f'{email}', 'r') as arqui7:
                        for valor in arqui7:
                            print(f'{valor}',end='')
                    print('')
                    print('\033[1;34mObrigado por usar nosso app, esperamos ter ajudado; \033[m')
                    b += 1
                if b > 0:
                    break


    else:
        while True:
            print('\033[1;31mERRO, email inválido!\033[m')
            email3 = str(input('\033[1;33mDigite outro email:\033[m')).strip()
            contlinha = 0
            linha = []
            for c in listaemail:
                if c.strip() == email3:
                    conte11 += 1
                    linha.append(contlinha + 1)
                contlinha += 2
            if conte11 > 0:
                break
        correta = []
        senha3 = str(input('\033[1;33mDigite sua senha: \033[m')).strip()
        conter = 0
        for a in listasenha:
            if str(a.strip()) == senha3:
                correta.append(conter + 2)
            conter += 2
            if correta == linha[0]+1:
                print('\033[1;32mTudo certo com seus dados!\033[m')
                sleep(2)
                print('')
                with open(f'{email3}', 'r') as arqui1:
                    for valor in arqui1:
                        print(f'{valor}',end='')
                print('')
                print('\033[1;34mObrigado por usar nosso app, esperamos ter ajudado; \033[m')

            else:
                while True:
                    print('\033[1;31mERRO, senha inválida!\033[m')
                    senha15 = str(input('\033[1;33mDigite sua senha:\033[m')).strip()
                    correta = []
                    conter = 0
                    lost = []
                    lost1 = []
                    for a in listasenha:
                        for item in a:
                            lost.append(item)
                        for s in senha15:
                            lost1.append(s)
                        lost1.append('\n')
                        if lost1 == lost:
                            correta.append(conter + 1)
                        lost1.clear()
                        lost.clear()
                        conter += 2

                        if correta == linha:
                            print('\033[1;32mTudo certo com seus dados!\033[m')
                            sleep(2)
                            print('')
                            with open(f'{email3}', 'r') as arqui5:
                                for valor in arqui5:
                                    print(f'{valor}',end='')
                                    print('')
                            print('\033[1;34mObrigado por usar nosso app, esperamos ter ajudado; \033[m')
                            b += 1
                    if b > 0:
                        break

else:
    print('\033[1;31mERRO, opção inválida!')
    while True:
        opcao1 = str(input('\033[1;33m Digite apenas [1], [2] ou [3]; Como podemos te ajudar hoje?\033[m'))
        print('')
        if opcao1 == '1' or opcao1 == '2' or opcao1 == '3':
            break
        else:
            print('\033[1;31mERRO, por favor digite seu email!\033[m')
    if opcao1 == '1':
        nome = str(input('\033[1;33mDigite seu primeiro nome: \033[m')).strip().title()
        if nome.isalpha() == False:
            print('\033[1;31mERRO, digite apenas seu nome!\033[m')
            while nome.isalpha() == False:
                nome = str(input('\033[1;33mDigite seu nome: ')).strip().title()
                if nome.isalpha():
                    break
                else:
                    print('\033[1;31mERRO, digite seu nome completo!\033[m')

        email = str(input('\033[1;33mDigite seu email: ')).strip()
        if email == '':
            print('\033[1;31mERRO, por favor digite seu email!\033[m')
            while email == '':
                email = str(input('\033[1;33mDigite seu email: ')).strip()
                if email != '':
                    break
                else:
                    print('\033[1;31mERRO, por favor digite seu email!\033[m')

        senha = str(input('\033[1;33mCrie uma senha de 8 digitos: ')).strip()
        if len(senha) < 8:
            print('\033[1;31mERRO, senha inválida!\033[m')
            while len(senha) < 8:
                senha = str(input('\033[1;33mCrie uma senha de 8 digitos: ')).strip()
                if len(senha) >= 8:
                    break
                else:
                    print('\033[1;31mERRO, senha inválida!\033[m')

        with open('DADOS.txt', 'r') as arquivo1:
            for valor in arquivo1:
                listaguardadados.append(valor)
                conte += 1

        if len(listaguardadados) < 1:
            with open('DADOS.txt', 'a') as arquivo2:
                arquivo2.write((str(email) + '\n'))
                arquivo2.write((str(senha) + '\n'))
            print('\033[1;32mDados cadastrados com sucesso!\033[m')

        else:
            for item in listaguardadados:
                if item[0:len(item) - 1] == email:
                    contt += 1
            if contt == 1:
                print('\033[1;31mERRO, esse email já existe!\033[m')
                while True:
                    conttt = 0
                    email = str(input('\033[1;33mDigite outro email: ')).strip()
                    for item in listaguardadados:
                        if item[0:len(item) - 1] == email:
                            conttt += 1

                    if conttt < 1:
                        with open('DADOS.txt', 'a') as arquivo3:
                            arquivo3.write((str(email) + '\n'))
                            arquivo3.write((str(senha) + '\n'))
                        print('\033[1;32mDados cadastrados com sucesso!\033[m')
                        break
                    else:
                        print('\033[1;31mERRO, por favor digite seu email!\033[m')
            else:
                with open('DADOS.txt', 'a') as arquivo4:
                    arquivo4.write((str(email) + '\n'))
                    arquivo4.write((str(senha) + '\n'))
                print('\033[1;32mDados cadastrados com sucesso!\033[m')
        sleep(2)
        print('\033[1;33m=' * 9)
        print('  LOGIN')
        print('=' * 9), print('\033[m')
        login = str(input('\033[1;33mDigite seu login para comfirmação: (É SEU EMAIL CADASTRADO) \033[m'))
        if login != email:
            while True:
                print('\033[1;31mERRO, login incorreto!\033[m')
                login = str(input('\033[1;33mDigite seu login: \033[m'))
                if login == email:
                    print('\033[1;32mLogin comfirmado!\033[m')
                    break

        sleep(1)
        print('')
        print('\033[1;33mAgora você quer adicionar alguns dados seus para ficar guardados?\033[m')

        verdados = str(input('\033[1;33m[1] para SIM\n[2] para NÃO\n \033[m')).strip()

        if verdados == '1':
            with open(f'{login}', 'a') as arqui4:
                arqui4.write(str(nome) + '\n')
            while True:
                dados = str(input('\033[1;33mDigite seus dados: \033[m'))
                with open(f'{login}', 'a') as arqui4:
                    arqui4.write(str(dados) + '\n')
                op = str(input('\033[1;33mQuer adicionar mais dados? S/N \033[m')).strip().upper()
                if op == 'N':
                    break
            print('\033[1;32mDADOS GUARDADOS!\033[m')
        if verdados == '2':
            with open(f'{login}', 'a') as arqui4:
                arqui4.write(str(nome) + '\n')
            print('\033[1;32mOK, até mais...')

    elif opcao1 == '3':
        conte12 = 0
        conte11 = 0
        listaemail = []
        listasenha = []
        email = str(input('\033[1;33mDigite seu email cadastrado: \033[1;33m')).strip()
        with open('DADOS.txt', 'r') as arquivo5:
            for valor in arquivo5:
                if conte12 % 2 != 0:
                    listasenha.append(valor)
                if conte12 % 2 == 0:
                    listaemail.append(valor)
                conte12 += 1
        contlinha = 0
        linha = []
        for c in listaemail:
            if c.strip() == email:
                conte11 += 1
                linha.append(contlinha + 1)
            contlinha += 2
        if conte11 > 0:
            correta = []
            lost = []
            lost1 = []
            senha10 = str(input('\033[1;33mDigite sua senha: \033[m')).strip()
            conter = 0
            for a in listasenha:
                for item in a:
                    lost.append(item)
                for s in senha10:
                    lost1.append(s)
                lost1.append('\n')
                if lost1 == lost:
                    correta.append(conter + 1)
                lost1.clear()
                lost.clear()
                conter += 2
            if correta == linha:
                print('\033[1;32mTudo certo com seus dados!')
                print('')
                while True:
                    dados = str(input('\033[1;33mDigite seus dados que deseja guardar: '))
                    with open(f'{email}', 'a') as arqui5:
                        arqui5.write((str(dados) + '\n'))
                    op = str(input('Quer adicionar mais dados? S/N ')).strip().upper()
                    if op == 'N':
                        break
                print('\033[1;32mDADOS GUARDADOS!')

            else:
                while True:
                    print('\033[1;31mERRO, senha inválida!\033[m')
                    senha11 = str(input('\033[1;33mDigite sua senha:\033[m')).strip()
                    correta = []
                    conter = 0
                    lost = []
                    lost1 = []
                    for a in listasenha:
                        for item in a:
                            lost.append(item)
                        for s in senha11:
                            lost1.append(s)
                        lost1.append('\n')
                        if lost1 == lost:
                            correta.append(conter + 1)
                        lost1.clear()
                        lost.clear()
                        conter += 2
                    if correta == linha:
                        print('\033[1;32mTudo certo com seus dados!')
                        print('')

                        while True:
                            dados = str(input('\033[1;33mDigite seus dados que deseja guardar: '))
                            with open(f'{email}', 'a') as arqui75:
                                arqui75.write((str(dados) + '\n'))
                            op = str(input('Quer adicionar mais dados? S/N ')).strip().upper()
                            if op == 'N':
                                break
                        print('\033[1;32mDADOS GUARDADOS!')
                        b += 1
                    if b > 0:
                        break

        else:
            while True:
                print('\033[1;31mERRO, email inválido!\033[m')
                email3 = str(input('\033[1;33mDigite outro email:\033[m')).strip()
                contlinha = 0
                linha = []
                for c in listaemail:
                    if c.strip() == email3:
                        conte11 += 1
                        linha.append(contlinha + 1)
                    contlinha += 2
                if conte11 > 0:
                    break
            correta = []
            senha3 = str(input('\033[1;33mDigite sua senha: \033[m')).strip()
            conter = 0
            for a in listasenha:
                if str(a.strip()) == senha3:
                    correta.append(conter + 2)
                conter += 2
                if correta == linha[0] + 1:
                    print('\033[1;32mTudo certo com seus dados!')
                    while True:
                        dados = str(input('\033[1;33mDigite seus dados que deseja guardar: '))
                        with open(f'{email3}', 'a') as arqui4:
                            arqui4.write(str(dados) + '\n')
                        op = str(input('Quer adicionar mais dados? S/N ')).strip().upper()
                        if op == 'N':
                            break
                    print('\033[1;32mDADOS GUARDADOS!')

                else:
                    while True:
                        print('\033[1;31mERRO, senha inválida!\033[m')
                        senha15 = str(input('\033[1;33mDigite sua senha:\033[m')).strip()
                        correta = []
                        conter = 0
                        lost = []
                        lost1 = []
                        for a in listasenha:
                            for item in a:
                                lost.append(item)
                            for s in senha15:
                                lost1.append(s)
                            lost1.append('\n')
                            if lost1 == lost:
                                correta.append(conter + 1)
                            lost1.clear()
                            lost.clear()
                            conter += 2
                            if correta == linha:
                                print('\033[1;32mTudo certo com seus dados!')
                                guardar = []
                                while True:
                                    dados = str(input('\033[1;33mDigite seus dados que deseja guardar: '))
                                    with open(f'{email3}', 'a') as arqui55:
                                        arqui55.write((str(dados) + '\n'))
                                    op = str(input('Quer adicionar mais dados? S/N ')).strip().upper()
                                    if op == 'N':
                                        break
                                print('\033[1;32mDADOS GUARDADOS!')
                                b += 1
                        if b > 0:
                            break

    elif opcao1 == '2':
        conte12 = 0
        conte11 = 0
        listaemail = []
        listasenha = []
        email = str(input('\033[1;33mDigite seu email cadastrado: \033[1;33m')).strip()
        with open('DADOS.txt', 'r') as arquivo5:
            for valor in arquivo5:
                if conte12 % 2 != 0:
                    listasenha.append(valor)
                if conte12 % 2 == 0:
                    listaemail.append(valor)
                conte12 += 1
        contlinha = 0
        linha = []
        for c in listaemail:
            if c.strip() == email:
                conte11 += 1
                linha.append(contlinha + 1)
            contlinha += 2

        if conte11 > 0:
            correta = []
            lost = []
            lost1 = []
            senha10 = str(input('\033[1;33mDigite sua senha: \033[m')).strip()
            conter = 0
            for a in listasenha:
                for item in a:
                    lost.append(item)
                for s in senha10:
                    lost1.append(s)
                lost1.append('\n')
                if lost1 == lost:
                    correta.append(conter + 1)
                lost1.clear()
                lost.clear()
                conter += 2

            if correta == linha:
                print('\033[1;32mTudo certo com seus dados!\033[m')
                print('')
                with open(f'{email}', 'r') as arqui15:
                    for valor in arqui15:
                        print(f'{valor}', end='')
                print('')
                print('\033[1;34mObrigado por usar nosso app, esperamos ter ajudado; \033[m')

            else:
                while True:
                    print('\033[1;31mERRO, senha inválida!\033[m')
                    senha11 = str(input('\033[1;33mDigite sua senha:\033[m')).strip()
                    correta = []
                    conter = 0
                    lost = []
                    lost1 = []
                    for a in listasenha:
                        for item in a:
                            lost.append(item)
                        for s in senha11:
                            lost1.append(s)
                        lost1.append('\n')
                        if lost1 == lost:
                            correta.append(conter + 1)
                        lost1.clear()
                        lost.clear()
                        conter += 2

                    if correta == linha:
                        print('\033[1;32mTudo certo com seus dados!\033[m')
                        print('')

                        with open(f'{email}', 'r') as arqui7:
                            for valor in arqui7:
                                print(f'{valor}', end='')
                        print('')
                        print('\033[1;34mObrigado por usar nosso app, esperamos ter ajudado; \033[m')
                        b += 1
                    if b > 0:
                        break


        else:
            while True:
                print('\033[1;31mERRO, email inválido!\033[m')
                email3 = str(input('\033[1;33mDigite outro email:\033[m')).strip()
                contlinha = 0
                linha = []
                for c in listaemail:
                    if c.strip() == email3:
                        conte11 += 1
                        linha.append(contlinha + 1)
                    contlinha += 2
                if conte11 > 0:
                    break
            correta = []
            senha3 = str(input('\033[1;33mDigite sua senha: \033[m')).strip()
            conter = 0
            for a in listasenha:
                if str(a.strip()) == senha3:
                    correta.append(conter + 2)
                conter += 2
                if correta == linha[0] + 1:
                    print('\033[1;32mTudo certo com seus dados!\033[m')
                    sleep(2)
                    print('')
                    with open(f'{email3}', 'r') as arqui1:
                        for valor in arqui1:
                            print(f'{valor}', end='')
                    print('')
                    print('\033[1;34mObrigado por usar nosso app, esperamos ter ajudado; \033[m')

                else:
                    while True:
                        print('\033[1;31mERRO, senha inválida!\033[m')
                        senha15 = str(input('\033[1;33mDigite sua senha:\033[m')).strip()
                        correta = []
                        conter = 0
                        lost = []
                        lost1 = []
                        for a in listasenha:
                            for item in a:
                                lost.append(item)
                            for s in senha15:
                                lost1.append(s)
                            lost1.append('\n')
                            if lost1 == lost:
                                correta.append(conter + 1)
                            lost1.clear()
                            lost.clear()
                            conter += 2

                            if correta == linha:
                                print('\033[1;32mTudo certo com seus dados!\033[m')
                                sleep(2)
                                print('')
                                with open(f'{email3}', 'r') as arqui5:
                                    for valor in arqui5:
                                        print(f'{valor}', end='')
                                        print('')
                                print('\033[1;34mObrigado por usar nosso app, esperamos ter ajudado; \033[m')
                                b += 1
                        if b > 0:
                            break
