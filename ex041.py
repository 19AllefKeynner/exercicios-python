from datetime import date
ano = int(input('Ano de nascimento:'))
a = date.today().year
b = a - ano
if b <=9:
    print('O atleta tem {} ano(s)!'.format(b))
    print('Você é um atleta \033[1;34mMIRIM\033[m')
elif b <=14:
    print('O atleta tem {} ano(s)!'.format( b))
    print('Você é um atleta \033[1;34mINFANTIL\033[m')
elif b <=19:
    print('O atleta tem {} ano(s)!'.format(b))
    print('Você é um atleta \033[1;34mJÚNIOR\033[m')
elif b <=25:
    print('O atleta tem {} ano(s)!'.format( b))
    print('Você é um atleta \033[1;34mSêNIOR\033[m')
elif b >25:
    print('O atleta tem {} ano(s)!'.format(b))
    print('Você é um atleta \033[1;34mMASTER\033[m')