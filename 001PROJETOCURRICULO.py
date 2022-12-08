nome = str(input('Qual seu nome completo?')).strip().title()
nasc = str(input('Qual sua nacionalidade?')).strip().title()
estd = str(input('Qual seu estado civil?')).strip().title()
print('\033[1;34mAgora seu endereço!\033[m')
rua = str(input('Digite a rua onde mora com o número da casa:')).strip().title()
bairro = str(input('Qual o bairro?')).strip().title()
tel = int(input('Qual seu telefone?'))
print('\033[1;34mAgora formação escolar!\033[m')
form = str(input('Qual a sua formação escolar?')).strip().title()
print('\033[1;34mExperiência profissional\033[m')
opcao = 0
while opcao != 'N':
    empresa = str(input('Qual empresa ja trabalhou?')).strip().title()
    funcao = str(input('Qual foi a fução?')).strip().title()
    periodo = str(input('Qual o periodo?')).strip().title()
    cid = str(input('Em qual cidade?')).strip().title()
    opcao = str(input('\033[1;33mHá mais empresas? [S/N]\033[m')).strip().upper()
print('\033[1;34mAgora suas habilidades!\033[m')
op = 0
while op != 'N':
    hab = str(input('Cite uma habilidade:')).strip().title()
    op = str(input('\033[1;33mHá mais habilidades? [S/N]\033[m')).strip().upper()

objetivo = str(input('\033[1;34mPor fim seu objetivo:\033[m'))
