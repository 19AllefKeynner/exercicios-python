maioridadehomem = 0
nomevelho = 0
soma = 0
media = 0
tot = 0
for p in range(1,5):
    print('----- {}ª pessoa! -----'.format(p))
    nome = str(input('NOME:'))
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO: [M/F]')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    else:
        if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
        if sexo in 'Ff' and idade < 20:
            tot += 1

media = soma / 4
print('\033[1;32mA média de idade do grupo é de {}\033[m'.format(media))
print('\033[1;32mO homem mais velho tem {} anos e se chama {}!\033[m'.format(maioridadehomem,nomevelho))
print('\033[1;31mAo todo são {} mulheres com menos de 20 anos!\033[m'.format(tot))
