p = float(input('qual preco do produto? R$'))
p2 = p * 5 / 100
p3 = p - p2
print('o produto que custava R${} agora com a promocao de 5% custara´ R${:.2f}'.format(p, p3))
