

from tkinter import PhotoImage
from tkinter import Tk 
from tkinter import Frame
from tkinter import Button
from tkinter import Label
from tkinter import Menu
from Glosario import ventanaAyuda
from Formulario import formulario
from ventanaArchivo import ayudaArchivo
from clasificacion2 import grupoPertence
from DTO import Origination

from cercanos import *
#from Prediccion import prediccion
import pandas as pd


raizMain = Tk()
raizMain.geometry("800x600")
raizMain.title("Sistema Trackit")
r=pd.read_csv("..\\Repositorio de datos\\HistoricalInformation.csv", nrows=(8181111,16362222‬))
print(r['current_actual_upb'])
print("holiwi")
barraMenu = Menu(raizMain)
raizMain.config(menu=barraMenu)

inicioMenu = Menu(barraMenu) 
inicioMenu.add_command(label="salir", command=raizMain.destroy)

ayudaMenu = Menu(barraMenu)
ayudaMenu.add_command(label="variables de entrada", command=lambda:ventanaAyuda(raizMain))
ayudaMenu.add_command(label="Subir archivo", command=lambda:ayudaArchivo(raizMain))

barraMenu.add_cascade(label="Inicio",menu=inicioMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

frameIni = Frame(raizMain)
frameIni.pack()

frameHead = Frame(frameIni)
frameHead.grid(row=0 , column=0, padx=0,pady=15)
presentaFra = Frame(frameHead, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd= 5)
presentaFra.grid(row=0 , column=0)
logoTrackit = PhotoImage(file="logos/logoTrackit.png")
Label(presentaFra, image=logoTrackit).grid(row=0,column=0,padx=10)

logoJaveriana = PhotoImage(file="logos/logoJaveriana.png")
Label(presentaFra, image=logoJaveriana).grid(row=0,column=2,padx=10)

tituloFra = Frame(presentaFra)
tituloFra.grid(row=0, column=1)
tituloLa = Label(tituloFra,text="Sistema de predicción de pagos", font=("Times New Roman",18,"bold","italic")).grid(row=0, column=0, padx=5)
tituloLa = Label(tituloFra,text="para creditos hipotecarios", font=("Times New Roman",18,"bold", "italic")).grid(row=1, column=0, padx=5)

frameAmar = Frame(frameHead, background="#FFFB00", width="715", height="5")
frameAmar.grid(row=1, column=0)
frameAmar = Frame(frameHead, background="#FFFFFF", width="715", height="5")
frameAmar.grid(row=2, column=0)
frameAmar = Frame(frameHead, background="#0D6AE1", width="715", height="5")
frameAmar.grid(row=3, column=0)

frameAmar = Frame(frameHead,width="715", height="120")
frameAmar.grid(row=4, column=0)

bodyFra = Frame(frameIni)
bodyFra.grid(row=4, column=0)
ingresarBut = Button(bodyFra, text="Ingresar Información", command=lambda:formulario(raizMain,r), width=20, height=2, bg="#AED6F1")
ingresarBut.grid(row=0, column=0, pady=5)
frameInter = Frame(bodyFra,width="715", height="120")
frameInter.grid(row=1, column=0)
salirBut = Button(bodyFra, text="Salir", command=raizMain.destroy, width=10, background="#F70A0A")
salirBut.grid(row=2, column=0, pady=5)

raizMain.mainloop()