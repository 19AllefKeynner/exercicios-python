from time import sleep

cont = int(input('Digite um valor: '))
while cont > -1:
    print(f"{cont}",end=' ')
    sleep(1)
    cont -= 1

print('FIM')

