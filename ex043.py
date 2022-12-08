peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual sua altura? (m)'))
imc = peso / (altura ** 2)
print('0 IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está \033[1;31mABAIXO\033[m do peso, procure orientação médica!!!')
elif imc > 18.5 and imc <= 25:
    print('O seu peso é \033[1;32mIDEAL\033[m')
elif imc > 25 and imc <= 30:
    print('Você está com \033[1;34mSOBREPESO\033[m')
elif imc > 30 and imc <= 40:
    print('Você está com \033[1;31mOBESIDADE\033[m')
else:
    print('Vocçê está com \033[1;35mOBESIDADE MÓBICA\033[M')
