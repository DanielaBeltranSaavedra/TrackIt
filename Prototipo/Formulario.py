# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 01:32:52 2020

@author: Miguel Barón

Description: Main form where the user can enter the data from the main query to run the prediction
"""


from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Menu
from Glosario import ventanaAyuda
from tkinter import Scrollbar
from tkinter import Canvas
from tkinter import ttk
from tkinter import messagebox
import tkinter
from Resultados import resultado
from ventanaArchivo import ayudaArchivo
from tkinter import filedialog

"""
Description: This method builds the interface of the form so that the user can enter 
             the values ​​of the person to be consulted.
inputs:
outputs:
""" 
def formulario(raizMain):

    class Archivo:
        nombre = ""
           
    archivoHisto=Archivo()
    archivoInfo = Archivo()
    
    raizForm = tkinter.Toplevel(raizMain)
    raizMain.iconify()
    raizForm.title("Ingreso de datos")
    raizForm.geometry("800x600")
    validar = raizForm.register(es_valido_campo)
    validar_ConPun = raizForm.register(es_valido_campo_con_punto)
    
    barraMenu = Menu(raizForm)
    raizForm.config(menu=barraMenu)
    
    inicioMenu = Menu(barraMenu) 
    inicioMenu.add_command(label="Salir", command=lambda:salirForm(raizMain,raizForm))
    
    ayudaMenu = Menu(barraMenu)
    ayudaMenu.add_command(label="Variables de entrada", command=lambda:ventanaAyuda(raizForm))
    ayudaMenu.add_command(label="Subir archivo", command=lambda:ayudaArchivo(raizForm))
    
    barraMenu.add_cascade(label="Inicio",menu=inicioMenu)
    barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)
 
    scrollbar = Scrollbar(raizForm)
    can = Canvas(raizForm, yscrollcomman=scrollbar.set)
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
    presentaFra.grid(row=0 , column=0)
    
    tituloFra = Frame(presentaFra)
    tituloFra.grid(row=0, column=0)
    Label(tituloFra,text="Sistema de predicción de pagos", font=("Times New Roman",18,"bold","italic"),width=49).grid(row=0, column=0, padx=5)
    Label(tituloFra,text="para creditos hipotecarios", font=("Times New Roman",18,"bold", "italic")).grid(row=1, column=0, padx=5)

#Frame de banderas
    frameAmar = Frame(frameHead, background="#FFFB00", width="715", height="5")
    frameAmar.grid(row=1, column=0)
    frameAmar = Frame(frameHead, background="#FFFFFF", width="715", height="5")
    frameAmar.grid(row=2, column=0)
    frameAmar = Frame(frameHead, background="#0D6AE1", width="715", height="5")
    frameAmar.grid(row=3, column=0)

    frameExpli = Frame(frameIniForm)
    frameExpli.grid(row=1, column=0)
    
    Label(frameExpli, text="Ingresar información de una persona para ser consultada en el sistema.", font=("",10)).grid(row=0,column=0)
    Label(frameExpli, text="Los campos marcados con * corresponden a campos obligatorios.", font=("",10)).grid(row=1,column=0)

#Frame del formulario    
    frameForm = Frame(frameExpli)
    frameForm.grid(row=2, column=0)
    
    Label(frameForm, text="Nombre *", font=("",10)).grid(row=0, column=0, sticky="w", padx=(50,2), pady=(30,5))
    nombreText = Entry(frameForm)
    nombreText.grid(row=0, column=1, pady=(30,5))
    
    Label(frameForm, text="Edad *", font=("",10)).grid(row=0, column=2, sticky="w", padx=(50,2), pady=(30,5))
    edadText = Entry(frameForm)
    edadText.grid(row=0, column=3, padx=(2,50), pady=(30,5))
          
    frameBody = Frame(frameIniForm)
    frameBody.grid(row=2 , column=0, padx=0,pady=15)
    volverBut = Button(frameBody, text="Volver", command=lambda:Volver(raizMain,raizForm), bg="#AED6F1", width=10, height=2)
    volverBut.grid(row=1,column=0, padx=(10), pady=(20))
    infoBut = Button(frameBody, text="Subir información", command=lambda:subir_Informacion(archivoInfo), bg="#58D68D", width=20, height=2)
    infoBut.grid(row=1, column=2, padx=(10), pady=(20))
    histoBut = Button(frameBody, text="Subir archivo historico", command=lambda:subir_archivo_historico(archivoHisto), bg="#5DADE2", width=20, height=2)
    histoBut.grid(row=1,column=4, padx=(10), pady=(20))
    sudmitBut = Button(frameBody, text="Guardar y consultar", command=lambda:guardarActualizar(raizMain,raizForm,archivoHisto,archivoInfo,nombreText.get(),edadText.get()), bg="#58D68D", width=20, height=2)
    sudmitBut.grid(row=1, column=6, padx=(10), pady=(20))
    
    raizForm.update()
    can.config(scrollregion=can.bbox("all"))

"""
Description: This method saves the path in which the file is contained with the
             payment behavior of the person to consult.
inputs: archivo - class in which the file name will be saved
outputs:
"""    
def subir_archivo_historico(archivoHisto):
    archivoHisto.nombre = filedialog.askopenfilename(title="abrir", filetypes=(("CSV delimitado por comas","*.csv"),))
"""
Description: This method saves the path in which the file is contained with the
             payment behavior of the person to consult.
inputs: archivo - class in which the file name will be saved
outputs:
"""    
def subir_Informacion(archivoInfo):
    archivoInfo.nombre = filedialog.askopenfilename(title="abrir", filetypes=(("CSV delimitado por comas","*.csv"),))
"""
Description: Method to return to the main interface
inputs: raizMain - main root of the interface
        raizForm - root of the form interface
outputs:
"""    
def Volver(raizMain,raizForm):
    raizForm.destroy()
    raizMain.deiconify()
"""
Description: Method to exit the program
inputs: raizMain - main root of the interface
        raizForm - root of the form interface
outputs:
"""        
def salirForm(raizMain,raizForm):
    raizForm.destroy()
    raizMain.destroy()
"""
Description: Method to validate that the value entered by the user is numeric
inputs: char - string with the value entered by the user
outputs: Returns if the entry is valid or not in values ​​1 or 0
"""    
def es_valido_campo(char):
    if char.isdigit() :
        return True
    else:
        messagebox.showerror("Valor ingresado erroneo","Ingrese solo valores numericos")
        return False
"""
Description: Method to validate that the value entered by the user is numeric
inputs: char - string with the value entered by the user
outputs: Returns if the entry is valid or not in values ​​1 or 0
"""    
def es_valido_campo_con_punto(char):
    try:
        float(char)
        return True
    except ValueError:
        messagebox.showerror("Valor ingresado erroneo","Ingrese solo valores numericos")
        return False
"""
Description: method of saving and passing the values entered by the user to the 
             results interface.
inputs: raizMain - main root of the interface
        raizForm - root of the form interface
        archivo - path of the file where the payment behavior of the person to be 
                  consulted is stored.
outputs:
""" 
def guardarActualizar(raizMain,raizForm,arcHistorico,arcInfor,nombre,edad):
    if arcHistorico.nombre == "" or arcInfor.nombre == "":
        messagebox.showerror("Error al leer archivo","Ingrese un archivo excel con los datos de pago. Si requiere ayuda consulte en la barra de menu 'Ayuda/Subir archivo'")
    else:
        resultado(raizMain,raizForm,arcHistorico.nombre,arcInfor.nombre,nombre,edad)