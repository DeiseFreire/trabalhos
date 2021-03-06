#https://www.youtube.com/watch?v=dzT33Rjw-jA&list=PL2Dw5PtrD32zzkQ1OQyN4gz3I_8G1MMHl&index=10

import tkinter
import random
import time
import datetime
root = Tk()
root.geometry("1350x750+0+0")
root.title("Sistema de vendas")
root.configure(background='gray')
# FRAMES PRIMÁRIOS
Tops = Frame(root, width=1350, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)
framef1 = Frame(root, width=900, height=650, bd=8, relief="raise")
framef1.pack(side=LEFT)
framef2 = Frame(root, width=440, height=650, bd=8, relief="raise")
framef2.pack(side=RIGHT)
# FRAME SECUNDÁRIOS
frameft2 = Frame(framef2, width=440, height=450, bd=2, relief="raise")
frameft2.pack(side=TOP)
framefb2 = Frame(framef2, width=440, height=250, bg=’black’, bd=2, relief="raise")
framefb2.pack(side=BUTTON)
framef1a = Frame(framef1a, width=900, height=330, bd=2, relief="raise")
framef1a.pack(side=TOP)
framef2a = Frame(framef1, width=900, height=320, bd=2, relief="raise")
framef2a.pack(side=BUTTON)
framef1aa = Frame(framef1a, width=1000, height=330, bd=2, relief="raise")
framef2a.pack(side=LEFT)
framef1ab = Frame(framef1a, width=450, height=330, bd=2, relief="raise")
framefab.pack(side=RIGHT)
# CRIANDO FRAMES DO RODAPE
framef2aa =Frame(framef2a, width=450, height=800, bd=2, relief="raise")
framef2aa.pack(side=LEFT)
framef2ab = Frame(framef2a, width=450, height=800, bd=2, relief="raise")
framef2ab.pack(side=RIGHT)
frameRODAPE = Frame(framef2a, width=211, height=190, bd=0, relief="raise")
frameRODAPE.pack(side=BUTTON)
# TROCANDO A COR DE FUNDO DO FRAME DA ESQUERDA
Tops.configure(background='gray')
framef1.configure(background='gray')
frame1aa.configure(background='DarkSeaGreen3')
frame1ab.configure(background='DarkSeaGreen3')  
frame2a.configure(background='Burlywood3')  
frame2aa.configure(background='Burlywood3') 
frame2ab.configure(background='Burlywood3')  
frameRodape.configure(background='Burlywood3')  
frameft2.configure(background='IndianRed3')
# INSERINDO O RÓTULO DO CABECALHO COM O TÍTULO
lblInfo = Label(Tops, font=('arial', 70, 'bold'), text="SISTEMA CAFETERIA", bd=6, width=23)
lblInfo =.grid(row=0, column=0)
# DECLARANDO AS PRIMEIRAS VARIÁVEIS
C_Latte=StringVar()
C_LatteGelado=StringVar()
C_cafegelado=StringVar()
C_cafecreme=StringVar()
C_cafecortado=StringVar()
C_cappuccino=StringVar()
C_cappuccinogelado=StringVar()
C_cafepreto=StringVar()
B_bolo_limao=StringVar()
B_bolo_milho=StringVar()
B_bolo_morando=StringVar()
B_torta.set=StringVar()
B_bolo_cafe=StringVar()
B_bolo_cenoura=StringVar()
B_bolo_chocolate=StringVar()
B_torta_limao=StringVar()
#VARIAVEIS DO RODAPE
Dataordem=StringVar()
Recibo=StringVar()
Imposto=StringVar()
Subtotal=StringVar()
Total=StringVar()
Totalbolo=StringVar()
taxaservico=StringVar()

var1 = IntVar()
var2 = IntVar()
var3 = ntVar()
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
C_Latte=StringVar()
C_LatteGelado=StringVar()
C_cafegelado=StringVar()
C_cafecreme=StringVar()
C_cafecortado=StringVar()
C_cappuccino=StringVar()
C_cappuccinogelado=StringVar()
C_cafepreto=StringVar()
B_bolo_limao=StringVar()
B_bolo_milho=StringVar()
B_bolo_morango=StringVar()
B_torta=StringVar()
B_bolo_cafe=StringVar()
B_bolo_cenoura=StringVar()
B_bolo_chocolate=StringVar()
B_torta_limao=StringVar()
Dataordem=StringVar()
Recibo=StringVar()
Imposto=StringVar()
Subtotal=StringVar()
Total=StringVar()
Totalbolo=StringVar()
taxaserviço=StringVar()
C_Latte.set("0")
var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")
var17.set("0")
var18.set("0")
# CRIANDO OS RADIO BUTTONS PARA O CAFE
Cafe_comLeite = Checkbutton(framef1aa, text=”Cafe_comLeite \t
", variable = var1, onvalue = 1, offvalue = 0, width=20, bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0,sticky = W)
Expresso = Checkbutton(framef1aa, text=”Expresso \t
", variable = var2, onvalue = 1, offvalue = 0, width=20,bg='DarkSeaGreen3',fg='blue', font=('arial', 18, 'bold')).grid(row=1,sticky = W)
Cafe_comChantilly = Checkbutton(framef1aa, text=”Cafe_comChantilly \t
", variable = var3, onvalue = 1, offvalue = 0, width=20,bg='DarkSeaGreen3',fg='blue', font=('arial', 18, 'bold')).grid(row=2,sticky = W)
Cafe_Gelado = Checkbutton(framef1aa, text=”Cafe_Gelado \t
", variable = var4, onvalue = 1, offvalue = 0, width=20,bg='DarkSeaGreen3',fg='blue', font=('arial', 18, 'bold')).grid(row=2,sticky = W)
Cafe_Cremoso = Checkbutton(framef1aa, text=”Cafe_Cremoso  \t
", variable = var5, onvalue = 1, offvalue = 0, width=20, font=('arial', 18, 'bold')).grid(row=3,sticky = W)
Cafe_comChocolate = Checkbutton(framef1aa, text=”Cafe_comChocolate \t
", variable = var6, onvalue = 1, offvalue = 0, width=20,bg='DarkSeaGreen3',fg='blue', font=('arial', 18, 'bold')).grid(row=4,sticky = W)
Cafe_Forte = Checkbutton(framef1aa, text=”Cafe_Preto \t
", variable = var7, onvalue = 1, offvalue = 0, width=20,bg='DarkSeaGreen3',fg='blue', font=('arial', 18, 'bold')).grid(row=5,sticky = W)
Cafe_Creme =Checkbutton(framef1aa, text=”Cafe_Creme \t
", variable = var8, onvalue = 1, offvalue = 0, width=20,bg='DarkSeaGreen3',fg='blue', font=('arial', 18, 'bold')).grid(row=6,sticky = W)
Cappuccino = Checkbutton(framef1aa, text=”Cappuccino \t
", variable = var9, onvalue = 1, offvalue = 0, width=20,bg='DarkSeaGreen3',fg='blue', font=('arial', 18, 'bold')).grid(row=7,sticky = W)
# CRIANDO OS RADIO BUTTONS PARA OS BOLOS
Bolo_Limao = Checkbutton(framef1ab, text="Bolo_Limao \t", variable=var9, onvalue=1, offvalue=0,
width=15,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Bolo_Milho = Checkbutton(framef1ab, text="Bolo_Milho \t", variable=var10, onvalue=1, offvalue=0, width=20,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Bolo_Morando = Checkbutton(framef1ab, text="Bolo_Morando \t", variable=var11, onvalue=1, offvalue=0, width=20,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Torta = Checkbutton(framef1ab, text="Torta \t", variable=var12, onvalue=1, offvalue=0, width=13,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Bolo_Cenoura = Checkbutton(framef1ab, text="Bolo_Cenoura \t", variable=var13, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Bolo_Chocolate = Checkbutton(framef1ab, text="Bolo_Chocolate \t", variable=var14, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Bolo_Prestigio = Checkbutton(framef1aa, text="Bolo_Prestigio \t", variable=var15, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Bolo_FlorestaNegra = Checkbutton(framef1ab, text="Bolo_FlorestaNegra \t", variable=var16, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Bolo_Pamonha = Checkbutton(framef1ab, text="Bolo_Pamonha \t", variable=var17, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0, sticky=W)
Bolo_SonhoDeValsa = Checkbutton(framef1ab, text="Bolo_SonhoDeValsa \t", variable=var18, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold')).grid(row=0, sticky=W)
# CRIANDO OS CAMPOS DE TEXTO, CAIXA TEXTO DO CAFÉ
txtLatte = Entry(frame1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=6, justify='left', textvariable=C_Latte, state=NORMAL)
txtLatte.grid(row=0, column=1)
txtLatte = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1, width=8, justify='left', textvariable=C_LatteGelado, state=NORMAL)
txtLatte.grid(row=1, column=1)
txtLatte = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cafegelado, state=DISABLED)
txtLatte.grid(row=2, column=1)
txtLatte = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cafecreme, state=DISABLED)
txtLatte.grid(row=3, column=1)
txtLatte = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cafecortado, state=DISABLED)
txtLatte.grid(row=4, column=1)
txtLatte = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cappuccino, state=DISABLED)
txtLatte.grid(row=5, column=1)
txtLatte = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cappuccinogelado, state=DISABLED)
txtLatte.grid(row=6, column=1)
txtLatte = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cafepreto, state=DISABLED)
txtLatte.grid(row=7, column=1)
# CRIANDO OS CAMPOS DE TEXTO, CAIXA TEXTO, DOS BOLOS
txtLatte = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=6, justify='left', textvariable=B_bolo_limao, state=DISABLED)
txtLatte.grid(row=0, column=1)
txtLatte = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_bolo_milho, state=DISABLED)
txtLatte.grid(row=1, column=1)
txtLatte = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_bolo_morango, state=DISABLED)
txtLatte.grid(row=2, column=1)
txtLatte = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left',textvariable=B_torta, state=DISABLED)
txtLatte.grid(row=3, column=1)
txtLatte = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_bolo_cafe, state=DISABLED)
txtLatte.grid(row=4, column=1)
txtLatte = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_bolo_cenoura, state=DISABLED)
txtLatte.grid(row=5, column=1)
txtLatte = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_bolo_chocolate, state=DISABLED)
txtLatte.grid(row=6, column=1)
txtLatte = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_torta_limao, state=DISABLED)
txtLatte.grid(row=7, column=1)
# CAMPO DO RECIBO
lblRecibo = Label = (frameft2, font=('arial', 12, 'bold'), text = "Recibo do Cliente :", bd = 2, anchor = 'W')
lblRecibo.grid(row=0, column=0, sticky=W)
lblRecibo = Text = (frameft2, width=59, height=28, bg"white", bd3, font=('arial', 10))
textRecibo.grid(row=1, column=0)
# CAMPOS DOS BOTÕES
cmdTotal = Button(framefb2, padx=16, pady=1, bg='black’, bd=4, fg='green', font=('arial', 16, 'bold'), width=5, text=”Total”).grid(
   row=0, column=0)
cmdRecibo = Button(framefb2, padx=16, pady=1, bg='black’, bd=4, fg=’white', font=('arial', 16, 'bold'), width=5, text=”Recibo”).grid(
   row=0, column=1)
cmdLimpar = Button(framefb2, padx=16, pady=1, bg='black’, bd=4, f'g=’yellow', font=('arial', 16, 'bold'), width=5, text=”Limpar”,command=Limpar).grid(
   row=0, column=2)
cmdSair = Button(framefb2, padx=16, pady=1, bg='black’, bd=4, fg='red', font=('arial', 16, 'bold'), width=5, text=”Sair”,command=Exit).grid(
   row=0, column=3)
# CRIANDO OS CAMPOS DO RODAPE  FRAME DA ESQUERDA
lblCustobedidas = Label(framef2aa, font=('arial', 12, 'bold'), text="Custo Bebidas :", bd=2)
lblCustobebidas.grid(row=0, column=0, sticky=W)
txtCustobebidas = Entry(framef2aa, font=('arial', 16, 'bold')
bd = 2, justify = 'left')
txtCustobebidas.grid(row=0, column=1)
lblCustobolo = Label(framef2aa, font=('arial', 12, 'bold'), text="Custo Bolos :", bd=2)
lblCustobolo.grid(row=1, column=0, sticky=W)
txtCustobolo = Entry(framef2aa, font=('arial', 16, 'bold')
bd = 2, justify = 'left')
txtCustobolo.grid(row=1, column=1)
lblTaxaservico = Label(framef2aa, font=('arial', 12, 'bold'), text="Taxa Serviços :", bd=2)
lblTaxaservico.grid(row=2, column=0, sticky=W)
txtTaxaservico = Entry(framef2aa, font=('arial', 16, 'bold')
bd = 2, justify = 'left')
txtTaxaservico.grid(row=2, column=1)
# CRIANDO OS CAMPOS DO RODAPE  FRAME DA DIREITA
lblCustobedidas = Label(framef2ab, font=('arial', 12, 'bold'), text="Imposto :", bd=2)
lblCustobebidas.grid(row=0, column=0, sticky=W)
txtCustobebidas = Entry(framef2ab, font=('arial', 16, 'bold')
bd = 2, justify = 'left')
txtCustobebidas.grid(row=0, column=1)
lblCustobedidas = Label(framef2ab, font=('arial', 12, 'bold'), text="Sub Total :", bd=2)
lblCustobebidas.grid(row=1, column=0, sticky=W)
txtCustobebidas = Entry(framef2aa, font=('arial', 16, 'bold')
bd = 2, justify = 'left')
txtCustobebidas.grid(row=1, column=1)
lblCustobedidas = Label(framef2ab, font=('arial', 12, 'bold'), text="Total  :", bd=2)
lblCustobebidas.grid(row=2, column=0, sticky=W)
txtCustobebidas = Entry(framef2ab, font=('arial', 16, 'bold')
bd = 2, justify = 'left')
txtCustobebidas.grid(row=2, column=1)
root.mainloop()



