print('\033[1;34mSequência de Fibonancci!\033[m')
n = int(input('Quantos termos quer exibir?'))
c = 1
t1 = 0
t2 = 1
print(t1, '>', '{}'.format(t2),end=' ')
while c != n - 1:
    t3 = t1 + t2
    print('> {}'.format(t3),end=" ")
    c += 1
    t1 = t2
    t2 = t3
print('> FIM')