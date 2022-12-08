import math
angulo = float(input('digite um angulo:'))
a = math.sin(math.radians(angulo))
print('o angulo de {} tem a Seno de {:.2f}'.format(angulo,a))
b = math.cos(math.radians(angulo))
print('o angulo de {} tem a Cosseno de {:.2f}'.format(angulo,b))
c = math.tan(math.radians(angulo))
print('o angulo de {} tem a Tangente de {:.2f}'.format(angulo,c))
