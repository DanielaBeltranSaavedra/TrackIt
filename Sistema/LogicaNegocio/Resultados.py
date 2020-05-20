

from tkinter import Frame
from tkinter import Label
from tkinter import Button
import tkinter
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Pronostico import prediccion

"""
Description: This method creates the results interface in which the user can see 
             the results obtained from the query.
inputs: raizMain - main root of the interface
        raizForm - root of the form interface
        nombre -nName of the person consulted.
        edad - age of the person consulted.
outputs:
""" 
def resultado(raizMain,raizForm,archivo,nombre,edad,cs,oirT,FHF,ocltv,MIP,oltv,nob,oupb,olt,data,lsqn,r):        
    
    meses = np.array(["Mes 1", "Mes 2", "Mes 3", "Mes 4", "Mes 5", "Mes 6", "Mes 7"])
    valores = prediccion()
    
    #parte grafica
    raizResult = tkinter.Toplevel(raizMain)
    raizForm.destroy()
    raizResult.title("Sistema Trackit")
    
    frameBack = Frame(raizResult)
    frameBack.pack()
    frameHead = Frame(frameBack)
    frameHead.grid(row=0 , column=0, padx=0,pady=15)
    
    #Frame de logos y titulo  
    presentaFra = Frame(frameHead, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd= 5)
    presentaFra.grid(row=0 , column=0)
    
    tituloFra = Frame(presentaFra)
    tituloFra.grid(row=0, column=0)
    Label(tituloFra,text="Sistema de predicción de pagos", font=("Times New Roman",18,"bold","italic"),width=49).grid(row=0, column=0, padx=5)
    Label(tituloFra,text="para creditos hipotecarios", font=("Times New Roman",18,"bold", "italic")).grid(row=1, column=0, padx=5)
        
    frameAmar = Frame(frameHead, background="#FFFB00", width="715", height="5")
    frameAmar.grid(row=1, column=0)
    frameAmar = Frame(frameHead, background="#FFFFFF", width="715", height="5")
    frameAmar.grid(row=2, column=0)
    frameAmar = Frame(frameHead, background="#0D6AE1", width="715", height="5")
    frameAmar.grid(row=3, column=0)
          
    frameBody = Frame(frameBack)
    frameBody.grid(row=1, column=0, sticky="w", pady=30)
    frameIzq = Frame(frameBody)
    frameIzq.grid(row=1, column=0, padx=5, pady=40, sticky="w")
    frameDer = Frame(frameBody)
    frameDer.grid(row=1, column=1, sticky="w")

    Label(frameIzq, text="Nombre", font=("",10,"bold")).grid(row=0,column=0,sticky="w")
    Label(frameIzq, text=nombre, font=("",10)).grid(row=1,column=0,sticky="w")
    
    frameEdad = Frame(frameIzq)
    frameEdad.grid(row=2, column=0, sticky="w")
    Label(frameEdad, text="Edad", font=("",10,"bold")).grid(row=0,column=0,sticky="w")
    Label(frameEdad, text=edad, font=("",10,)).grid(row=1,column=0,sticky="w")
    Label(frameEdad, text="Perfil de riesgo", font=("",10,"bold")).grid(row=0,column=1,sticky="w")
    Label(frameEdad, text="Alto riesgo", font=("",10)).grid(row=1,column=1,sticky="w")
    
    Label(frameIzq, text="Valor total del credito", font=("",10,"bold")).grid(row=3,column=0,sticky="w")
    Label(frameIzq, text="$193000", font=("",10)).grid(row=4,column=0,sticky="w")
    Label(frameIzq, text="Valor en riesgo o perdida", font=("",10,"bold")).grid(row=5,column=0,sticky="w")
    Label(frameIzq, text="$178381", font=("",10)).grid(row=6,column=0,sticky="w")
    
    Button(frameIzq, text="Volver", bg="#AED6F1", width=10, height=1, command=lambda:VolverForm(raizResult,raizMain)).grid(row=7, column=0, pady=(20,0))
    
    graficar(valores,meses,frameDer)
    
    salir = Button(frameDer, text="Salir", command=lambda:Salir(raizResult,raizMain), width=10, background="#F70A0A")
    salir.grid(row=1, column=1, padx=20, pady=(10,10), sticky="e")
"""
Description: Method to return to the form.
inputs: raizResult - main root of results interface
        raizMain - main root of the interface
outputs:
""" 
def VolverForm(raizResult,raizMain):
    raizResult.destroy()
    raizMain.deiconify()
"""
Description: Method to exit the program
inputs: raizResult - main root of results interface
        raizMain - main root of the interface
outputs:
"""     
def Salir(raizResult,raizMain):
    raizResult.destroy()
    raizMain.destroy()
"""
Description: Method to graphically represent the results of the person consulted 
             and the closest individual
inputs: valores - Array with the values ​​of the payment behavior of the person consulted
        meses - Array with the texts of the seven predicted
        frameDer - Graphics container
outputs:
"""  
def graficar(valores,meses,frameDer):
    
    desv = np.std(valores)
    tam = len(valores)
    resul = np.empty(tam)
    for i in range(0,tam):
        resul[i] = valores[i] + (1.26*desv)
    
    figPre = Figure(figsize=(8,6))
    graPre = figPre.add_subplot(111)
    graPre.scatter(meses,valores,color='red')
    graPre.plot(meses, valores, color='blue')
    
    inter_super = np.empty(tam)
    for i in range(0,tam):
        inter_super[i] = resul[i]*2
    graPre.plot(meses, inter_super, color='red')
    
    inter_infer = np.empty(tam)
    for i in range(0,tam):
        inter_infer[i] = resul[i]*-1
    graPre.plot(meses, inter_super, color='red')
    
    for i, txt in enumerate(valores):
        graPre.annotate(txt, (meses[i], valores[i]))
    graPre.plot(meses, inter_infer, color='red')
    
    graPre.set_title ("Predicción de pago en el tiempo", fontsize=16)
    graPre.set_ylabel("Valor pagado", fontsize=14)
    graPre.set_xlabel("Cuotas mesuales", fontsize=14)
    graPre.set_ylim([np.amin(inter_infer-100),np.amax(inter_super+100)])

    canvasPre = FigureCanvasTkAgg(figPre, master=frameDer)
    canvasPre.get_tk_widget().grid(row=0, column=0, padx=5)
    canvasPre.draw()
    
    figCerca = Figure(figsize=(8,6))
    graCerca = figCerca.add_subplot(111)
    graCerca.scatter(meses,valores,color='red')
    graCerca.plot(meses, valores, color='yellow')
    
    graCerca.set_title ("Comportamiento de pago del cercano", fontsize=16)
    graCerca.set_ylabel("Valor pagado", fontsize=14)
    graCerca.set_xlabel("Cuotas mesuales", fontsize=14)
    graCerca.set_ylim([np.amin(inter_infer-100),np.amax(inter_super+100)])
    
    canvasPre = FigureCanvasTkAgg(figCerca, master=frameDer)
    canvasPre.get_tk_widget().grid(row=0, column=1, padx=10)
    canvasPre.draw()