# Bibliotecas
from cgitb import text
from codecs import BOM_UTF16
from msilib.schema import Icon
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import width


# cores
cor1 = "#3b3b3b"    # preta
cor2 = "#feffff"    # branco
cor3 = "#38576b"    # azul
cor4 = "#ECEFF1"    # cinzento 
cor5 = "#FFAB40"    # laranja 
cor6 = "#058073"    # azul esverdiado


# janelas

janela = Tk()
janela.title('Calculadora')
janela.geometry("238x330")
janela.config(bg=cor1)
janela.iconbitmap("imagens/icone.ico")

frame_tela = Frame(janela, width=245, height=70, bg=cor6)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=245, height=268)
frame_corpo.grid(row=1, column=0)


#variavel todos valores
todos_valores= ''

# criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable =valor_texto, width=16, height=2, padx=11, relief=FLAT,anchor="e",justify=RIGHT,font=('Ivy 18'), bg= cor6, fg= cor2)
app_label.place(x=0,y=0)

# criando função
def entrada_valor(event):

    global todos_valores
    todos_valores = todos_valores + str(event)
    
    # mostrando valor na tela
    valor_texto.set(todos_valores)

# Função para calculos

def calcular():
    global todos_valores
    resultado= eval(todos_valores)
    valor_texto.set(str(resultado))

#limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


# botoes
b_1= Button(frame_corpo,command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo,command=lambda: entrada_valor('%'), text="%", width=5, height=2, bg=cor5,fg= cor2, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=119, y=0)
b_3 = Button(frame_corpo,command=lambda: entrada_valor('/'),  text="/", width=5, height=2, bg=cor5, fg= cor2, font=('ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=179,y=0)
b_4 = Button(frame_corpo,command=lambda: entrada_valor('*'),  text="x", width=5, height=2, bg=cor5, fg= cor2, font=('ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=179,y=52)
b_5 = Button(frame_corpo,command=lambda: entrada_valor('-'),  text="-", width=5, height=2, bg=cor5, fg= cor2, font=('ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=179,y=105)
b_6 = Button(frame_corpo,command=lambda: entrada_valor('+'),  text="+", width=5, height=2, bg=cor5, fg= cor2, font=('ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=179,y=158)
b_7 = Button(frame_corpo,command= calcular,  text="=", width=5, height=2, bg=cor5, fg= cor2, font=('ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=179,y=210)
b_8= Button(frame_corpo,command=lambda: entrada_valor('7'),  text="7", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_8.place(x=0,y=52)
b_9= Button(frame_corpo,command=lambda: entrada_valor('8'),  text="8", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_9.place(x=58,y=52)
b_10= Button(frame_corpo,command=lambda: entrada_valor('9'),  text="9", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_10.place(x=118,y=52)
b_11= Button(frame_corpo,command=lambda: entrada_valor('4'),  text="4", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_11.place(x=0,y=104)
b_12= Button(frame_corpo,command=lambda: entrada_valor('5'),  text="5", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_12.place(x=58,y=104)
b_13= Button(frame_corpo,command=lambda: entrada_valor('6'),  text="6", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_13.place(x=118,y=104)
b_14= Button(frame_corpo,command=lambda: entrada_valor('1'),  text="1", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_14.place(x=0,y=156)
b_15= Button(frame_corpo,command=lambda: entrada_valor('2'),  text="2", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_15.place(x=58,y=156)
b_16= Button(frame_corpo,command=lambda: entrada_valor('3'),  text="3", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_16.place(x=118,y=156)
b_17= Button(frame_corpo,command=lambda: entrada_valor('0'),  text="0", width=11, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_17.place(x=-1,y=208)
b_17= Button(frame_corpo,command=lambda: entrada_valor('.'),  text=".", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE)
b_17.place(x=118,y=208)




janela.mainloop()