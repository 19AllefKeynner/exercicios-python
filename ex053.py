p = str(input('DIGITE UMA PALAVRA:')).strip().upper()
palavras = p.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(p, inverso)
if inverso == junto:
    print('TEMOS UM \033[1;32mPALÍNDROMO\033[m')
else:
    print('A FRASE DIGITADA \033[1;31mNÃO É UM PALÍNDROMO\033[m')