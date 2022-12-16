from mypacote import ex108

a = float(input('Digite um valor: '))
ab = (ex108.dinheiro(a,'$'))
print(f'A metade de {ab} é {ex108.dinheiro(a=ex108.metade(a),moeda="$")}!')
print(f'O dobro de {ab} é {ex108.dinheiro(ex108.dobro(a),"$")}!')
print(f'Com mais 10%, temos: {ex108.dinheiro(ex108.aumentar(a, 10),"$")}!')
print(f'Tirando 5% resta: {ex108.dinheiro(ex108.diminuir(a,5),"$")}!')