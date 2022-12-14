def nota(*num, show=False):
    ficha = {}
    ficha['total'] =  len(num)
    ficha['media'] = sum(num) / len(num)
    ficha['maior'] = max(num)
    ficha['menor'] = min(num)
    if ficha['media'] >= 7:
        situacao = "Boa"
    elif ficha['media'] >= 5:
        situacao = "Razoavel"
    else:
        situacao = "Ruim"
    if show == True:
        ficha['Situação'] = situacao
    return ficha


a = nota(15, 12, show=True)
print(a)
