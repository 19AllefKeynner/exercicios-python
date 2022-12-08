print('-='*30)
print('{}ANALIZANDO TRIÃNGULOS!{}'.format(('-=')*10, ('-=')*9))
print('-='*30)

r1 = int(input('          1º segmento:'))
r2 = int(input('          2º segmento?:'))
r3 = int(input('          3º segmento:'))
if r1 <= r2 + r3 and  r2 <= r3 + r1  and r3 <= r2 + r1:
    print('Esses segmentos formam um triângulo!')
else:
    print('Esses segmentos não podem formar um triângulo!')
print('-='*30)
print('-='*30)
