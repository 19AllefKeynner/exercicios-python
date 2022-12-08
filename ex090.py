dicionario = {'Nome':str(input('nome:')).strip().title()}
dicionario['Media'] = float(input(f'Média de {dicionario["Nome"]}:'))
dicionario['Situação'] = 'Reprovado'
if dicionario['Media'] >= 7:
    dicionario['Situação'] = 'Aprovado'
for k, v in dicionario.items():
    print(f'{k} é igual a {v}')


