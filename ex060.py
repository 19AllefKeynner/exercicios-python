# Usando "WHILE"
A = int(input('digite um número?'))
c = A
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=',end=' ')
    f*= c
    c -= 1
print(f)

#Usando o "FOR"
b = int(input('Qual o número?'))
g = 1
for c in range(b,0,-1):
    print('{}'.format(c),end=' ')
    print('x' if c > 1 else '=',end=' ')
    g *= c
print(g)