expre = str(input('Digite sua expressão:'))
cont = 0
for simb in expre:
    if simb == '(':
       cont += 1
    elif simb == ')':
        cont -= 1
if cont == 0:
        print('\033[1;34mA sua expressão está correta!\033[m')
else:
        print('\033[1;31mA sua expressão está incorreta!\033[m')


