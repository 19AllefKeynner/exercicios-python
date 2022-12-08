from time import sleep
def contador(i, f, passo):
    if passo < 0:
       passo *= -1
    if passo == 0:
        passo = 1
    print('=-'*30)
    print(f'Contagem de {i} à {f} de {passo} em {passo}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont += passo
        print('FIM')
    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM')


contador(1,10,1)
contador(10,0,2)
print('-='*30)
print('Agora é sua vez de dizer qual será nossa contagem.')
i = int(input('Inicio:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
contador(i, f, p)