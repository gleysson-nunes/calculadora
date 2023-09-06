from customtkinter import *
from tkinter import messagebox
from math import sqrt

root = CTk()
root.geometry('428x400')
root.resizable(False, False)
root.title('Calculadora')
root.iconbitmap('icone.ico')
root.configure(fg_color='#22276E')


# Monitor
monitor = CTkEntry(root, width=410, height=80, justify='right',
                   font=('Arial', 40, 'bold'), fg_color='#4D57F7',
                   border_color='#292F85', corner_radius=10)
monitor.place(x=10, y=10)


# Função para pegar cada número clicado
def clicar_numero(numero):
    valor_atual = monitor.get()  # Pega o 1° número que está no monitor
    monitor.delete(0, END)  # Limpa o monitor do início até o final
    monitor.insert(0, str(valor_atual + str(numero)))  # Insere os números


# Função para inserir um ponto
def ponto():
    monitor.insert(END, '.')    # Insere o ponto no final


# Função para limpar o monitor
def limpar():
    monitor.delete(0, END)  # Limpa o monitor do início até o final


# Foi criada uma função para cada operação matemática
def somar():
    global primeiro_numero       # Variável que será usada na função igual()
    global operacao              # Variável que será usada na função igual()
    primeiro_numero = float(monitor.get())  # Pega o primeiro número do monitor
    operacao = 'somar'         # O valor "somar" será usado na função igual()
    monitor.delete(0, END)     # Limpa o monitor do início até o final


def subtrair():
    global primeiro_numero
    global operacao
    primeiro_numero = float(monitor.get())
    operacao = 'subtrair'
    monitor.delete(0, END)


def multiplicar():
    global primeiro_numero
    global operacao
    primeiro_numero = float(monitor.get())
    operacao = 'multiplicar'
    monitor.delete(0, END)


def dividir():
    global primeiro_numero
    global operacao
    primeiro_numero = float(monitor.get())
    operacao = 'dividir'
    monitor.delete(0, END)


def raiz_quadrada():
    global primeiro_numero
    global operacao
    primeiro_numero = float(monitor.get())
    operacao = 'raiz_quadrada'
    monitor.delete(0, END)


def potencia():
    global primeiro_numero
    global operacao
    primeiro_numero = float(monitor.get())
    operacao = 'potencia'
    monitor.delete(0, END)


# Função de igualdade com um if para cada operação matemática
def igual():
    segundo_numero = monitor.get()  # Pega o 2° número que está no monitor
    monitor.delete(0, END)  # Limpa o monitor do início até o final
    try:
        if operacao == 'somar':
            monitor.insert(0, primeiro_numero + float(segundo_numero))
        elif operacao == 'subtrair':
            monitor.insert(0, primeiro_numero - float(segundo_numero))
        elif operacao == 'multiplicar':
            monitor.insert(0, primeiro_numero * float(segundo_numero))
        elif operacao == 'dividir':
            monitor.insert(0, primeiro_numero / float(segundo_numero))
        elif operacao == 'raiz_quadrada':
            monitor.insert(0, sqrt(primeiro_numero))
        else:
            monitor.insert(0, primeiro_numero ** float(segundo_numero))
    except ValueError:
        messagebox.showwarning(title='Aviso', message='O campo deve ser '
                                                      'preenchido só com '
                                                      'números')


# 1° Filiera de botões
botao_limpar = CTkButton(root, text='c', width=95, height=50,
                         font=('Arial', 22, 'bold'), command=limpar,
                         fg_color='#006996', hover_color='#0077AB')
botao_limpar.place(x=10, y=100)

botao_potencia = CTkButton(root, text='^', width=95, height=50,
                           fg_color='#D96C21', hover_color='#FF7F27',
                           font=('Arial', 22, 'bold'), command=potencia)
botao_potencia.place(x=115, y=100)

botao_raiz_quadrada = CTkButton(root, text='√', width=95, height=50,
                                fg_color='#D96C21', hover_color='#FF7F27',
                                font=('Arial', 22, 'bold'),
                                command=raiz_quadrada)
botao_raiz_quadrada.place(x=220, y=100)

botao_divisao = CTkButton(root, text='/', width=95, height=50,
                          fg_color='#D96C21', hover_color='#FF7F27',
                          font=('Arial', 22, 'bold'), command=dividir)
botao_divisao.place(x=325, y=100)

# 2° Filiera de botões
botao_7 = CTkButton(root, text='7', width=95, height=50,
                    font=('Arial', 22, 'bold'), fg_color='#343BA8',
                    hover_color='#3E47C9',
                    command=lambda: clicar_numero(7))
botao_7.place(x=10, y=160)

botao_8 = CTkButton(root, text='8', width=95, height=50,
                    font=('Arial', 22, 'bold'), fg_color='#343BA8',
                    hover_color='#3E47C9',
                    command=lambda: clicar_numero(8))
botao_8.place(x=115, y=160)

botao_9 = CTkButton(root, text='9', width=95, height=50,
                    font=('Arial', 22, 'bold'), fg_color='#343BA8',
                    hover_color='#3E47C9',
                    command=lambda: clicar_numero(9))
botao_9.place(x=220, y=160)

botao_multiplicacao = CTkButton(root, text='x', width=95, height=50,
                                fg_color='#D96C21', hover_color='#FF7F27',
                                font=('Arial', 22, 'bold'),
                                command=multiplicar)
botao_multiplicacao.place(x=325, y=160)

# 3° Filiera de botões
botao_4 = CTkButton(root, text='4', width=95, height=50,
                    font=('Arial', 22, 'bold'), fg_color='#343BA8',
                    hover_color='#3E47C9',
                    command=lambda: clicar_numero(4))
botao_4.place(x=10, y=220)

botao_5 = CTkButton(root, text='5', width=95, height=50,
                    font=('Arial', 22, 'bold'), fg_color='#343BA8',
                    hover_color='#3E47C9',
                    command=lambda: clicar_numero(5))
botao_5.place(x=115, y=220)

botao_6 = CTkButton(root, text='6', width=95, height=50,
                    font=('Arial', 22, 'bold'), fg_color='#343BA8',
                    hover_color='#3E47C9',
                    command=lambda: clicar_numero(6))
botao_6.place(x=220, y=220)

botao_menos = CTkButton(root, text='-', width=95, height=50,
                        fg_color='#D96C21', hover_color='#FF7F27',
                        font=('Arial', 22, 'bold'), command=subtrair)
botao_menos.place(x=325, y=220)

# 4° Filiera de botões
botao_1 = CTkButton(root, text='1', width=95, height=50,
                    font=('Arial', 22, 'bold'), fg_color='#343BA8',
                    hover_color='#3E47C9',
                    command=lambda: clicar_numero(1))
botao_1.place(x=10, y=280)

botao_2 = CTkButton(root, text='2', width=95, height=50,
                    font=('Arial', 22, 'bold'), fg_color='#343BA8',
                    hover_color='#3E47C9',
                    command=lambda: clicar_numero(2))
botao_2.place(x=115, y=280)

botao_3 = CTkButton(root, text='3', width=95, height=50,
                    font=('Arial', 22, 'bold'), fg_color='#343BA8',
                    hover_color='#3E47C9',
                    command=lambda: clicar_numero(3))
botao_3.place(x=220, y=280)

botao_adicao = CTkButton(root, text='+', width=95, height=50,
                         fg_color='#D96C21', hover_color='#FF7F27',
                         font=('Arial', 22, 'bold'), command=somar)
botao_adicao.place(x=325, y=280)

# 5° Filiera de botões
botao_ponto = CTkButton(root, text='.', width=95, height=50,
                        fg_color='#D96C21', hover_color='#FF7F27',
                        font=('Arial', 22, 'bold'), command=ponto)
botao_ponto.place(x=10, y=340)

botao_0 = CTkButton(root, text='0', width=95, height=50,
                    font=('Arial', 22, 'bold'), fg_color='#343BA8',
                    hover_color='#3E47C9',
                    command=lambda: clicar_numero(0))
botao_0.place(x=115, y=340)

botao_igual = CTkButton(root, text='=', width=200, height=50,
                        fg_color='#14662B', hover_color='#156E2F',
                        font=('Arial', 22, 'bold'), command=igual)
botao_igual.place(x=220, y=340)

root.mainloop()
