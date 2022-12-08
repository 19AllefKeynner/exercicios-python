pessoa=[]
media=[]
notas=[]
add=[]
cont = 0
while True:
    n = str(input('Nome:')).title()
    pessoa.append(n)
    n1 = float(input('Nota 1:'))
    add.append(n1)
    n2 = float(input('Nota 2:'))
    add.append(n2)
    notas.append(add[:])
    add.clear()
    a = (n1+n2)/2
    media.append(a)
    cont += 1
    opcao = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if opcao == 'N':
        break
print('=-'*30)
print('Nº  NOME       MÉDIA')
print('-'*30)
for c in range(0,cont):
    print(f'{c}   {pessoa[c]}',end='')
    print(f'{media[c]:>10}')
print('-'*40)
while True:
    a1 = int(input('Quer ver a nota de qual aluno? (999 interrompe) '))
    print(f'Notas de {pessoa[a1]} são {notas[a1]}!')
    print('=-'*30)
    if a1 == 999:
        break