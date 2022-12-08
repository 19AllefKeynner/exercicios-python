quadro = [[],[],[]]
cont = contt = j = 0
for c in range(0,9):
    a = int(input(f'Digite um número para [{j}, {contt}]'))
    if cont < 3: quadro[0].append(a)
    if cont < 6 and cont >= 3: quadro[1].append(a)
    if cont < 9 and cont >= 6: quadro[2].append(a)
    contt += 1
    cont += 1
    if cont == 3: j += 1
    if cont == 6: j += 1
    if contt == 3: contt = 0
print(f'[{quadro[0][0]:^5}] [{quadro[0][1]:^5}] [{quadro[0][2]:^5}]')
print(f'[{quadro[1][0]:^5}] [{quadro[1][1]:^5}] [{quadro[1][2]:^5}]')
print(f'[{quadro[2][0]:^5}] [{quadro[2][1]:^5}] [{quadro[2][2]:^5}]')