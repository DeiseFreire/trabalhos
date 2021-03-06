# -------------------------------------------------------------------------------------------
# Fonte da ideia: 
# Alinhando Os Objetos Em Python Tkinter - 05
# https://www.youtube.com/watch?v=gVi7mm51cBU&list=PL2Dw5PtrD32zzkQ1OQyN4gz3I_8G1MMHl&index=5
# -------------------------------------------------------------------------------------------

from tkinter import* 
import random
import time;
import datetime
root = Tk()
root.geometry("1350x750+0+0")
root.title("Sistema de vendas")
root.configure(background= 'grey')
#FRAMES PRIMÁRIOS
Tops = Frame (root, width=1350 , height=100 , bd= 14, relief= "raise")
Tops.pack(side = TOP)
framef1 = Frame (root, width=900 , height=650 , bd= 8 , relief= "raise")
framef1.pack(side=LEFT)
framef2 = Frame (root, width=440 , height=650 , bd= 8 , relief= "raise")
framef2.pack(side=RIGHT)
# FRAME SECUNDÁRIOS
frameft2 = Frame (framef2, width=440, height=650, bd=2, relief="raise")
frameft2.pack(side=TOP)
framefb2 = Frame (framef2, width=440, height=50, bd=2, relief="raise")
framefb2.pack(side=BOTTON)
framef1a = Frame (framef1a, width=900, height=330, bd=2, relief="raise")
framef1a.pack(side=TOP)
framef2a = Frame (framef1, width=900, height=320, bd=2, relief="raise")
framef2a.pack(side=BOTTON)
framef1aa = Frame (framef1a, width=450, height=330, bd=2, relief="raise")
framef2a.pack(side=LEFT)
framef1ab = Frame (framef1a, width=450, height=330, bd=2, relief="raise")
framefab.pack(side=RIGHT)
# TROCANDO A COR DE FUNDO DO FRAME DA ESQUERDA
framef1.configure(background 'grey')
# INSERINDO O RÓTULO DO CABECALHO COM O TÍTULO 
lblInfo=Label(Tops, font=('arial', 70, 'bold'), text="SISTEMA CAFETERIA", bd=8, width=23)
lblInfo=.grid(row=0, column=0)
#DECLARANDO AS PRIMEIRAS VARIÁVEIS 
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
# SETANDO AS VARIÁVEIS 
var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
# CRIANDO OS RADIO BUTTONS PARA O CAFE
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var1, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var2, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var3, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var4, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var5, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var6, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var1, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var7, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var8, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
# CRIANDO OS RADIO BUTTONS PARA OS BOLOS
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var9, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var10, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var11, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var12, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var13, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var14, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1aa, text = "Latta \t", variable = var15, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var16, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var17, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
Latta = Checkbutton(framef1ab, text = "Latta \t", variable = var18, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold')).grid(row=0,column=0)
