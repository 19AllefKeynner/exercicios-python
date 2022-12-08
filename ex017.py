co = float(input('comprimento do cateto oposto?'))
ca = float(input('comprimento do cateto adiacente?'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenuza e´ {:.2f}'.format(hi))