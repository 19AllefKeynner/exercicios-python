from datetime import date
idade = int(input('Qual sua data de nascimento?'))
f = date.today().year
a = (f-idade)
if a >18:
    b = (a - 18)
    c = (f - b)
    print('Quem nasceu em {} tem {} anos'.format(idade,a))
    print('\033[1;31mVocê ja deveria ter se alistado há {} anos\033[m'.format(b))
    print('Seu alistamento foi em {}!'.format(c))
elif a <18:
    d = (18 - a)
    e = (f + d)
    print('Quem nasceu em {} tem {} anos!'.format(idade,a))
    print('\033[1;34mFaltam {} anos para seu alistamento!\033[m'.format(d))
    print('Seu alistamento vai ser em {}!'.format(e))
elif a == 18:
    print('Quem nasceu em {} tem {} anos!'.format(idade, a))
    print('\033[1;32mO seu alistamento é esse ano, não perca tempo!!!\033[m')