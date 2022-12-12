
def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade == 16 or idade == 17 or idade >= 60:
        return f'Com {idade} anos, O voto é OPCIONAL! '
    elif idade >= 18:
        return f'Com {idade} anos, O voto é OBRIGATÓRIO! '
    elif idade < 16:
        return f'Com {idade} anos, O voto é INVÁLIDO! '

print('=-'*30)
a = int(input('Em que ano vc nasceu?'))
print(voto(a))