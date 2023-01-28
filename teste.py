'''listanum = ['1','2','+','2', '2', '2', '-', '2', '/', '2', '3','*','1000000000']
a = 0
lista = []
concat = ''

for c in listanum:
    if c.isnumeric():
        concat += c
    else:
        lista.append(concat)
        lista.append(c)
        concat = ''

lista.append(concat)


total = ''

num1 = ''
num2 = ''
sinal = ''
for calc in lista:
    if calc.isnumeric():
        if num1 == '' and total == '':
            num1 = int(calc)
        else:
            num2 = int(calc)

    else:
        if sinal == '':
            sinal = calc

    if num1 != '' and num2 != '' and sinal != '':
       if total == '':
           if sinal == '+':
               total = num1 + num2
           elif sinal == '-':
               total = num1 - num2
           elif sinal == '/':
               total = num1 / num2
           elif sinal == '*':
                total = num1 * num2
       num1=''
       num2=''
       sinal=''
    if total != '' and sinal != '' and num2 != '':
        if sinal == '+':
            total += num2
        elif sinal == '-':
            total -= num2
        elif sinal == '/':
            total = total / num2
        elif sinal == '*':
            total = total * num2
        sinal = ''
        num2 = ''

print(total)'''
lista = [1,1,1,1,1]
print(lista.remove())
