while True:
    t = int(input('Quer saber a tabuada de qual valor?'))
    print('-'*30)
    if t <= -1:
     break
    print(f'\033[1;34mEXIBINDO RESULTADOS PRA TABUADA DE {t}\033[m')
    print('-'*30)
    for c in range(1,11):
        print(f'[{t} x {c} = {t*c}]')
    print('-' * 30)

print('\033[1;31mFIM DA TABUADA!!!\033[m')

