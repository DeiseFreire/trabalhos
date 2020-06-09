# Criando Frames Internos Em Python Tkinter
# https://www.youtube.com/watch?v=T-6MXSh3r8k&list=PL2Dw5PtrD32zzkQ1OQyN4gz3I_8G1MMHl&index=3

from tkinter import*
import random
import time;
import datetime
root = Tk()
root.geometry("1350x750+0+0")
root.title("Sistema de vendas")
root.configure(background= 'grey')
#FRAMES PRIMÁRIOS
Tops = Frame (root, width=1350 , height=100 , bd= 9 , relief= "raise")
Tops.pack(side = TOP)
framef1 = Frame (root, width=900 , height=650 , bd= 8 , relief= "raise")
framef1.pack(side=LEFT)
framef2 = Frame (root, width=440 , height=650 , bd= 8 , relief= "raise")
framef2.pack(side=RIGHT)
#TROCANDO COR DO FUNDO
framef1.configure(background = 'gray')
#RÓTULO CABEÇALHO
lblInfo = Label(Tops, font =('arial', 50, 'bold'), text = 'SISTEMA CAFÉ', bd = 8, width=20)
lblInfo.grid(row=0,column=0) 
#declarando as primeiras variáveis
val1=IntVar()
val1.set("0")
Latta = Checkbutton(framef1aa, text = 'Latta \t', variable=val1, onvalue = 1, offvalue = 0,
                    font =('arial', 18,'bold')).grid(row=0,column=0)
root.mainloop()
