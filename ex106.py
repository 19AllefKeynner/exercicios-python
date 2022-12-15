from time import sleep
c = ('\033[m', #Cor 0 = sem cor
     '\033[0;30;41m', #Cor 1 = Vermelho
      '\033[0;30;42m', #Cor 2 = Verde
       '\033[0;30;43m', #Cor 3 = Amarelo
        '\033[0;30;44m', #Cor 4 = Azul
         '\033[0;30;45m', #Cor 5 = Roxo
     )
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[3],end='')
    help(com)
    print(c[0],end='')
    sleep(2)


def titulo(msg, cor=0):
    print(c[cor],end='')
    TAM = len(msg) + 4
    print('~'*TAM)
    print(f'  {msg}')
    print('~'*TAM)
    print(c[cor],end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA pyHELP',2)
    comando = input('\033[mFunção ou biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO',1)