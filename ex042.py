
print('\033[1;32m-=\033[m'*30)
print('\033[1;34mANALIZANDO TRIÂNGULOS!!!\033[m')
print('\033[1;32m-=\033[m'*30)

a = int(input('Primeiro segmento:'))
b = int(input('Segundo segmento:'))
c = int(input('Terceiro segmento:'))
if a <= b + c and b <= c + a and c <= a + b:
    if a == b == c:
       print('Esse triângulo é EQUILÁTERO!')
    if a != b and b != c and c != a:
       print('Esse triângulo é ISÓSCELES')
    else:
       print('Esse triângulo é ESCALENO')
else:
    print('Esses segmentos NÃO formam um triângulo!')