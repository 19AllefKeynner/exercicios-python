print('\033[1;30m-=\033[m'*15)
print('\033[1;34m=-------Banco Keynner-------=\033[m')
print('\033[1;30m-=\033[m'*15)
num = int(input('Quanto quer sacar?'))
total = num
cedula = 50
totalced = 0
while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de {cedula} Reais!')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break
