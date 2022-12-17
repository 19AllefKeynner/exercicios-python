from Modulos.uteis import moeda

n = float(input('Digite um número: '))
print(f'A metade de {n} é {moeda.metade(n)}!')
print(f'O dobro de {n} é {moeda.dobro(n)}!')
print(f'Com mais 10%, temos: {moeda.aumentar(n, 10)}')
print(f'Tirando 5% resta: {moeda.diminuir(n, 5)}')
