from tkinter import *  # interface python padrão de ferramentas GUI
from tkinter import Tk, StringVar, ttk  # (tkinter.ttk=button,checkbutton,entry,frame,label....)

# import topo as topo

root = Tk()  # A criação de uma instância de Tk inicializa este interpretador e cria  root window.
root.geometry( "1350x750+0+0" )
root.title( " João Paulo Pires Dantas e Deise Freire" )
# --------A tela esta pronta-------------

Tops = Frame( root, width=1350, height=100, bd=6,
              relief="raise" )  # (bd=The size tamanho da borda ao redor do indicador. O padrão é 2 pixels)
# relief=With Com o valor padrão, relief = FLAT, o botão de seleção não se destaca de seu fundo. Você pode definir esta opção para qualquer um dos outros estilos
# height=A dimensão vertical do novo frame.
Tops.pack( side=TOP )  # Este gerenciador de geometria organiza widgets em blocos antes de colocá-los na parte de cima.
# -----------É aqui que o restaurante de fast food se torna útil--------------------

lblTitle = Label( Tops, font=('arial', 50, 'bold'), text="Sistema de Pedidos de Alimentos\t" )
lblTitle.grid( row=0, column=0 )
# ------------o restaurante de fast food está em construção---------------------

BottomMainFrame = Frame( root, width=1350, height=650, bd=6, relief="raise" )
BottomMainFrame.pack( side=BOTTOM )
# ----------o quadro do frame da direita está pronto------------------

f1 = Frame( BottomMainFrame, width=450, height=650, bd=2, relief="raise" )
f1.pack( side=LEFT )

f2 = Frame( BottomMainFrame, width=450, height=650, bd=2, relief="raise" )
f2.pack( side=LEFT )

f2TOP = Frame( f2, width=450, height=350, bd=2, relief="raise" )
f2TOP.pack( side=TOP )

f2BOTTOM = Frame( f2, width=450, height=300, bd=1, relief="raise" )
f2BOTTOM.pack( side=BOTTOM )
# ---------------F2 FRAME MOLDURA------------------------------------

f3 = Frame( BottomMainFrame, width=450, height=650, bd=0, relief="raise" )
f3.pack( side=RIGHT )
# ----------------F2 FRAME---------------------------------

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
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = StringVar()
var23 = IntVar()

var1.set( 0 )
var2.set( 0 )
var3.set( 0 )
var4.set( 0 )
var5.set( 0 )
var6.set( 0 )
var7.set( 0 )
var8.set( 0 )
var9.set( 0 )
var10.set( 0 )
var11.set( 0 )
var12.set( 0 )
var13.set( 0 )
var14.set( 0 )
var15.set( 0 )
var16.set( 0 )
var17.set( 0 )
var18.set( 0 )
var19.set( 0 )
var20.set( 0 )
var21.set( 0 )
var22.set( "" )
var23.set( 0 )

varFritas = StringVar()
varSalada = StringVar()
varHamburguer = StringVar()
varPizza = StringVar()
varPasteis = StringVar()
varMacarronada = StringVar()
varCrepes = StringVar()
varSanduiches = StringVar()

varSorvetes = StringVar()
varBrigadeiro = StringVar()
varPudim = StringVar()
varTorta = StringVar()
varGelatina = StringVar()

varCha = StringVar()
varRefrigerantes = StringVar()
varCafe = StringVar()
varSuco = StringVar()
varToddynho = StringVar()

varBaunilha = StringVar()
varMorango = StringVar()
varChocolate = StringVar()

varAlterar = StringVar()
varSubTotal = StringVar()
varTotal = StringVar()
varVAT = StringVar()
varTaxa = StringVar()
varPagar = IntVar()

varFritas.set( "0" )
varSalada.set( "0" )
varHamburguer.set( "0" )
varPizza.set( "0" )
varPasteis.set( "0" )
varMacarronada.set( "0" )
varCrepes.set( "0" )
varSanduiches.set( "0" )
varTotal.set( "0" )
varPagar.set( " " )

varSorvetes.set( "0" )
varBrigadeiro.set( "0" )
varPudim.set( "0" )
varTorta.set( "0" )
varGelatina.set( "0" )

varCha.set( "0" )
varRefrigerantes.set( "0" )
varCafe.set( "0" )
varSuco.set( "0" )
varToddynho.set( "0" )
varBaunilha.set( "0" )
varMorango.set( "0" )
varChocolate.set( "0" )

varVAT.set( "" )
varTaxa.set( "0" )
varTotal.set( "0" )
varAlterar.set( "0" )
varSubTotal.set( "0" )


def iSair():
    from tkinter import messagebox
    qSair = messagebox.askyesno("Você quer sair?" )
    if qSair > 0:
        root.destroy()
        return


def Iniciar():
    var1.set( 0 )
    var2.set( 0 )
    var3.set( 0 )
    var4.set( 0 )
    var5.set( 0 )
    var6.set( 0 )
    var7.set( 0 )
    var8.set( 0 )
    var9.set( 0 )
    var10.set( 0 )
    var11.set( 0 )
    var12.set( 0 )
    var13.set( 0 )
    var14.set( 0 )
    var15.set( 0 )
    var16.set( 0 )
    var17.set( 0 )
    var18.set( 0 )
    var19.set( 0 )
    var20.set( 0 )
    var21.set( 0 )
    var22.set( 0 )
    var23.set( 0 )

    varFritas.set( "0" )
    varSalada.set( "0" )
    varHamburguer.set( "0" )
    varPizza.set( "0" )
    varPasteis.set( "0" )
    varMacarronada.set( "0" )
    varCrepes.set( "0" )
    varSanduiches.set( "0" )
    varTotal.set( "0" )

    varSorvetes.set( "0" )
    varBrigadeiro.set( "0" )
    varPudim.set( "0" )
    varTorta.set( "0" )
    varGelatina.set( "0" )

    varCha.set( "0" )
    varRefrigerantes.set( "0" )
    varCafe.set( "0" )
    varSuco.set( "0" )
    varToddynho.set( "0" )
    varBaunilha.set( "0" )
    varMorango.set( "0" )
    varChocolate.set( "0" )

    # varAlterar.set("0")
    # varSubTotal.set("0")

    # =======================
    varVAT.set( "" )
    varTaxa.set( "0" )
    varTotal.set( "0" )
    varAlterar.set( " " )
    varSubTotal.set( "0" )
    varPagar.set( " " )

    # ====================

    txtFritas.configure( state=DISABLED )
    txtSalada.configure( state=DISABLED )
    txtHamburguer.configure( state=DISABLED )
    txtPizza.configure( state=DISABLED )
    txtPasteis.configure( state=DISABLED )
    txtMacarronada.configure( state=DISABLED )
    txtCrepes.configure( state=DISABLED )
    txtSanduiches.configure( state=DISABLED )
    txtSorvetes.configure( state=DISABLED )
    txtBrigadeiro.configure( state=DISABLED )
    txtPudim.configure( state=DISABLED )
    txtTorta.configure( state=DISABLED )
    txtGelatina.configure( state=DISABLED )
    txtCha.configure( state=DISABLED )
    txtRefrigerantes.configure( state=DISABLED )
    txtCafe.configure( state=DISABLED )
    txtSuco.configure( state=DISABLED )
    txtToddynho.configure( state=DISABLED )
    txtBaunilha.configure( state=DISABLED )
    txtMorango.configure( state=DISABLED )
    txtChocolate.configure( state=DISABLED )
    # txtPagar.configure(state =DISABLED)
    txtAlterar.configure( state=DISABLED )
    txtTaxa.configure( state=DISABLED )
    txtSubTotal.configure( state=DISABLED )
    txtTotal.configure( state=DISABLED )
    var8.get() == 0


def chkFritas():
    if (var1.get() == 1):
        txtFritas.configure( state=NORMAL )
        varFritas.set( "" )

    elif (var1.get() == 0):
        txtFritas.configure( state=DISABLED )
        varFritas.set( "0" )


def chkSalada():
    if (var2.get() == 1):
        txtSalada.configure( state=NORMAL )
        varSalada.set( "" )

    elif (var2.get() == 0):
        txtSalada.configure( state=DISABLED )
        varSalada.set( "0" )


def chkHamburguer():
    if (var3.get() == 1):
        txtHamburguer.configure( state=NORMAL )
        varHamburguer.set( "" )

    elif (var3.get() == 0):
        txtHamburguer.configure( state=DISABLED )
        varHamburguer.set( "0" )


def chkPizza():
    if (var4.get() == 1):
        txtPizza.configure( state=NORMAL )
        varPizza.set( "" )

    elif (var4.get() == 0):
        txtPizza.configure( state=DISABLED )
        varPizza.set( "0" )


def chkPasteis():
    if (var5.get() == 1):
        txtPasteis.configure( state=NORMAL )
        varPasteis.set( "" )

    elif (var5.get() == 0):
        txtPasteis.configure( state=DISABLED )
        varPasteis.set( "0" )


def chkMacarronada():
    if (var6.get() == 1):
        txtMacarronada.configure( state=NORMAL )
        varMacarronada.set( "" )

    elif (var6.get() == 0):
        txtMacarronada.configure( state=DISABLED )
        varMacarronada.set( "0" )


def chkCrepes():
    if (var7.get() == 1):
        txtCrepes.configure( state=NORMAL )
        varCrepes.set( "" )

    elif (var7.get() == 0):
        txtCrepes.configure( state=DISABLED )
        varCrepes.set( "0" )


def chkSanduiches():
    if (var8.get() == 1):
        txtSanduiches.configure( state=NORMAL )
        varSanduiches.set( "" )

    elif (var8.get() == 0):
        txtSanduiches.configure( state=DISABLED )
        varSanduiches.set( "0" )


def chkSorvetes():
    if (var9.get() == 1):
        txtSorvetes.configure( state=NORMAL )
        varSorvetes.set( "" )

    elif (var9.get() == 0):
        txtSorvetes.configure( state=DISABLED )
        varSorvetes.set( "0" )


def chkBrigadeiro():
    if (var10.get() == 1):
        txtBrigadeiro.configure( state=NORMAL )
        varBrigadeiro.set( "" )

    elif (var10.get() == 0):
        txtBrigadeiro.configure( state=DISABLED )
        varBrigadeiro.set( "0" )


def chkPudim():
    if (var11.get() == 1):
        txtPudim.configure( state=NORMAL )
        varPudim.set( "" )

    elif (var11.get() == 0):
        txtPudim.configure( state=DISABLED )
        varPudim.set( "0" )


def chkTorta():
    if (var12.get() == 1):
        txtTorta.configure( state=NORMAL )
        varTorta.set( "" )

    elif (var12.get() == 0):
        txtTorta.configure( state=DISABLED )
        varTorta.set( "0" )


def chkGelatina():
    if (var13.get() == 1):
        txtGelatina.configure( state=NORMAL )
        varGelatina.set( "" )

    elif (var13.get() == 0):
        txtGelatina.configure( state=DISABLED )
        varGelatina.set( "0" )


def chkCha():
    if (var14.get() == 1):
        txtCha.configure( state=NORMAL )
        varCha.set( "" )

    elif (var14.get() == 0):
        txtCha.configure( state=DISABLED )
        varCha.set( "0" )


def chkRefrigerantes():
    if (var15.get() == 1):
        txtRefrigerantes.configure( state=NORMAL )
        varRefrigerantes.set( "" )

    elif (var15.get() == 0):
        txtRefrigerantes.configure( state=DISABLED )
        varRefrigerantes.set( "0" )


def chkCafe():
    if (var16.get() == 1):
        txtCafe.configure( state=NORMAL )
        varCafe.set( "" )

    elif (var16.get() == 0):
        txtCafe.configure( state=DISABLED )
        varCafe.set( "0" )


def chkSuco():
    if (var17.get() == 1):
        txtSuco.configure( state=NORMAL )
        varSuco.set( "" )

    elif (var17.get() == 0):
        txtSuco.configure( state=DISABLED )
        varSuco.set( "0" )


def chkToddynho():
    if (var18.get() == 1):
        txtToddynho.configure( state=NORMAL )
        varToddynho.set( "" )

    elif (var18.get() == 0):
        txtToddynho.configure( state=DISABLED )
        varToddynho.set( "0" )


def chkBaunilha():
    if (var19.get() == 1):
        txtBaunilha.configure( state=NORMAL )
        varBaunilha.set( "" )

    elif (var19.get() == 0):
        txtBaunilha.configure( state=DISABLED )
        varBaunilha.set( "0" )


def chkMorango():
    if (var20.get() == 1):
        txtMorango.configure( state=NORMAL )
        varMorango.set( "" )

    elif (var20.get() == 0):
        txtMorango.configure( state=DISABLED )
        varMorango.set( "0" )


def chkChocolate():
    if (var21.get() == 1):
        txtChocolate.configure( state=NORMAL )
        varChocolate.set( "" )

    elif (var21.get() == 0):
        txtChocolate.configure( state=DISABLED )
        varChocolate.set( "0" )


def costofmeal():
    meal1 = float( varFritas.get() )
    meal2 = float( varSalada.get() )
    meal3 = float( varHamburguer.get() )
    meal4 = float( varPizza.get() )
    meal5 = float( varPasteis.get() )
    meal6 = float( varMacarronada.get() )
    meal7 = float( varCrepes.get() )
    meal8 = float( varSanduiches.get() )
    meal9 = float( varSorvetes.get() )
    meal10 = float( varBrigadeiro.get() )
    meal11 = float( varPudim.get() )
    meal12 = float( varTorta.get() )
    meal13 = float( varGelatina.get() )
    meal14 = float( varCha.get() )
    meal15 = float( varRefrigerantes.get() )
    meal16 = float( varCafe.get() )
    meal17 = float( varSuco.get() )
    meal18 = float( varToddynho.get() )
    meal19 = float( varBaunilha.get() )
    meal20 = float( varMorango.get() )
    meal21 = float( varChocolate.get() )

    iTotal1 = ((meal1 * 50) + (meal2 * 40) + (meal3 * 100) + (meal4 * 70))
    iTotal2 = ((meal5 * 50) + (meal6 * 30) + (meal7 * 40) + (meal8 * 80))
    iTotal3 = ((meal9 * 140) + (meal10 * 250) + (meal11 * 20) + (meal12 * 40))
    iTotal4 = ((meal13 * 60) + (meal14 * 25) + (meal15 * 30) + (meal16 * 40))
    iTotal5 = ((meal17 * 50) + (meal18 * 50) + (meal19 * 80) + (meal20 * 90) + (meal21 * 60))

    if (var22.get() == "Cash"):
        iAlterar = float( varPagar.get() )
        iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
        iTaxa = (iCost * 3.4) / 100
        iTaxaq = "R$", str( '%.2f' % (iTaxa) )
        varTaxa.set( iTaxaq )

        iCostq = "R$", str( '%.2f' % (iCost) )
        varSubTotal.set( iCostq )
        iTotalq = "R$", str( '%.2f' % ((iCost + iTaxa)) )
        varTotal.set( iTotalq )
        cAlterar = (iAlterar - (iCost + iTaxa))
        cAlterarq = "R$", str( '%.2f' % (cAlterar) )
        varAlterar.set( cAlterarq )
    elif (var22.get() == "Master Card" or "Visa Master Card" or "Debit Card"):
        varPagar.set( "" )
        iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
        iTaxa = (iCost * 3.4) / 100
        iTaxaq = "R$", str( '%.2f'( iTaxa ) )
        varTaxa.set( iTaxaq )
        iCostq = "R$", str( '%.2f' % (iCost) )
        varSubTotal.set( iCostq )
        iTotalq = "R$", str( '%.2f'( (iCost + iTaxa) ) )
        varTotal.set( iTotalq )
        varAlterar.set( "" )


# -------------------------------frame1-----------------------------------------------------------
lblmeal = Label( f1, font=('arial', 18, 'bold'), text="Refeições rápidas\n" )
lblmeal.grid( row=0, column=0 )

Fritas = Checkbutton( f1, text="Fritas\t\tR$ 1,00", variable=var1, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold'), command=chkFritas ).grid( row=1, column=0, sticky=W )
txtFritas = Entry( f1, font=('arial', 18, 'bold'), textvariable=varFritas, width=6, justify='right', state=DISABLED )
txtFritas.grid( row=1, column=1 )

Salada = Checkbutton( f1, text="Saladas\t\tR$ 2,00", variable=var2, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold'), command=chkSalada ).grid( row=2, column=0, sticky=W )
txtSalada = Entry( f1, font=('arial', 18, 'bold'), textvariable=varSalada, width=6, justify='right', state=DISABLED )
txtSalada.grid( row=2, column=1 )

Hamburguer = Checkbutton( f1, text="Hamburguer\tR$ 5,00", variable=var3, onvalue=1, offvalue=0,
                      font=('arial', 18, 'bold'), command=chkHamburguer ).grid( row=3, column=0, sticky=W )
txtHamburguer = Entry( f1, font=('arial', 18, 'bold'), textvariable=varHamburguer, width=6, justify='right', state=DISABLED )
txtHamburguer.grid( row=3, column=1 )

Pizza = Checkbutton( f1, text="Pizza\t\tR$ 3,00", variable=var4, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold'), command=chkPizza ).grid( row=4, column=0, sticky=W )
txtPizza = Entry( f1, font=('arial', 18, 'bold'), textvariable=varPizza, width=6, justify='right', state=DISABLED )
txtPizza.grid( row=4, column=1 )

Pasteis = Checkbutton( f1, text="Pastéis\t\tR$ 2,00", variable=var5, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold'), command=chkPasteis ).grid( row=5, column=0, sticky=W )
txtPasteis = Entry( f1, font=('arial', 18, 'bold'), textvariable=varPasteis, width=6, justify='right', state=DISABLED )
txtPasteis.grid( row=5, column=1 )

# ----------------------------------------------------------------------------------
# lblMeal = Label(f1, font=('arial',20,'bold'), text="\nSandwiches\n")
# lblMeal.grid(row =6, column=0)
# ----------------------------------------------------------------------------------

Macarronada = Checkbutton( f1, text="Macarronada\tR$ 1,00", variable=var6, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold'), command=chkMacarronada ).grid( row=6, column=0, sticky=W )
txtMacarronada = Entry( f1, font=('arial', 18, 'bold'), textvariable=varMacarronada, width=6, justify='right', state=DISABLED )
txtMacarronada.grid( row=6, column=1 )

Crepes = Checkbutton( f1, text="Crepes\t\tR$ 4,00", variable=var7, onvalue=1, offvalue=0,
                        font=('arial', 18, 'bold'), command=chkCrepes ).grid( row=7, column=0, sticky=W )
txtCrepes = Entry( f1, font=('arial', 18, 'bold'), textvariable=varCrepes, width=6, justify='right',
                     state=DISABLED )
txtCrepes.grid( row=7, column=1 )

Sanduiches = Checkbutton( f1, text="Sanduiches\tR$ 3,00", variable=var8, onvalue=1, offvalue=0,
                               font=('arial', 18, 'bold'), command=chkSanduiches ).grid( row=8, column=0,
                                                                                              sticky=W )
txtSanduiches = Entry( f1, font=('arial', 18, 'bold'), textvariable=varSanduiches, width=6, justify='right',
                            state=DISABLED )
txtSanduiches.grid( row=8, column=1 )

lblspace = Label( f1, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n" )
lblspace.grid( row=10, column=0 )

# ------------------------frame2------------------------------------


lblMeal = Label( f2TOP, font=('arial', 18, 'bold'), text="Sobremesas\n" )
lblMeal.grid( row=0, column=0 )

Sorvetes = Checkbutton( f2TOP, text="Sorvetes\t\tR$ 0,50", variable=var9, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), command=chkSorvetes ).grid( row=1, column=0, sticky=W )
txtSorvetes = Entry( f2TOP, font=('arial', 18, 'bold'), textvariable=varSorvetes, width=6, justify='right',
                       state=DISABLED )
txtSorvetes.grid( row=1, column=1 )

Brigadeiro = Checkbutton( f2TOP, text="Brigadeiro\tR$ 0,20", variable=var10, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'), command=chkBrigadeiro ).grid( row=2, column=0, sticky=W )
txtBrigadeiro = Entry( f2TOP, font=('arial', 18, 'bold'), textvariable=varBrigadeiro, width=6, justify='right',
                      state=DISABLED )
txtBrigadeiro.grid( row=2, column=1 )

Pudim = Checkbutton( f2TOP, text="Pudim\t\tR$ 0,10", variable=var11, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold'), command=chkPudim ).grid( row=3, column=0, sticky=W )
txtPudim = Entry( f2TOP, font=('arial', 18, 'bold'), textvariable=varPudim, width=6, justify='right', state=DISABLED )
txtPudim.grid( row=3, column=1 )

Torta = Checkbutton( f2TOP, text="Torta\t\tR$ 0,25", variable=var12, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'), command=chkTorta ).grid( row=4, column=0, sticky=W )
txtTorta = Entry( f2TOP, font=('arial', 18, 'bold'), textvariable=varTorta, width=6, justify='right',
                      state=DISABLED )
txtTorta.grid( row=4, column=1 )

Gelatina = Checkbutton( f2TOP, text="Gelatina\t\tR$ 0,15", variable=var13, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold'), command=chkGelatina ).grid( row=5, column=0, sticky=W )
txtGelatina = Entry( f2TOP, font=('arial', 18, 'bold'), textvariable=varGelatina, width=6, justify='right', state=DISABLED )
txtGelatina.grid( row=5, column=1 )

# --------------------------------frame3--------------------------------------------------------------------------

lblMeal = Label( f3, font=('arial', 18, 'bold'), text="Bebidas\n" )
lblMeal.grid( row=0, column=0 )

Cha = Checkbutton( f3, text="Chá\t\tR$ 0,20", variable=var14, onvalue=1, offvalue=0,
                   font=('arial', 18, 'bold'), command=chkCha ).grid( row=1, column=0, sticky=W )
txtCha = Entry( f3, font=('arial', 18, 'bold'), textvariable=varCha, width=6, justify='right', state=DISABLED )
txtCha.grid( row=1, column=1 )

Refrigerantes = Checkbutton( f3, text="Refrigerantes\tR$ 0,50", variable=var15, onvalue=1, offvalue=0,
                    font=('arial', 18, 'bold'), command=chkRefrigerantes ).grid( row=2, column=0, sticky=W )
txtRefrigerantes = Entry( f3, font=('arial', 18, 'bold'), textvariable=varRefrigerantes, width=6, justify='right', state=DISABLED )
txtRefrigerantes.grid( row=2, column=1 )

Cafe = Checkbutton( f3, text="Café\t\tR$ 0,10", variable=var16, onvalue=1, offvalue=0,
                        font=('arial', 18, 'bold'), command=chkCafe ).grid( row=3, column=0, sticky=W )
txtCafe = Entry( f3, font=('arial', 18, 'bold'), textvariable=varCafe, width=6, justify='right',
                     state=DISABLED )
txtCafe.grid( row=3, column=1 )

Suco = Checkbutton( f3, text="Suco\t\tR$ 0,15", variable=var17, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), command=chkSuco ).grid( row=4, column=0, sticky=W )
txtSuco = Entry( f3, font=('arial', 18, 'bold'), textvariable=varSuco, width=6, justify='right',
                       state=DISABLED )
txtSuco.grid( row=4, column=1 )

Toddynho = Checkbutton( f3, text="Toddynho\tR$ 0,30", variable=var18, onvalue=1, offvalue=0,
                     font=('arial', 18, 'bold'), command=chkToddynho ).grid( row=5, column=0, sticky=W )
txtToddynho = Entry( f3, font=('arial', 18, 'bold'), textvariable=varToddynho, width=6, justify='right', state=DISABLED )
txtToddynho.grid( row=5, column=1 )

# ------------------------------------------------------------------------------------
lblShakes = Label( f3, font=('arial', 20, 'bold'), text="\nShakes\n" )
lblShakes.grid( row=6, column=0 )

Baunilha = Checkbutton( f3, text="Baunilha\t\tR$ 0,80", variable=var19, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'), command=chkBaunilha ).grid( row=7, column=0, sticky=W )
txtBaunilha = Entry( f3, font=('arial', 18, 'bold'), textvariable=varBaunilha, width=6, justify='right',
                      state=DISABLED )
txtBaunilha.grid( row=7, column=1 )

Morango = Checkbutton( f3, text="Morango\t\tR$ 0,80", variable=var20, onvalue=1, offvalue=0,
                            font=('arial', 18, 'bold'), command=chkMorango ).grid( row=8, column=0, sticky=W )
txtMorango = Entry( f3, font=('arial', 18, 'bold'), textvariable=varMorango, width=6, justify='right',
                         state=DISABLED )
txtMorango.grid( row=8, column=1 )

Chocolate = Checkbutton( f3, text="Chocolate\tR$ 0,80", variable=var21, onvalue=1, offvalue=0,
                               font=('arial', 18, 'bold'), command=chkChocolate ).grid( row=9, column=0,
                                                                                              sticky=W )
txtChocolate = Entry( f3, font=('arial', 18, 'bold'), textvariable=varChocolate, width=6, justify='right',
                            state=DISABLED )
txtChocolate.grid( row=9, column=1 )

lblspace = Label( f3, text="\n\n\n\n\n\n\n\n\n" )
lblspace.grid( row=10, column=0 )

# -------------------------------------------------------------------------------------------------------------------------

lblPagamento = Label( f2BOTTOM, font=('arial', 14, 'bold'), text="Pagamento", bd=10, width=16, anchor='w' )
lblPagamento.grid( row=0, column=0 )

lblAlterar = Label( f2BOTTOM, font=('arial', 14, 'bold'), text="Alterar", bd=10, anchor='w' )
lblAlterar.grid( row=0, column=1 )
txtAlterar = Entry( f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varAlterar, width=6, justify='right',
                   state=DISABLED )
txtAlterar.grid( row=0, column=2 )

# --------------------------------------------------------------

'''
self.cmbBxMen1 = Combobox(self, values = data, width = 60)
self.cmbBxMen1.grid(row=0, column=1, padx = 4, pady = 20)
def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


def create_widgets(self):

        data = Application.data

        self.cmbBxMen1 = Combobox(self, values = data, width = 60).grid(row=0, column=1, padx = 4, pady = 20)
        self.btnAdMen = Button(self, text = "Add to Menu", command = self.Add_To_Menu).grid(row=0, column=9, pady = 20, sticky = W)
def Add_To_Menu(self):
        menuItem1 = self.cmbBxMen1.get()
        '''
# ----------------------------------------------------------------
cmbPagamento = ttk.Combobox( f2BOTTOM, textvariable=var22, state='readonly', font=('arial', 10, 'bold'), width=20 )
cmbPagamento['value'] = ('Dinheiro', 'Master Card', 'Visa Card', 'Ouro Card')
cmbPagamento.current( 0 )
cmbPagamento.grid( row=1, column=0 )

lblTaxa = Label( f2BOTTOM, font=('arial', 14, 'bold'), text="Taxa    ", bd=10, anchor='w' )
lblTaxa.grid( row=1, column=1 )
txtTaxa = Entry( f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varTaxa, width=6, justify='right', state=DISABLED )
# txtTaxa = Entry(f2BOTTOM,font=('arial',18, 'bold'), textvariable =var23, width =6, justify='left',state =DISABLED)
txtTaxa.grid( row=1, column=2 )

txtPagar = Entry( f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varPagar, width=6,
                    justify='right' )  # , state =DISABLED)
txtPagar.grid( row=2, column=0 )
lblSubTotal = Label( f2BOTTOM, font=('arial', 14, 'bold'), text="Subtotal", bd=10, width=8, anchor='w' )
lblSubTotal.grid( row=2, column=1 )
txtSubTotal = Entry( f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varSubTotal, width=6, justify='right',
                     state=DISABLED )
txtSubTotal.grid( row=2, column=2 )

lblTotal = Label( f2BOTTOM, font=('arial', 14, 'bold'), text="Total", bd=10, width=6, anchor='w' )
lblTotal.grid( row=3, column=1 )
txtTotal = Entry( f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varTotal, width=6, justify='right',
                  state=DISABLED )
txtTotal.grid( row=3, column=2 )

# ------------------------------------------------------------------------------------------------------------------------------

btnTotal = Button( f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                   text="Total ", command=costofmeal ).grid( row=4, column=0 )
# text="Total" , command = Total).grid(row=4, column=0)
btnIniciar = Button( f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                   text="Iniciar", command=Iniciar ).grid( row=4, column=1 )
btnSair = Button( f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                  text="Sair", command=lambda: iSair() ).grid( row=4, column=2 )
lblspace = Label( f2BOTTOM, text="\n\n\n\n\n\n\n" )
lblspace.grid( row=5, column=0 )

root.mainloop()
