from Modulos.uteis import moeda

n = float(input('Digite um número: '))
print(f'A metade de {moeda.dinheiro(n)} é {moeda.metade(n=n, formate=True)}!')
print(f'O dobro de {moeda.dinheiro(n)} é {moeda.dobro(n, True)}!')
print(f'Com mais 10%, temos: {moeda.aumentar(n, 10, True)}')
print(f'Tirando 5% resta: {moeda.diminuir(n, 5, True)}')
