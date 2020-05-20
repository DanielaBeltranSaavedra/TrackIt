

from tkinter import Frame
from tkinter import Label
from tkinter import Button
import tkinter
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import csv

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('fast')

from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib
from PrediccionModel import *
from clasificacion2 import grupoPertence
import pandas as pd
"""
Description: This method creates the results interface in which the user can see 
             the results obtained from the query.
inputs: raizMain - main root of the interface
        raizForm - root of the form interface
        nombre -nName of the person consulted.
        edad - age of the person consulted.
outputs:
""" 
def resultado(raizMain,raizForm,historico,informacion,nombre,edad):     
    
    
    meses = np.array(["Mes 1", "Mes 2", "Mes 3", "Mes 4", "Mes 5", "Mes 6", "Mes 7"])
   
    valores = predict(historico)
    print(len(valores))
    perdida=0
    dif=0
    dif=valores[0]-valores[1]
    if dif>0:
        perdida=dif
    dif=valores[1]-valores[2]
    if dif >0:
        perdida+=dif
    dif=valores[2]-valores[3]
    if dif >0:
        perdida+=dif
    dif=valores[3]-valores[4]
    if dif >0:
        perdida+=dif
    dif=valores[4]-valores[5]
    if dif >0:
        perdida+=dif
    dif=valores[5]-valores[6]
    if dif >0:
        perdida+=dif
    perdida=float(perdida)
    
    information=pd.read_csv(informacion)
    print(information['OIR'])
    grupo= grupoPertence(information['CREDIT SCORE'].iloc[0],information['OIR'].iloc[0],information['FTHF'].iloc[0],information['OLTV'].iloc[0],information['MIP'].iloc[0],information['OCLTV'].iloc[0],information['NOB'].iloc[0],information['OUPB'].iloc[0],information['OLT'].iloc[0])
    Caract=" "
    if grupo==0:
        Caract="Riesgo alto"
    if grupo==1:
         Caract="Riesgo medio"
    if grupo==2:
         Caract="Riesgo bajo"
    if grupo==3:
         Caract="Riesgo alto-medio"
    if grupo==4:
         Caract="Riesgo medio-bajo"
    if grupo==5:
         Caract="Riesgo medio"
    if grupo==6:
         Caract="Riesgo bajo"
    if grupo==7:
         Caract="Riesgo alto-medio"
        
        
    
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
    Label(frameEdad, text=Caract, font=("",10)).grid(row=1,column=1,sticky="w")
    
    Label(frameIzq, text="Valor en riesgo o perdida", font=("",10,"bold")).grid(row=3,column=0,sticky="w")
    Label(frameIzq, text=perdida, font=("",10)).grid(row=4,column=0,sticky="w")
    
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
    #graPre.plot(meses, inter_super, color='red')
    
    inter_infer = np.empty(tam)
    for i in range(0,tam):
        inter_infer[i] = resul[i]*-1
    #graPre.plot(meses, inter_super, color='red')
        
    for i, txt in enumerate(valores):
        graPre.annotate(txt, (meses[i], valores[i]))
    #graPre.plot(meses, inter_infer, color='red')
    
    graPre.set_title ("Predicción de pago en el tiempo", fontsize=16)
    graPre.set_ylabel("Valor pagado", fontsize=14)
    graPre.set_xlabel("Cuotas mesuales", fontsize=14)
    graPre.set_ylim([np.amin(valores)-100,np.amax(valores)+100])

    canvasPre = FigureCanvasTkAgg(figPre, master=frameDer)
    canvasPre.get_tk_widget().grid(row=0, column=0, padx=5)
    canvasPre.draw()
    