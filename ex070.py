tot = barato = mil = cont = 0
qual = ''
while True:
    produto = str(input('Qual o nome do produto?')).strip().title()
    preco = float(input('Qual preço desse produto? R$'))
    tot += preco
    cont += 1
    if preco > 1000:
        mil += 1
    if cont == 1 or preco < barato:
        barato = preco
        qual = produto

    op = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if op != 'S' and op != 'N':
        while True:
            print('\033[1;31mOpção inválida, tente novamente!\033[m')
            op = str(input('quer continuar? [S/N]')).strip().upper()[0]
            if op == 'S':
                break
            if op == 'N':
                break
    if op == 'N':
        break
print(f'\033[1;34mTemos {mil} produto(s) custando mais de R$ 1000 reais!\033[m')
print(f'\033[1;34mO total foi de R$ {tot} reais!\033[m')
print(f'\033[1;34mO produto mais barato foi {qual} e custa R$ {barato} real(s)!\033[m')