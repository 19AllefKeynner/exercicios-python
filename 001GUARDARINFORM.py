from time import sleep
from Modulos.uteis.textos import titulo

print(titulo('COFRE VIRTUAL'))
nome = str(input('Digite seu nome completo: '))
senha = str(input('Digite uma senha: '))
print(titulo('GUARDANDO DADOS')), print('Faça os seguinte passos...')
print('Em "DIGITE SEUS DADOS PARA GUARDAR: " Digite-os assim como no exemplo abaixo!\n'
      'Senha "Espaço" *******\n'
      'email "Espaço" usuario12@gmail.com\n'
      'e etc, use esse exemplo pra tudo que quiser guardar.\n'
      '(OBS: Sempre específique o que você quer guardar a < Esquerda do que está guardadando\n'
      'e não tecle "ENTER" até que tenha digitado tudo!)\n'
      '(OBS): min: de 2 items e max: de 10!')
dados = str(input('Digite aqui seus dados: (ATENÇÃO) '))
print('')
sleep(1)
dados1 = dados.split()
print(titulo('ANALIZANDO DADOS')), sleep(1), print('Aguarde',end=''), sleep(1), print('.',end=''), sleep(1), print('.',end=''), sleep(1), print('.',end='')
if len(dados1) >=4  and len(dados1) <= 10:
      print('\033[1;32m Tudo certo com seus dados, dados salvos com sucesso!\033[m')
else:
      print('\033[1;31m Algo deu errado tente novamente!\033[m')
      while True:
            dados = str(input('Digite aqui seus dados: (ATENÇÃO)'))
            dados1 = dados.split()
            sleep(1)
            if len(dados1) >=4 and len(dados1) <= 10:
                  print('\033[1;32m Tudo certo com seus dados, dados salvos com sucesso!\033[m')
                  break
            else:
                  print('\033[1;31m Algo deu errado tente novamente!\033[m')
lista = []
lista.append(dados1)
sleep(1)
cont = 0
pedirsenha = str(input('Digite sua senha para ver seus dados: (Três erros e seu dados serão cancelados automaticamente) '))
sleep(1)
if pedirsenha != senha:
      print('\033[1;31mSENHA INCORRETA\033[m')
      pedirsenha = str(input('Digite sua senha para ver seus dados: (Três erros e seu dados serão cancelados automaticamente) '))
if pedirsenha != senha:
      print('\033[1;31mSENHA INCORRETA\033[m')
      pedirsenha = str(input('Digite sua senha para ver seus dados: (Três erros e seu dados serão cancelados automaticamente) '))
if pedirsenha != senha:
      print('\033[1;31mSISTEMA TRAVADO, POR SEGURANÇA SEUS DADOS FORAM APAGADOS...\033[m')
      lista.clear()
      print('\033[1;31mFIM')

else:
      print(titulo('EXIBINDO DADOS SALVOS'))
      sleep(2)

      print(f'{lista[0][0]} \t{lista[0][1]}')
      print(f'{lista[0][2]} \t{lista[0][3]}')
      if len(lista) >= 3:
            print(f'{lista[0][4]} \t{lista[0][5]}')
      if len(lista) >= 4:
            print(f'{lista[0][6]} \t{lista[0][7]}')
      if len(lista) >= 5:
            print(f'{lista[0][8]} \t{lista[0][9]}')
      else:
            print('\033[1;32mFIM\033[m')

