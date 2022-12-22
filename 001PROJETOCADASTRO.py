from time import sleep
lista = []
cont = 0

#ADD SLEEPS()
#DEIXAR O PROGRAMINHA EXCELENTE!

print('=-'*26)
print('      BANCO DE DADOS KEYNNER')
print('-='*26)
print('')
deseja = int(input(' [1] PARA SE CADASTRA\n [2] VER SEUS DADOS\n Em que podemos te ajudar hoje? '))
if deseja == 1:
    print('~'*17)
    print('  TELA DE LOGIN')
    print('~'*17)
    nome = str(input('Digite seu nome completo: ')).title()
    senha = str(input('escolha uma senha de 8 digitos: OBS-(COMECE SEMPRE COM "0" ZERO!) '))
    while len(senha) > 8:
        print('\033[1;31mErro, DIGITE UMA SENHA DE 8 DIGITOS!\033[m')
        senha = str(input('escolha uma senha de 8 digitos: OBS-(COMECE SEMPRE COM "0" ZERO!)' ))
    with open(f'0SENHAS.txt', 'w') as arquivo:
        arquivo.write((str(senha) + '\n'))
    print('')
    print('~'*19)
    print('  HORA DE GUARDAR')
    print('~'*19)
    print('')
    print('\033[1;33mEm "DIGITE SEUS DADOS: " Digite-os assim como no exemplo abaixo!\n'
          'Senha "Espaço" *******\n'
          'email "Espaço" usuario12@gmail.com\n'
          'e etc, use esse exemplo pra tudo que quiser guardar.\n'
          '(OBS: Sempre específique o que você quer guardar a < Esquerda do que está guardadando\n'
          'e não tecle "ENTER" até que tenha digitado tudo!)\n'
          '(OBS): Escreva de forma que possa entender depois, pois o computador vai registrar da forma você escrever! \033[m')
    sleep(1)
    print('')
    while True:
        dados = str(input('Digite seus dados: OBS-(ASSIM COMO NO EXEMPLO ACIMA) ')).title()
        lista.append(dados)
        opc = str(input('Quer guardar mais dados? S/N ')).upper()
        if opc == 'N':
            break

    with open(f'{senha}.txt', 'w') as arquivo:
        arquivo.write((str(nome.title()) + '\n'))
        for valor in lista:
            arquivo.write((str(lista[cont]) + '\n'))
            cont += 1
    print('\033[1;32mDados guardados com sucesso!\033[m')
    print('')
    deseja2 = str(input('Deseja ver seus dados cadastrados agora? S/N ')).upper()
    if deseja2 == 'S':
        lista = []
        print('~' * 20)
        print('  ANALIZANDO DADOS')
        print('~' * 20)
        print('')
        nome = str(input('Digite seu nome: ')).title()
        senha = str(input('Digite sua senha: '))
        LISTA = []
        with open('0SENHAS.txt', 'r') as arquivo:
            for valor in arquivo:
                LISTA.append(valor[0:len(valor) - 1])
            cont = 1
            while senha not in LISTA:
                print('\033[1;31mSENHA INCORRETA!\033[m')
                senha = str(input('Por gentileza digite sua senha: OBS-(NÃO ERRE MAIS DE 3X) '))
                cont += 1
                if cont == 3:
                    break

        if senha in LISTA:
            print('')
            print('~' * 18)
            print('  SEUS DADOS SÃO')
            print('~' * 18)
            with open(f'{senha}.txt', 'r') as arquivo:
                for valor in arquivo:
                    print(f'{valor}', end='')
                    lista.append(valor[0:len(valor) - 1])

            if nome not in lista:
                print('\n\033[1;31mATENÇÃO, esses dados não pertencem a você!\033[m')
            else:
                print(f'\033[1;32mTudo certo com seus dados senhor(a) {nome.split()[0]}')

        elif cont >= 3:
            print('\033[1;31mPROGRAMA TRAVADO!!!\033[m')
            print('\033[1;33mPor segurança seus dados estão sendo excluidos,\n agradecemos a sua compreenssão e poderá se cadastrar de novo quando quiser!')
            print('Até mais...\033[m')
    else:
        print('\n\033[1;32mOK, Volte quando quiser! ;)\033[m ')

if deseja == 2:
    lista = []
    print('~' * 20)
    print('  ANALIZANDO DADOS')
    print('~' * 20)
    print('')
    nome = str(input('Digite seu nome: ')).title()
    senha = str(input('Digite sua senha: '))
    LISTA = []
    with open('0SENHAS.txt', 'r') as arquivo:
        for valor in arquivo:
            LISTA.append(valor[0:len(valor) - 1])
        cont = 1
        while senha not in LISTA:
            print('\033[1;31mSENHA INCORRETA!\033[m')
            senha = str(input('Por gentileza digite sua senha: OBS-(NÃO ERRE MAIS DE 3X) '))
            cont += 1
            if cont == 3:
                break

    if senha in LISTA:
        print('')
        print('~' * 18)
        print('  SEUS DADOS SÃO')
        print('~' * 18)
        with open(f'{senha}.txt', 'r') as arquivo:
            for valor in arquivo:
                print(f'{valor}', end='')
                lista.append(valor[0:len(valor) - 1])

        if nome not in lista:
            print('\n\033[1;31mATENÇÃO, esses dados não pertencem a você!\033[m')
        else:
            print(f'\033[1;32mTudo certo com seus dados senhor(a) {nome.split()[0]}')

    else:
            print('\033[1;31mPROGRAMA TRAVADO!!!\033[m')
            print('\033[1;33mPor segurança seus dados estão sendo excluidos,\n agradecemos a sua compreenssão e poderá se cadastrar de novo quando quiser!')
            print('Até mais...\033[m')
else:
    print('\n\033[1;32mOK, Volte quando quiser! ;)\033[m ')

#ADD A PARTE EM QUE O USUÁRIO PODE TROCAR A SENHA CASO PRECISE
#ADD A PARTE EM QUE O USUÁRIO PODE ADICIONAR MAIS DADOS SE QUISER