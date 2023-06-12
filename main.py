# Importando tkinter
from tkinter import *
from tkinter import ttk

# cores
cor1 = "#363434"  # Preto = Fundo
cor2 = "#fcfafa"  # Branco = Tela
cor3 = "#031c96"  # Azul = Igual
cor4 = "#494a4d"  # Cinza = Números
cor5 = "#f57b2f"  # Laranja = Apagar, Dividir, Vezes, Subtração e Soma


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

# Criando Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_button = Frame(janela, width=235, height=268)
frame_button.grid(row=1, column=0)

#Variavel todos Valores
todos_valores = ""
valor_text = StringVar()

# Criando Funções
def entrada_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    #Passando valor para Tela
    valor_text.set(todos_valores)

# Função para calcular
def calcular():
    resultado = eval(todos_valores)
    valor_text.set(str(resultado))

# Função Limpar
def clear():
    global todos_valores
    todos_valores = ""
    valor_text.set("")

# Função Apagar
def apagar():
    global todos_valores

    if todos_valores:
        todos_valores = todos_valores[:-1]  # Remover o último caractere
        valor_text.set(todos_valores)

# Função porcentagem
def porcentagem():
    global todos_valores

    # Verificar se todos_valores é um número
    if todos_valores.isdigit():
        porcentagem = float(todos_valores)
        calculo = porcentagem - (porcentagem * 5 / 100)
        todos_valores = str(calculo)
        valor_text.set(todos_valores)


#Criando Label
app_label = Label(frame_tela, textvariable=valor_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 17 bold'), bg=cor2, fg=cor1)
app_label.place(x=0, y=0)

# Criando os Botões
# Linha 1
b_1 = Button(frame_button, command=apagar, text="C", width=11, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # Limpar
b_1.place(x=5, y=0)
b_2 = Button(frame_button, command=porcentagem, text="%", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # Porcentagem
b_2.place(x=117, y=0)
b_3 = Button(frame_button, command=clear, text="DEL", width=5, height=2, bg=cor5, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # Apagar
b_3.place(x=175, y=0)
# Linha 2
b_4 = Button(frame_button, command=lambda: entrada_valores("7"), text="7", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # N7
b_4.place(x=4, y=52)
b_5 = Button(frame_button, command=lambda: entrada_valores("8"), text="8", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # N8
b_5.place(x=60, y=52)
b_6 = Button(frame_button, command=lambda: entrada_valores("9"), text="9", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # N9
b_6.place(x=117, y=52)
b_7 = Button(frame_button, command=lambda: entrada_valores("/"), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # DIVIDIR
b_7.place(x=175, y=52)
# Linha 3
b_8 = Button(frame_button, command=lambda: entrada_valores("4"), text="4", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # N4
b_8.place(x=4, y=104)
b_9 = Button(frame_button, command=lambda: entrada_valores("5"), text="5", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # N5
b_9.place(x=60, y=104)
b_10 = Button(frame_button, command=lambda: entrada_valores("6"), text="6", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # N6
b_10.place(x=117, y=104)
b_11 = Button(frame_button, command=lambda: entrada_valores("*"), text="X", width=5, height=2, bg=cor5, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # Vezes X
b_11.place(x=175, y=104)
# Linha 4
b_12 = Button(frame_button, command=lambda: entrada_valores("1"), text="1", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # N1
b_12.place(x=4, y=156)
b_13 = Button(frame_button, command=lambda: entrada_valores("2"), text="2", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # N2
b_13.place(x=60, y=156)
b_14 = Button(frame_button, command=lambda: entrada_valores("3"), text="3", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # N3
b_14.place(x=117, y=156)
b_15 = Button(frame_button, command=lambda: entrada_valores("-"), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # Subtração
b_15.place(x=175, y=156)
# Linha 5
b_16 = Button(frame_button, command=lambda: entrada_valores("0"), text="0", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # N0
b_16.place(x=4, y=208)
b_17 = Button(frame_button, command=lambda: entrada_valores("."), text=".", width=5, height=2, bg=cor4, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # Ponto e/ou Vírgula
b_17.place(x=60, y=208)
b_18 = Button(frame_button, command=calcular, text="=", width=5, height=2, bg=cor3, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # Igual
b_18.place(x=117, y=208)
b_19 = Button(frame_button, command=lambda: entrada_valores("+"), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('bold'), relief=RAISED, overrelief=RIDGE)  # Soma
b_19.place(x=175, y=208)

# Rodando a Janela
janela.mainloop()
