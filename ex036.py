print('\033[1;34mBom dia, vamos analizar se vc está ápto a receber esse empréstimo!!!\033[m')
casa = float(input('Qual o valor da casa?'))
renda = float(input('Qual sua renda mensal?'))
ano = int(input('Em quantos anos quer parcelar?'))
parcela = casa / (ano * 12)
minimo = renda * 30 / 100
if minimo >= parcela:
    print('\033[1;34mPara pegar uma casa de R${} em {} anos a parcela será de {:.2f}\033[m'.format(casa, ano, parcela))
    print('\033[1;32mParabêns, o seu empréstimo foi aprovado!\033[m')
else:
    print('\033[1;34mPara pegar uma casa de R${} em {} anos a parcela será de {:.2f}\033[m'.format(casa, ano, parcela))
    print('\033[1;31mDesculpe, o seu empréstimo foi recusado!\033[m')
