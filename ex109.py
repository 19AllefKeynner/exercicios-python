from mypacote import ex109

n = float(input('Digite um número: '))
print(f'A metade de {ex109.dinheiro(n)} é {ex109.metade(n=n,formate=True)}!')
print(f'O dobro de {ex109.dinheiro(n)} é {ex109.dobro(n,True)}!')
print(f'Com mais 10%, temos: {ex109.aumentar(n, 10, True)}')
print(f'Tirando 5% resta: {ex109.diminuir(n, 5, True)}')
