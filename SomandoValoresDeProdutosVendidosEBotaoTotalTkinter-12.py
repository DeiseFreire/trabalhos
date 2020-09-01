#https://www.youtube.com/watch?v=jTzYc8saGqE&list=PL2Dw5PtrD32zzkQ1OQyN4gz3I_8G1MMHl&index=12

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
#CRIANDO OS METODOS DOS BOTOES
#CRIANDO O CODIGO DO BOTAO SAIR
def iExit(): 
root.destroy() 
return 
# CRIANDO O CODIGO DO BOTAO LIMPAR
def Limpar():
Dataordem.set("")
txtRecibo.delete("1.0",END)
Imposto.set("")
Subtotal.set("")
Total.set("")
Totalbolo.set("")
taxaservico.set("")
C_Latte.set("0")
C_LatteGelado.set("0")
C_cafegelado.set("0")
C_cafecreme.set("0") 
C_cafecortado.set("0") 
C_cappuccino.set("0") 
C_cappuccinogelado.set("0") 
C_cafepreto.set("0")
B_bolo_limao.set("0")
B_bolo_milho.set("0")
B_bolo_morango.set("0")
B_torta.set("0")
B_bolo_cafe.set("0")
B_bolo_cenoura.set("0")
B_bolo_chocolate.set("0")
B_torta_limao.set("0")
txtLatte.configure(state=DISABLED) 
txtLatteGelado.configure(state=DISABLED)  
txtcafegelado.configure(state=DISABLED)
txtcafecreme.configure(state=DISABLED) 
txtLatte.configure(state=DISABLED) 
txtcappuccino.configure(state=DISABLED) 
txtcappuccinogelado.configure(state=DISABLED)
txtcafepreto.configure(state=DISABLED)
txtbolo_limao.configure(state=DISABLED) 
txtLatte.configure(state=DISABLED) 
txtbolo_morango.configure(state=DISABLED) 
txttorta.configure(state=DISABLED) 
txtbolo_cafe.configure(state=DISABLED) 
txtbolo_cenoura.configure(state=DISABLED) 
txtbolo_chocolate.configure(state=DISABLED) 
txttorta_limao.configure(state=DISABLED) 

#CRIANDO OS METODOS PARA OS RADIO BUTTONS
def chkLatte():
if(var1.get()==1):
txtLatte.configure(state=NORMAL)
C_Latte.set("")
elif(var1.get()==0):
txtLatte.configure(state=DISABLED)
C_Latte.set("0")

def chkLatte_Gelado():
if(var2.get()==1):
txtLatteGelado.configure(state=NORMAL)
C_LatteGelado.set("")
elif(var2.get()=0):
txtLatteGelado.configure(state==DISABLED)
C_LatteGelado.set("0")


def chkCafe_Gelado():
if(var3.get()==1):
txtcafegelado.configure(state=NORMAL)
C_cafegelado.set("")
elif(var3.get()=0):
txtcafegelado.configure(state==DISABLED)
C_cafegelado.set("0")

def chkCafe_Creme():
if(var4.get()==1):
txtcafecreme.configure(state=NORMAL)
C_cafegelado.set("")
elif(var4.get()=0):
txtcafecreme.configure(state==DISABLED)
C_cafecreme.set("0")

def chkCafe_Cortado():
if(var5.get()==1):
txtcafecortado.configure(state=NORMAL)
C_cafecortado.set("")
elif(var5.get()=0):
txtcafecortado.configure(state==DISABLED)
C_cafecortado.set("0")

def chkCappuccino():
if(var6.get()==1):
txtcappuccino.configure(state=NORMAL)
C_cappuccino.set("")
elif(var6.get()=0):
txtcappuccino.configure(state==DISABLED)
C_cappuccino.set("0")

def chkCappuccino_Gelado():
if(var7.get()==1):
txtcappuccinogelado.configure(state=NORMAL)
C_cappuccinogelado.set("")
elif(var7.get()=0):
txtcappuccinogelado.configure(state==DISABLED)
C_cappuccino.set("0")

def chkCafe_preto():
if(var8.get()==1):
txtcafepreto.configure(state=NORMAL)
C_cafepreto.set("")
elif(var8.get()=0):
txtcafepreto.configure(state==DISABLED)
C_cafepreto.set("0")

def chkBolo_Limao():
if(var9.get()==1):
txtbolo_limao.configure(state=NORMAL)
B_bolo_limao.set("")
elif(var9.get()=0):
txtbolo_limao.configure(state==DISABLED)
B_bolo_limao.set("0")

def chkBolo_Milho():
if(var10.get()==1):
txtbolo_milho.configure(state=NORMAL)
B_bolo_milho.set("")
elif(var10.get()=0):
txtbolo_milho.configure(state==DISABLED)
B_bolo_milho.set("0")

def chkBolo_morango():
if(var11.get()==1):
txtbolo_morango.configure(state=NORMAL)
B_bolo_morango.set("")
elif(var11.get()=0):
txtbolo_morango.configure(state==DISABLED)
B_bolo_morango.set("0")

def chkTorta():
if(var12.get()==1):
txttorta.configure(state=NORMAL)
B_torta.set("")
elif(var12.get()=0):
txttorta.configure(state==DISABLED)
B_torta.set("0")

def chkBolo_Cafe():
if(var13.get()==1):
txtbolo_cafe.configure(state=NORMAL)
B_bolo_cafe.set("")
elif(var13.get()=0):
txtbolo_cafe.configure(state==DISABLED)
B_bolo_cafe.set("0")

def chkBolo_Cenoura():
if(var14.get()==1):
txtbolo_cenoura.configure(state=NORMAL)
B_bolo_cenoura.set("")
elif(var14.get()=0):
txtbolo_cenoura.configure(state==DISABLED)
B_bolo_cenoura.set("0")

def chkBolo_Chocolate():
if(var15.get()==1):
txtbolo_chocolate.configure(state=NORMAL)
B_bolo_chocolate.set("")
elif(var15.get()=0):
txtbolo_chocolate.configure(state==DISABLED)
B_bolo_chocolate.set("0")

def chkTorta_Limao():
if(var16.get()==1):
txttorta_limao.configure(state=NORMAL)
B_torta_limao.set("")
elif(var16.get()=0):
txttorta_limao.configure(state==DISABLED)
B_torta_limao.set("0")

#CRIANDO CODIGO DO BOTAO RECIBO
def custoItem():
Item1=float(C_Latte.get())
Item2=float(C_Lattegelado.get()) 
Item3=float(C_cafegelado.get())  
Item4=float(C_cafecreme.get()) 
Item5=float(C_cafecortado.get()) 
Item6=float(C_cappuccino.get())   
Item7=float(C_cappuccinogelado.get())   
Item8=float(C_cafepreto.get())
Item9=float(B_bolo_limao.get())
Item10=float(B_bolo_milho.get())
Item11=float(B_bolo_morango.get())
Item12=float(B_torta.get())
Item13=float(B_bolo_cafe.get())
Item14=float(B_bolo_cenoura.get())
Item15=float(B_bolo_chocolate.get())
Item16=float(B_torta_limao.get())
Precobebidas=(Item1*1.2)+(Item2*1.99)+(Item3*2.05)+(Item4*2.10)+(Item5*1.99)+(Item6*2.99)+(Item7*1.99)+(Item8*1.99)
Precobolos=(Item9*1.2)+(Item10*1.99)+(Item11*2.05)+(Item12*2.10)+(Item13*1.99)+(Item14*2.99)+(Item15*1.99)+(Item16*1.99)
Bebidapreco="i",str('%.2f'%(Precobebidas))  
Bolopreco="i",str('%.2f'%(Precobolos))  
Totalbolo.set(Bolopreco) 
Totalbebida.set(Bebidapreco)  
SC="i",str('%.2f'%(0.10))
Taxaservico.set(SC)  
SubtotalItens="i",str('%.2f'%(Precobebidas+Precobolos+0,10))      
Taxa="i",str('%.2f'%((Precobebidas+Precobolos+0.10)*0.15) 
Imposto.set(Taxa)
TT=((Precobebidas+Precobolos+0.10)*0.15) 
TC="i",str('%.2f'%((Precobebidas+Precobolos+1.60+TT)
Total.set(TC)






# DECLARANDO AS PRIMEIRAS VARIAVEIS
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
C_LatteGelado.set("0")
C_cafegelado.set("0")
C_cafecreme.set("0") 
C_cafecortado.set("0") 
C_cappuccino.set("0") 
C_cappuccinogelado.set("0") 
C_cafepreto.set("0")
B_bolo_limao.set("0")
B_bolo_milho.set("0")
B_bolo_morango.set("0")
B_torta.set("0")
B_bolo_cafe.set("0")
B_bolo_cenoura.set("0")
B_bolo_chocolate.set("0")
B_torta_limao.set("0")
# CRIANDO OS RADIO BUTTONS PARA O CAFE
Latte = Checkbutton(framef1aa, text=”Cafe_comLeite \t", variable = var1, onvalue = 1, offvalue = 0, width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkLatte).grid(row=0,sticky = W)
Latte_Gelado = Checkbutton(framef1aa, text=”Expresso \t", variable = var2, onvalue = 1, offvalue = 0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkLatte_Gelado).grid(row=1,sticky = W)
Cafe_Creme = Checkbutton(framef1aa, text=”Cafe_comChantilly \t", variable = var3, onvalue = 1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkCafe_Gelado ).grid(row=2,sticky = W)
Cafe_Cortado = Checkbutton(framef1aa, text=”Cafe_Gelado \t", variable = var4, onvalue = 1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkCafe_Creme).grid(row=2,sticky = W)
Cappuccino = Checkbutton(framef1aa, text=”Cafe_Cremoso  \t", variable = var5, onvalue =1,offvalue = 0, width=20, font=('arial', 18, 'bold'),command=chkCafe_Cortado).grid(row=3,sticky = W)
Cappuccino_Gelado=Checkbutton(framef1aa,text=”Cafe_comChocolate\t",variable=var6,onvalue=1,offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkCappuccino).grid(row=4,sticky = W)
Cafe_preto= Checkbutton(framef1aa, text=”Cafe_Preto \t", variable = var7, onvalue = 1, offvalue = 0, width=20,bg='DarkSeaGreen3',fg='blue', font=('arial', 18, 'bold'),command=chkCappuccino_Gelado ).grid(row=5,sticky = W)
Cafe_preto=Checkbutton(framef1aa,text="Cafe_preto\t",variable=var8,onvalue=1,offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkCafe_preto).grid(row=7,sticky=W) 
# CRIANDO OS RADIO BUTTONS PARA OS BOLOS
Bolo_Limao=Checkbutton(framef1ab,text="Bolo_Limao",variable=var9,onvalue=1,offvalue=0,width=15,bg='DarkSeaGreen3',fg='blue',font('ariel',18,'bold'),command=chkBolo_Limao).grid(row=0,sticky=W)
Bolo_Milho = Checkbutton(framef1ab, text="Bolo_Milho \t", variable=var10, onvalue=1, offvalue=0, width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkBolo_Milho).grid(row=0, sticky=W)
Bolo_morando = Checkbutton(framef1ab, text="Bolo_Morando \t", variable=var11, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkBolo_morando).grid(row=0, sticky=W)
Torta = Checkbutton(framef1ab, text="Torta \t", variable=var12, onvalue=1, offvalue=0, width=13,bg='DarkSeaGreen3',fg='blue',font=('arial', 18, 'bold'),command=chkTorta).grid(row=0, sticky=W)
Bolo_Cafe = Checkbutton(framef1ab, text="Bolo_Cafe \t", variable=var13, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkBolo_Cafe).grid(row=0, sticky=W)
Bolo_Cenoura = Checkbutton(framef1ab, text="Bolo_Cenoura \t", variable=var14, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkBolo_Cenoura).grid(row=0, sticky=W)
Bolo_Chocolate = Checkbutton(framef1aa, text="Bolo_Chocolate \t", variable=var15, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkBolo_Chocolate).grid(row=0, sticky=W)
Torta_Limao = Checkbutton(framef1ab, text="Torta_Limao \t", variable=var16, onvalue=1, offvalue=0,width=20,bg='DarkSeaGreen3',fg='blue',font=('arial',18,'bold'),command=chkTorta_Limao).grid(row=0, sticky=W)
# CRIANDO OS CAMPOS DE TEXTO, CAIXA TEXTO DO CAFÉ
txtLatte = Entry(frame1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=6, justify='left', textvariable=C_Latte, state=NORMAL)
txtLatte.grid(row=0, column=1)
txtLatteGelado = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1, width=8, justify='left', textvariable=C_LatteGelado, state=NORMAL)
txtLatteGelado.grid(row=1, column=1)
txtcafegelado = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cafegelado, state=DISABLED)
txtcafegelado.grid(row=2, column=1)
txtcafecreme = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cafecreme, state=DISABLED)
txtcafecreme.grid(row=3, column=1)
txtLatte = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cafecortado, state=DISABLED)
txtLatte.grid(row=4, column=1)
txtcappuccino = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cappuccino, state=DISABLED)
txtcappuccino.grid(row=5, column=1)
txtcappuccinogelado = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cappuccinogelado, state=DISABLED)
txtcappuccinogelado.grid(row=6, column=1)
txtcafepreto = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,bg='SKYBlue1', width=8, justify='left', textvariable=C_cafepreto, state=DISABLED)
txtcafepreto.grid(row=7, column=1)
# CRIANDO OS CAMPOS DE TEXTO, CAIXA TEXTO, DOS BOLOS
txtbolo_limao = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=6, justify='left', textvariable=B_bolo_limao, state=DISABLED)
txtbolo_limao.grid(row=0, column=1)
txtLatte = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_bolo_milho, state=DISABLED)
txtLatte.grid(row=1, column=1)
txtbolo_morango = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_bolo_morango, state=DISABLED)
txtbolo_morango.grid(row=2, column=1)
txttorta = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left',textvariable=B_torta, state=DISABLED)
txttorta.grid(row=3, column=1)
txtbolo_cafe = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_bolo_cafe, state=DISABLED)
txtbolo_cafe.grid(row=4, column=1)
txtbolo_cenoura = Entry(frame1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_bolo_cenoura, state=DISABLED)
txtbolo_cenoura.grid(row=5, column=1)
txtbolo_chocolate = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_bolo_chocolate, state=DISABLED)
txtbolo_chocolate.grid(row=6, column=1)
txttorta_limao = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1, bg='SKyBlue1', width=8, justify='left', textvariable=B_torta_limao, state=DISABLED)
txttorta_limao.grid(row=7, column=1)
# CAMPO DO RECIBO
lblRecibo = Label = (frameft2, font=('arial', 12, 'bold'), text = "Recibo do Cliente :",bg='IndianRed3' bd = 2, fg='white',anchor = 'W')
lblRecibo.grid(row=0,column=0,sticky=w)
lblRecibo = Text(frameft2, width=59, height=28, bg=”lemonchiffon”, bd=8, font=('arial', 10))
textRecibo.grid(row=1, column=0)
# CAMPOS DOS BOTÕES
cmdTotal = Button(framefb2, padx=16, pady=1, bg='black’, bd=4, fg='green', font=('arial', 16, 'bold'), width=5, text=”Total”).grid(
   row=0, column=0)
cmdRecibo = Button(framefb2, padx=16, pady=1, bg='black’, bd=4, fg=’white', font=('arial', 16, 'bold'), width=5, text=”Recibo”).grid(
   row=0, column=1)
cmdLimpar = Button(framefb2, padx=16, pady=1, bg='black’, bd=4, f'g=’yellow', font=('arial', 16, 'bold'), width=5, text=”Limpar”,command=Limpar).grid(
   row=0, column=2)
cmdSair = Button(framefb2, padx=16, pady=1, bg='black’, bd=4, fg='red', font=('arial', 16, 'bold'), width=5, text=”Sair”,command=iExit).grid(
   row=0, column=3)
# CRIANDO OS CAMPOS DO RODAPE  FRAME DA ESQUERDA
lblCustobedidas = Label(framef2aa, font=('arial', 12, 'bold'), text="Custo Bebidas :", bd=2)
lblCustobebidas.grid(row=0, column=0, sticky=W)
txtCustobebidas = Entry(framef2aa, font=('arial', 16, 'bold')
bd = 2, justify = 'left',textvariable=Totalbebida)
txtCustobebidas.grid(row=0, column=1)
lblCustobolo = Label(framef2aa, font=('arial', 12, 'bold'), text="Custo Bolos :", bd=2)
lblCustobolo.grid(row=1, column=0, sticky=W)
txtCustobolo=Entry(frame2aa,font=('arial',16,'bold'),bd=2,justify='left',textvariable=Custobolo)
txtCustobolo.grid(row=1,column=1)
lblTaxaservico = Label(framef2aa, font=('arial', 12, 'bold'), text="Taxa Serviços :", bd=2)
lblTaxaservico.grid(row=2, column=0, sticky=W)
txtTaxaservico = Entry(framef2aa, font=('arial', 16, 'bold')
bd = 2, justify = 'left'), 
txtTaxaservico.grid(row=2, column=1)
Totalbolo.set("")
Totalbebida.set("")

# CRIANDO OS CAMPOS DO RODAPE  FRAME DA DIREITA
lblimposto=Label(frame2ab,font=('arial',12,'bold'),text="Imposto :",bd=2,bg='Burlywood3') lblimposto.grid(row=0,column=0,sticky=W) 

txtimposto=Entry(frame2ab,font=('arial',16,'bold'),bd=2,justify='left',textvariable=imposto ) txtimposto.grid(row=0,column=1) 

lblsubtotal=Label(frame2ab,font=('arial',12,'bold'),text="Subtotal :",bd=2,bg='Burlywood3') lblsubtotal.grid(row=0,column=0,sticky=W) 

txtsubtotal=Entry(frame2ab,font=('arial',16,'bold'),bd=2,justify='left',textvariable=Subtotal ) txtsubtotal.grid(row=0,column=1) 

lbltotal=Label(frame2ab,font=('arial',12,'bold'),text="Total :",bd=2,bg='Burlywood3') lbltotal.grid(row=0,column=0,sticky=W) 

txttotal=Entry(frame2ab,font=('arial',16,'bold'),bd=2,justify='left',textvarialble=Total) 
txtsubtotal.grid(row=0,column=1) 

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




