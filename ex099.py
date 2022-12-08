from time import sleep

def numeros(* num):
    cont = contt = 0
    maior = 0
    print(f'\nAnalizando valores passados...')
    print('-='*30)
    for v in num:
        print(f'{v}',end=', ')
        sleep(0.5)
        contt += 1
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {contt} valores ao todo.',end='')
    print(f'\nO maior valor foi {maior}.')
    print('-='*30)
    sleep(2.5)


numeros(1,3,5,8,2)
numeros(0,9,8,7,6,3)
numeros(6)
numeros()