print('\033[1;34m=-=-=-=- GERADOR DE PA -=-=-=-=\033[m')
num = int(input('Qual PRIMEIRO TERMO?'))
razao = int(input('Qual a razão?'))
termo = num
cont = 1
a = 10
while cont <=10:
    print('\033[1;32m {} \033[m'.format(termo),end='')
    print('>>' if cont < 10 else 'PAUSA',end='')
    termo += razao
    cont +=1
    # DAQUI PRA BAIXO 62!
    if cont == 11:
        d = int(input('\n Quantos termos mais quer mostrar?'))
        cont -= d
        a += d
        if d == 0:
            print('\033[1;34mProgressão finalizada com\033[m \033[1;31m{} \033[1;34mtermos!\033[m'.format(a))