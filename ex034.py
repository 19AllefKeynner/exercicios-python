S = int(input('Qual seu salário?'))
if S <= 1200:
    a = S * 15 / 100
    b = a + S
    print('O salário que era de R${} passa a ser de R${:.0f}'. format(S, b))
else:
    a = S * 10 / 100
    b = a + S
    print('O salário que era de R${} passa a ser de R${:.0f}'.format(S,b))
