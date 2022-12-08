list = []
tot = totid = 0
while True:
    dic = {'Nome' :str(input('Nome: ')).strip().title(),'Sexo' : 'M' ,'Idade' :int(input('Idade: '))}
    sexo = dic['Sexo'] = str(input('Sexo: ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        print('\033[1;31mERRO!\033[m Por favor, digite M ou F')
        sexo = dic['Sexo'] = str(input('Sexo: ')).strip().upper()
    list.append(dic)
    opc = str(input('Quer continur? S/N')).strip().upper()
    while opc != 'S' and opc != 'N':
        print('\033[1;31mERRO!\033[m Por favor, digite S ou N')
        opc = str(input('Quer continur? S/N')).strip().upper()
    tot += 1
    if opc == 'N':
        break
contt = 0
for c in list:
    totid += list[contt]['Idade']
    contt += 1
media = totid / tot
print('-='*30)
print(f'A) Ao todo foram {tot} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print('C) As mulheres cadastradas foram: ',end='')
cont = 0
for c in list:
    if c['Sexo'] == 'F':
        print(f'{list[cont]["Nome"]}',end='...')
    cont += 1
print('\nD) Lista de pessoas acima da média:')
con = 0
for c in list:
    if c['Idade'] > media:
        print(f'Nome = {list[con]["Nome"]}; Sexo = {list[con]["Sexo"]}; Idade = {list[con]["Idade"]}')
    con += 1
print('<<<ENCERRADO>>>')