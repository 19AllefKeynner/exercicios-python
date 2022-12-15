from mypacote import números

n = float(input('Digite um número: '))
print(f'A metade de {n} é {números.metade(n)}!')
print(f'O dobro de {n} é {números.dobro(n)}!')
print(f'Com mais 10%, temos: {números.aumentar(n, 10)}')
print(f'Tirando 5% resta: {números.diminuir(n, 5)}')
