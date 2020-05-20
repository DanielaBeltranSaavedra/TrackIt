

from tkinter import Frame
from tkinter import Label
from tkinter import Scrollbar
from tkinter import Canvas
import tkinter
"""
Description: This method builds the interface of the steps to follow to upload a 
             file with the payment behavior of the person consulted
inputs: raizMain - main root of the interface
outputs:
""" 
def ayudaArchivo(raizMain):
        
    raizVetana = tkinter.Toplevel(raizMain)
    raizVetana.title("Definición de variables")
    raizVetana.geometry("760x600")
    
    scrollbar = Scrollbar(raizVetana)
    can = Canvas(raizVetana, yscrollcomman=scrollbar.set)
    scrollbar.config(command=can.yview)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    
 #Frame principal   
    frameIniForm = Frame(can)
    can.pack(side="left", fill="both", expand=True)
    can.create_window(0,0,window=frameIniForm,anchor='nw')
    
    frameHead = Frame(frameIniForm)
    frameHead.grid(row=0 , column=0, padx=0,pady=15)
    
#Frame de logos y titulo  
    presentaFra = Frame(frameHead, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd= 5)
    presentaFra.grid(row=0 , column=0, padx=10)
    
    tituloFra = Frame(presentaFra)
    tituloFra.grid(row=0, column=0)
    Label(tituloFra,text="Ingresar información del comportamineto de pago", font=("Times New Roman",18,"bold","italic"),width=49).grid(row=0, column=0, padx=5)
#Frame de banderas
    frameAmar = Frame(frameHead, background="#FFFB00", width="715", height="5")
    frameAmar.grid(row=1, column=0)
    frameAmar = Frame(frameHead, background="#FFFFFF", width="715", height="5")
    frameAmar.grid(row=2, column=0)
    frameAmar = Frame(frameHead, background="#0D6AE1", width="715", height="5")
    frameAmar.grid(row=3, column=0)

    frameExpli = Frame(frameIniForm)
    frameExpli.grid(row=1, column=0)
    
    Label(frameExpli, text="Los siguientes pasos describen el proceso para ingresar información", font=("",10)).grid(row=0,column=0)
    Label(frameExpli, text="de una persona con respecto a su comportamiento de pago.", font=("",10)).grid(row=1,column=0)
    
    Label(frameExpli, text="Paso 1:", font=("",10,"bold")).grid(row=2,column=0,sticky="w", padx=5, pady=5)
    Label(frameExpli, text="Con la ayuda de la herramiento Microsoft Excel creee un archivo en formato .csv (Separado por comas).", font=("",10)).grid(row=3, column=0,sticky="w", padx=5, pady=5)    
    
    Label(frameExpli, text="Paso 2:", font=("",10,"bold")).grid(row=4,column=0,sticky="w", padx=5, pady=5)
    Label(frameExpli, text="Ingrese solo el valor del comportamineto de pago mes a mes de manera vertical en la columana 'A' del documento.", font=("",10)).grid(row=5, column=0,sticky="w", padx=5, pady=5) 
    
    Label(frameExpli, text="Paso 3:", font=("",10,"bold")).grid(row=6,column=0,sticky="w", padx=5, pady=5)
    Label(frameExpli, text="Ingrese la información de manera ascendente conforme al tiempol ejemplo: Mes 1, Mes 2 ... Mes n.", font=("",10)).grid(row=7, column=0,sticky="w", padx=5, pady=5) 
    
    Label(frameExpli, text="Paso 4:", font=("",10,"bold")).grid(row=8,column=0,sticky="w", padx=5, pady=5)
    Label(frameExpli, text="Guarde el documento asegurandoce que el formato a guardar es de tipo .csv.", font=("",10)).grid(row=9, column=0,sticky="w", padx=5, pady=5) 
    
    Label(frameExpli, text="Paso 5:", font=("",10,"bold")).grid(row=10,column=0,sticky="w", padx=5, pady=5)
    Label(frameExpli, text="Selecione el boton 'Subir archivo' del formulario y busque el documento guardado anteriormente.", font=("",10)).grid(row=11, column=0,sticky="w", padx=5, pady=5) 
    
    Label(frameExpli, text="Paso 6:", font=("",10,"bold")).grid(row=12,column=0,sticky="w", padx=5, pady=5)
    Label(frameExpli, text="Selecione el boton 'Abrir'.", font=("",10)).grid(row=13, column=0,sticky="w", padx=5, pady=5) 
        
    raizVetana.update()
    can.config(scrollregion=can.bbox("all"))