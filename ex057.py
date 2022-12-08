s = str(input('Qual seu sexo? [M/F]')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('\033[1;31mResposta errada, por favor digite (M) para masculino e (F) para feminino!')).strip().upper()[0]
if s == 'M':
    s = 'Masculino'
if s == 'F':
    s = 'Feminino'
print('\033[1;32mDados para sexo {} guardados!\033[m'.format(s))