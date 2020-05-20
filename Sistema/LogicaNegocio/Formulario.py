


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

from clasificacion2 import grupoPertence
from DTO import Origination
from readFiles import readFile
from cercanos import *

#from Prediccion import prediccion
import pandas as pd

"""
Description: This method builds the interface of the form so that the user can enter 
             the values ​​of the person to be consulted.
inputs:
outputs:
""" 
def formulario(raizMain,r):
    
    data=readFile()
    enteredPersonn=enteredPerson("F109Q1595501",data)
    print(enteredPersonn[0].cs)
    class Archivo:
        nombre = ""
           
    archivo=Archivo()
    raizForm = tkinter.Toplevel(raizMain)
    raizMain.iconify()
    raizForm.title("Ingreso de datos")
    raizForm.geometry("800x600")
    validar = raizForm.register(es_valido_campo)
    validar_ConPun = raizForm.register(es_valido_campo_con_punto)
    
    barraMenu = Menu(raizForm)
    raizForm.config(menu=barraMenu)
    
    inicioMenu = Menu(barraMenu) 
    inicioMenu.add_command(label="salir", command=lambda:salirForm(raizMain,raizForm))
    
    ayudaMenu = Menu(barraMenu)
    ayudaMenu.add_command(label="variables de entrada", command=lambda:ventanaAyuda(raizForm))
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
    
    Label(frameForm, text="Credit Score *", font=("",10)).grid(row=1, column=0, sticky="w", padx=(50,2), pady=5)
    CreSText = Entry(frameForm, validate="key", validatecommand = (validar, "%P"))
    CreSText.grid(row=1, column=1, pady=5)
    
    Label(frameForm, text="First homebuyer flag *", font=("",10)).grid(row=1, column=2, sticky="w", padx=(50,2), pady=5)
    FHFcombo = ttk.Combobox(frameForm, state="readonly", width=17)
    FHFcombo["values"] = ["Y (yes)","N (No)","9"]
    FHFcombo.grid(row=1, column=3, padx=(2,50), pady=(5))
    
    Label(frameForm, text="Maturity date (YYYY/MM)*", font=("",10)).grid(row=2, column=0, sticky="w", padx=(50,2), pady=5)
    frameFecha = Frame(frameForm)
    frameFecha.grid(row=2, column=1, pady=(5))
    MDateYText = Entry(frameFecha, validate="key", validatecommand = (validar, "%P"), width=8)
    MDateYText.grid(row=0, column=0)
    Label(frameFecha, text=" / ", font=("",10)).grid(row=0, column=1)
    MDateMText = Entry(frameFecha, validate="key", validatecommand = (validar, "%P"), width=8)
    MDateMText.grid(row=0, column=2)
    
    Label(frameForm, text="Metropolitan statical area *", font=("",10)).grid(row=2, column=2, sticky="w", padx=(50,2), pady=5)
    MSAText = Entry(frameForm, validate="key", validatecommand = (validar, "%P"))
    MSAText.grid(row=2, column=3, padx=(2,50), pady=(5))
    
    Label(frameForm, text="Mortage insurance percentage *", font=("",10)).grid(row=3, column=0, sticky="w", padx=(50,2), pady=5)
    MIPText = Entry(frameForm, validate="key", validatecommand = (validar, "%P"))
    MIPText.grid(row=3, column=1, pady=(5))
    
    Label(frameForm, text="Occupa NCY status *", font=("",10)).grid(row=3, column=2, sticky="w", padx=(50,2), pady=5)
    NCYcombo = ttk.Combobox(frameForm, state="readonly", width=17)
    NCYcombo["values"] = ["P (Primary Residence)","I (Investment Property)","S (Second Home)", "9 (Not Avalaible)"]
    NCYcombo.grid(row=3, column=3, padx=(2,50), pady=(5))
    
    Label(frameForm, text="Original combined loan to value *", font=("",10)).grid(row=4, column=0, sticky="w", padx=(50,2), pady=5)
    OCLVText = Entry(frameForm, validate="key", validatecommand = (validar, "%P"))
    OCLVText.grid(row=4, column=1, pady=(5))
    
    Label(frameForm, text="Original debit to income ratio *", font=("",10)).grid(row=4, column=2, sticky="w", padx=(50,2), pady=5)
    ODIRText = Entry(frameForm, validate="key", validatecommand = (validar, "%P"))
    ODIRText.grid(row=4, column=3, padx=(2,50), pady=(5))
    
    Label(frameForm, text="Loan purpose *", font=("",10)).grid(row=5, column=0, sticky="w", padx=(50,2), pady=5)
    LoanPcombo = ttk.Combobox(frameForm, state="readonly", width=17)
    LoanPcombo["values"] = ["P (Compra)","C (Retirada)","N (Sin retiro de efectivo)", "R (No especificado)", "9 (No disponible)"]
    LoanPcombo.grid(row=5, column=1, pady=(5))
    
    Label(frameForm, text="Number of borrowers *", font=("",10)).grid(row=5, column=2, sticky="w", padx=(50,2), pady=5)
    NumBText = Entry(frameForm, validate="key", validatecommand = (validar, "%P"))
    NumBText.grid(row=5, column=3, padx=(2,50), pady=(5))
    
    Label(frameForm, text="Postal Code *", font=("",10)).grid(row=6, column=0, sticky="w", padx=(50,2), pady=5)
    LoanPText = Entry(frameForm, validate="key", validatecommand = (validar, "%P"))
    LoanPText.grid(row=6, column=1, pady=(5))
    
    Label(frameForm, text="Original interest rate *", font=("",10)).grid(row=6, column=2, sticky="w", padx=(50,2), pady=5)
    oirText = Entry(frameForm, validate="key", validatecommand = (validar_ConPun, "%P"))
    oirText.grid(row=6, column=3, padx=(2,50), pady=(5))
    
    Label(frameForm, text="Original loan to value *", font=("",10)).grid(row=7, column=0, sticky="w", padx=(50,2), pady=5)
    oltvText = Entry(frameForm, validate="key", validatecommand = (validar, "%P"))
    oltvText.grid(row=7, column=1, pady=(5))
    
    Label(frameForm, text="Original UPB *", font=("",10)).grid(row=7, column=2, sticky="w", padx=(50,2), pady=5)
    
    oupbText = Entry(frameForm, validate="key", validatecommand = (validar, "%P"))
    oupbText.grid(row=8, column=1, pady=(5))
    Label(frameForm, text="Original loan term *", font=("",10)).grid(row=8, column=0, sticky="w", padx=(50,2), pady=5)
    oltText = Entry(frameForm, validate="key", validatecommand = (validar, "%P"))
    oltText.grid(row=8, column=3, padx=(2,50), pady=(5))
    
    
    Label(frameForm, text="Property state *", font=("",10)).grid(row=8, column=2, sticky="w", padx=(50,2), pady=5)
    psText = Entry(frameForm)
    psText.grid(row=9, column=1, pady=(5))
    Label(frameForm, text="Loan sequence number *", font=("",10)).grid(row=9, column=0, sticky="w", padx=(50,2), pady=5)
    
    lsqnText = Entry(frameForm)
    lsqnText.grid(row=9, column=3, padx=(2,50), pady=(5))
       
    frameBody = Frame(frameIniForm)
    frameBody.grid(row=2 , column=0, padx=0,pady=15)
    volverBut = Button(frameBody, text="Volver", command=lambda:Volver(raizMain,raizForm), bg="#AED6F1", width=10, height=2)
    volverBut.grid(row=1,column=0, padx=(60), pady=(20))
    upFileBut = Button(frameBody, text="Subir archivo", command=lambda:subir_archivo(archivo), bg="#5DADE2", width=15, height=2)
    upFileBut.grid(row=1,column=3, padx=(60), pady=(20))
    sudmitBut = Button(frameBody, text="Guardar y consultar", command=lambda:guardarActualizar(raizMain,raizForm,archivo,nombreText.get(),edadText.get(),float(CreSText.get()),float(oirText.get()),FHFcombo.get(),float(OCLVText.get()),float(MIPText.get()),float(oltvText.get()),float(NumBText.get()),float(oupbText.get()),float(oltText.get()),data,lsqnText.get(),r), bg="#58D68D", width=20, height=2)
    sudmitBut.grid(row=1, column=5, padx=(60), pady=(20))
    
    raizForm.update()
    can.config(scrollregion=can.bbox("all"))

"""
Description: This method saves the path in which the file is contained with the
             payment behavior of the person to consult.
inputs: archivo - class in which the file name will be saved
outputs:
"""    
def subir_archivo(archivo):
    archivo.nombre = filedialog.askopenfilename(title="abrir", filetypes=(("CSV delimitado por comas","*.csv"),))
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
        numero = float(char)
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
def guardarActualizar(raizMain,raizForm,archivo,nombre,edad,cs,oirT,FHF,ocltv,MIP,oltv,nob,oupb,olt,data,lsqn,r):
    if archivo.nombre == "":
        messagebox.showerror("Error al leer archivo","Ingrese un archivo excel con los datos de pago. Si requiere ayuda consulte en la barra de menu 'Ayuda/Subir archivo'")
    else:
        #print(len(data))
        #personIngresada=enteredPerson(lsqn,data)
        #print(personIngresada[0].cs)
        #grupClass=grupoPertence(cs,oirT,FHF,ocltv,MIP,oltv,nob,oupb,olt)
        #print(grupClass)
        
        historicalMyModel=r.iloc[:8000]
        dataMyModel=divDb(data,historicalMyModel)
        