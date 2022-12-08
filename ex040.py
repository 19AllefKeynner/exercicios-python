n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
a = (n1 + n2) /2
if a >= 7.0:
    print('\033[1;34mO aluno esta aprovado!\033[m')
elif a < 5.0:
    print('O aluno está \033[1;31mreprovado!\033[m')
elif a > 5.0 or a < 6.9:
    print('O aluno está de \033[1;31mrecuperação!\033[m')