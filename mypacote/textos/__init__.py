
c = ('\033[m', #Cor 0 = sem cor
     '\033[0;30;41m', #Cor 1 = Vermelho
      '\033[0;30;42m', #Cor 2 = Verde
       '\033[0;30;43m', #Cor 3 = Amarelo
        '\033[0;30;44m', #Cor 4 = Azul
         '\033[0;30;45m',) #Cor 5 = Roxo


def titulocor(msg, cor=0):
    print(c[cor],end='')
    TAM = len(msg) + 4
    print('~'*TAM)
    print(f'  {msg}')
    print('~'*TAM)
    print('\033[m')


def titulo(msg):
    TAM = len(msg) + 4
    return f'{"~"*TAM}\n  {msg}\n{"~"*TAM}'
