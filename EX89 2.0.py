fixa = []
cont = 0
while True:
    nome = str(input('Seu nome:')).strip().title()
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    fixa.append([nome, [nota1, nota2], media])
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    if opcao == 'N':
        break
print('\033[1;33m=-\033[m'*40)
print('\033[1;33m[Nº   NOME        MÉDIA]\033[m')
print('\033[1;33m-\033[m'*25)
for c in range(0,cont):
    print(f'{c:>2}    {fixa[c][0]}',end=' ')
    print(f'{fixa[c][2]:>10}')
print('\033[1;33m-'*25)

while True:
    a1 = int(input('\033[1;33mQuer ver a nota de qual aluno? [999 interrompe]\033[m'))
    print(f'As notas de {fixa[a1][0]} são {fixa[a1][1]}!')
    print('\033[1;33m=-\033[m'*30)
    if a1 == 999:
        break
