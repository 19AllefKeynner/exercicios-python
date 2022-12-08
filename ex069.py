from datetime import date
print('-='*10)
print('\033[1;33mCADASTRE UMA PESSOA!\033[m')
print('-='*10)
hj = date.today().year
totmaior = homem = mulhernova = 0
while True:
    idade = int(input('Qual a idade dessa pessoa?'))
    if idade >= 18:
        totmaior += 1
    sexo = str(input('Qual o sexo? [M/F]')).strip().upper()[0]
    print('-' *20)
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade <20:
        mulhernova += 1
    op = str(input('\033[1;34mquer continuar? [S/N]\033[m')).strip().upper()[0]
    if op != 'S' and op != 'N':
        while True:
            op = str(input('\033[1;34mquer continuar? [S/N]\033[m')).strip().upper()[0]
            if op == 'S':
                break
            if op == 'N':
                break
    if op == 'N':
        break
print(f'\033[1;32m{totmaior} pessoa(s) tem mais de 18 anos!!!\033[m')
print(f'\033[1;32m{homem} Homen(s) foram cadastrados!!!\033[m')
print(f'\033[1;32m{mulhernova} mulhere(s) tem menos de 20 anos!!!\033m')