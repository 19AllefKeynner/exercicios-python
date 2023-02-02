#Add botão de apagar tudo e o de apagar i ultimo digito
from tkinter import *
from time import sleep
listanum = []
valor = len(listanum) - 1
def numero7():
    a = 7
    listanum.append(str(a))
    texto_calculo["text"] += "7"
def numero8():
    b = 8
    listanum.append(str(b))
    texto_calculo["text"] += "8"
def numero9():
    a = 9
    listanum.append(str(a))
    texto_calculo["text"] += "9"
def numero1():
    a = 1
    listanum.append(str(a))
    texto_calculo["text"] += "1"
def numero2():
    b = 2
    listanum.append(str(b))
    texto_calculo["text"] += "2"
def numero3():
    a = 3
    listanum.append(str(a))
    texto_calculo["text"] += "3"

def numero4():
    a = 4
    listanum.append(str(a))
    texto_calculo["text"] += "4"

def numero5():
    b = 5
    listanum.append(str(b))
    texto_calculo["text"] += "5"
def numero0():
    a = 0
    listanum.append(str(a))
    texto_calculo["text"] += "0"
def numero6():
    a = 6
    listanum.append(str(a))
    texto_calculo["text"] += "6"
def sinalmais():
    listanum.append('+')
    texto_calculo["text"] += "+"
def sinalmenos():
    listanum.append('-')
    texto_calculo["text"] += "-"
def sinaldivi():
    listanum.append('/')
    texto_calculo["text"] += "÷"
def sinalvezes():
    listanum.append('*')
    texto_calculo["text"] += "x"
def sinaldeigual():
    a = 0
    lista = []
    concat = ''
    for c in listanum:
        if c.isnumeric():
            concat += c
        else:
            lista.append(concat)
            lista.append(c)
            concat = ''

    lista.append(concat)

    total = ''
    num1 = ''
    num2 = ''
    sinal = ''
    for calc in lista:
        if calc.isnumeric():
            if num1 == '' and total == '':
                num1 = int(calc)
            else:
                num2 = int(calc)

        else:
            if sinal == '':
                sinal = calc

        if num1 != '' and num2 != '' and sinal != '':
            if total == '':
                if sinal == '+':
                    total = num1 + num2
                elif sinal == '-':
                    total = num1 - num2
                elif sinal == '/':
                    total = num1 / num2
                elif sinal == '*':
                    total = num1 * num2
            num1 = ''
            num2 = ''
            sinal = ''
        if total != '' and sinal != '' and num2 != '':
            if sinal == '+':
                total += num2
            elif sinal == '-':
                total -= num2
            elif sinal == '/':
                total = total / num2
            elif sinal == '*':
                total = total * num2
            sinal = ''
            num2 = ''
    texto_calculo["text"] = str(total)
    listanum.clear()
    listanum.append(str(total))
def botaoc():
    listanum.clear()
    texto_calculo["text"] = ''

janela = Tk()
janela.geometry("200x200")
janela.title("CALCULADOR")
botao7 = Button(janela, text="   7   ", command=numero7)
botao7.grid(column=0, row=1, padx=10, pady=10)
botao8 = Button(janela, text="   8   ", command=numero8)
botao8.grid(column=1, row=1, padx=10, pady=5)
botao9 = Button(janela, text="   9   ", command=numero9)
botao9.grid(column=2, row=1, padx=10, pady=5)
botao4 = Button(janela, text="   4   ", command=numero4)
botao4.grid(column=0, row=2, padx=10, pady=5)
botao5 = Button(janela, text="   5   ", command=numero5)
botao5.grid(column=1, row=2, padx=10, pady=5)
botao6 = Button(janela, text="   6   ", command=numero6)
botao6.grid(column=2, row=2, padx=10, pady=5)
botao1 = Button(janela, text="   1   ", command=numero1)
botao1.grid(column=0, row=3, padx=10, pady=5)
botao2 = Button(janela, text="   2   ", command=numero2)
botao2.grid(column=1, row=3, padx=10, pady=5)
botao3 = Button(janela, text="   3   ", command=numero3)
botao3.grid(column=2, row=3, padx=10, pady=5)
botao0 = Button(janela, text="   0   ", command=numero0)
botao0.grid(column=1, row=4, padx=10, pady=5)
botaosoma = Button(janela, text='+', command=sinalmais)
botaosoma.grid(column=3, row=3)
botaomenos = Button(janela, text='-', command=sinalmenos)
botaomenos.grid(column=3, row=2)
botaoihaul = Button(janela, text='=', command=sinaldeigual)
botaoihaul.grid(column=3, row=4)
botaodivi = Button(janela, text='÷',command=sinaldivi)
botaodivi.grid(column=3, row=0)
botaox = Button(janela, text='x',command=sinalvezes)
botaox.grid(column=3, row=1)
botaoc = Button(janela, text='   C   ', command=botaoc)
botaoc.grid(column=0, row=4)
botaoapagar = Button(janela, text=' [ x ] ')
botaoapagar.grid(column=2, row=4)
texto_calculo = Label(janela, text="")
texto_calculo.grid(column=1, row=0)

janela.mainloop()

