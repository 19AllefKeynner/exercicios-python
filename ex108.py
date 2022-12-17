from Modulos.uteis import moeda

a = float(input('Digite um valor: '))
ab = (moeda.dinheiro(a, '$'))
print(f'A metade de {ab} é {moeda.dinheiro(a=moeda.metade(a), moeda="$")}!')
print(f'O dobro de {ab} é {moeda.dinheiro(moeda.dobro(a), "$")}!')
print(f'Com mais 10%, temos: {moeda.dinheiro(moeda.aumentar(a, 10), "$")}!')
print(f'Tirando 5% resta: {moeda.dinheiro(moeda.diminuir(a, 5), "$")}!')