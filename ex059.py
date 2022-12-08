from time import sleep
a = int(input('\033[1;34mPrimeiro valor:\033[m'))
b = int(input('\033[1;34mSegundo valor:\033[m'))
opcao = 0
while opcao != 5:
    print('-='*10)
    print(' [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa')
    print('-=' * 10)
    opcao = int(input('Qual sua opção?'))
    if opcao == 5:
        print('\033[1;31mFechando programa em\033[m \n3...')
        sleep(1)
        print('2...')
        sleep(1)
        print('1...')
        sleep(1)
        print('\033[1;31mPrograma encerrado, volte sempre!\033[m')
        opcao == 5
    elif opcao == 1:
        print('\033[1;32mA soma de {} com {} foi {}!\033[m'.format(a,b,(a+b)))
    elif opcao == 2:
        print('\033[1;32mA multiplicação de {} x {} foi {}\033[m'.format(a,b,(a*b)))
    elif opcao == 3:
        if a < b:
            print('\033[1;32mO maior número digitado foi {}!\033[m'.format(b))
        else:
            print('\033[1;32mO maior número digitado foi {}!\033[m'.format(a))
    elif opcao == 4:
        a = int(input('\033[1;34mPrimeiro valor:\033[m'))
        b = int(input('\033[1;34mSegundo valor:\033[m'))
    else:
        print('\033[1;31mOpção inválida, tente novamente!\033[m')
    sleep(2)

