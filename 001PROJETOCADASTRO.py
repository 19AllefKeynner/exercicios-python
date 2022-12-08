pessoas = []
cont = contt = 1
while True:
    print(' ')
    pessoas.append(str(input(f'\033[1;33mCadastro {cont}, Digite seu nome e idade:\033[m')).title().strip())
    cont += 1
    print('[1] Cadastrae novo aluno;\n[2] Vizualizar todos cadastros;\n[3]Vizualizar um cadastro expecífico;\n[4] Finalizar cadastros;')
    opcao = int(input('Qual sua opção?'))
    if opcao == 2:
        for obj in pessoas:
            print(' ')
            print(f'\033[1;34mCadastro {contt}\033[m')
            print(f'{obj}')
            contt += 1
    elif opcao == 3:
        print(' ')
        a = int(input(f'\033[1;33mVocê cadastrou {len(pessoas)} alunos, qual cadastro gostaria de vizualizar?\033[m'))
        print(f'\033[1;34mCadastro {a}\n\033[m{pessoas[a-1]}')
    elif opcao == 4:
        break


