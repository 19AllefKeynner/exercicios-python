numeros = []
for p in range(0,5):
    n = input('Digite um número?')
    if p == 0 or n > numeros[-1]:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos,n)
                break
            pos += 1
print('=-'*20)
print(numeros)



