from datetime import datetime
a = datetime.now().year
trabalho = {'Nome': str(input('Nome:')).strip().title(),
            'Idade': int(input('Ano de nascimento:')),
            'Ctps': int(input('Carteira de trabalho: (0 não tem) '))}
nascido = trabalho['Idade']
trabalho['Idade'] = a - trabalho['Idade']
if trabalho['Ctps'] != 0:
    trabalho['Contratação'] = int(input('Ano de contratação:'))
    trabalho['Salário'] = float(input('Salário: R$'))
    trabalho['Aposentadoria'] = trabalho['Contratação'] - nascido + 35
for k, v in trabalho.items():
        print(f'- {k} tem o valor de {v}')