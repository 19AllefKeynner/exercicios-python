a = int(input('Primeiro número:'))
b = int(input('Segundo número:'))
c = int(input('Terceiro número:'))
Menor = a
if b<a and b<c:
    Menor = b
if c<a and c<b:
    Menor = c
print('O menor número foi: {}'.format(Menor))
Maior = a
if b>a and b>c:

    Maior = b
if c>a and c>b:
    Maior = c
print('O maior número foi: {}'.format(Maior))