preço = float(input('Qual preço da sua compra?'))
print('\033[1;34m-=\033[m'*20)
print('Qual a forma de pagamento? \n [1] À vista no Dinheiro/Cheque:\n [2] À Vista no cartão:\n [3] 2x no cartão\n [4] 3x ou mais no cartão:')
print('\033[1;34m-=\033[m'*20)
op = int(input('Qual sua opção?'))
if op == 1:
    a = preço - (preço * 10 /100)
    print('O valor a pagar é de {:.2f}'.format(a))
elif op == 2:
    b = preço - (preço * 5 /100)
    print('O valor a pagar é de {:.2f}'.format(b))
elif op == 3:
     print('O valor total de sua compra é de {} SEM JUROS!'.format(preço))
     print('O valor a pagar é de {:.2f}'.format((preço/2)))
elif op == 4:
    p = int(input('Quantas parcelas vão ser?'))
    a = preço + (preço * 20 /100)
    parcela = a / p
    print('O valor total a pagar é de {}'.format(a))
    print('O valor a pagar é de {}x de {:.2f}'.format(p,parcela))
else:
    print('\033[1;31mOpção inválida!!!\033[m')