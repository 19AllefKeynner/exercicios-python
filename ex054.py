from datetime import date
a = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input('\033[1;34mQual ano de nascimento da {}ª pessoa?\033[m'.format(c)))
    b = a - ano
    if b >= 18:
        totmaior += 1
    else:
        if b < 18:
            totmenor += 1
print('\033[1;32mTemos {} pessoas maiores de idade \ne também temos {} pessoas menores de idade!\033[m'.format(totmaior,totmenor))