from random import randint
l = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'\033[1;34mOs números sorteados foram:\033[m {l}')
print(f'\033[1;34mO maior valor sorteado foi:\033[m {max(l)}')
print(f'\033[1;34mO menor valor sorteado foi:\033[m {min(l)}')
