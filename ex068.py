from random import randint
print('\033[1;34m-=\033[m'*14)
print('\033[1;32mVAMOS JOGAR ÍMPAR OU PAR!!!\033[m')
print('\033[1;34m-=\033[m'*14)
v = 0
while True:
   num = int(input('Digite um valor:'))
   comp = randint(0, 11)
   soma = comp + num
   opcao = ''
   while True:
      opcao = str(input('Qual sua escolha [P/I]')).strip().upper()[0]
      if opcao == 'P':
         break
      if opcao == 'I':
         break
   print(f'\033[1;34mO computador escolheu {comp}!\033[m')
   if opcao == 'P':
      if soma % 2 == 0:
         print('\033[1;32mVocê ganhou!!!\033[m')
         v += 1
      else:
         print('\033[1;31mVocê perdeu!!!\033[m')
         break
   elif opcao == 'I':
      if soma % 2 == 1:
         print('\033[1;32mVocê ganhou!!!\033[m')
         v += 1
      else:
         print('\033[1;31mVocê perdeu!!!\033[m')
         break
   print('\033[1;34mVamos jogar novamente!!!\033[m')
print(f'\033[1;31mGAME OVER,\033[m você venceu {v} vezes!')

