

from tkinter import Frame
from tkinter import Label
from tkinter import Scrollbar
from tkinter import Canvas
import tkinter
"""
Description: This method builds the glossary interface
inputs: raizMain - main root of the interface
outputs:
""" 
def ventanaAyuda(raizMain):
    raizVetana = tkinter.Toplevel(raizMain)
    raizVetana.title("Definición de variables")
    raizVetana.geometry("750x600")
    
    scrollbar = Scrollbar(raizVetana)
    can = Canvas(raizVetana, yscrollcomman=scrollbar.set)
    scrollbar.config(command=can.yview)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
       
    frameHead = Frame(can)
    can.pack(side="left", fill="both", expand=True)
    can.create_window(0,0,window=frameHead,anchor='nw')
    
    Label(frameHead, wraplength=300,text="Variable", font=("",10,"bold")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="Definición",font=("",10,"bold")).grid(row=0, column=1, sticky="w", padx=5, pady=5)
    
    Label(frameHead, wraplength=100,text="C", font=("",10,"bold")).grid(row=1, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Credit score").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="Resume la solvencia crediticia del prestatario, que puede ser indicativa de la probabilidad de que el prestatario reembolse oportunamente obligaciones futuras. Generalmente, el puntaje de crédito divulgado es el puntaje conocido en el momento de adquisición y es el puntaje utilizado para originar la hipoteca.").grid(row=2, column=1, sticky="w", padx=5, pady=5)
    
    Label(frameHead, wraplength=100,text="F", font=("",10,"bold")).grid(row=3, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="First time homebuyer flag").grid(row=4, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="Indica si el prestatario, o uno de un grupo de prestatarios, es un individuo que (1) está comprando la propiedad hipotecada, (2) residirá en la propiedad hipotecada como residencia principal y (3) no tenían interés de propiedad (único o conjunto) en un propiedad residencial durante el período de tres años anterior a la fecha de la compra de la propiedad hipotecada. ").grid(row=4, column=1, padx=5, pady=5, sticky="w")
    
    Label(frameHead, wraplength=300,text="L", font=("",10,"bold")).grid(row=5, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Loan purpose").grid(row=6, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="Indica si el préstamo hipotecario es una hipoteca de refinanciamiento de retiro de efectivo, una hipoteca de refinanciamiento sin retiro de efectivo o una hipoteca de compra.").grid(row=6, column=1, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Loan sequence number").grid(row=7, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="Identificador único asignado a cada préstamo.").grid(row=7, column=1, sticky="w", padx=5, pady=5)
    
    Label(frameHead, wraplength=500,text="M", font=("",10,"bold")).grid(row=8, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Maturity date").grid(row=9, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="El mes en que el pago mensual final en la hipoteca está programada para hacerse como se indica en el original nota de hipoteca").grid(row=9, column=1, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Metropolitan statistical area").grid(row=10, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="Es el área estadística metropolitana basada en el censo de 2010 (para marzo de 2013 y mayo de 2013 publicaciones) y el censo de 2013 (para las publicaciones de agosto de 2013 y diciembre de 2013) datos.").grid(row=10, column=1, sticky="w", padx=5, pady=5)     
    Label(frameHead, wraplength=300,text="Mortage insurance percentage").grid(row=11, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="El porcentaje de cobertura de pérdidas en el préstamo, en el momento en que Freddie Mac compra el préstamo hipotecario que una aseguradora hipotecaria está proporcionando para cubrir pérdidas incurrido como resultado de un incumplimiento en el préstamo.").grid(row=11, column=1, sticky="w", padx=5, pady=5)
    
    Label(frameHead, wraplength=100,text="N", font=("",10,"bold")).grid(row=12, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Number of borrowers").grid(row=13, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="El número de prestatario (s) que están obligados a pagar la nota de la hipoteca asegurada por la hipoteca propiedad.").grid(row=13, column=1, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Number of borrowers").grid(row=14, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="El número de prestatario (s) que están obligados a pagar la nota de la hipoteca asegurada por la hipoteca propiedad.").grid(row=14, column=1, sticky="w", padx=5, pady=5)
    
    Label(frameHead, wraplength=100,text="O", font=("",10,"bold")).grid(row=15, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Occupancy status").grid(row=16, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="Denota si el tipo de hipoteca es ocupada por el propietario, segunda residencia o propiedad de inversión.").grid(row=16, column=1, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Original combined loan to value").grid(row=17, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="En el caso de un compra de préstamo hipotecario, la proporción se obtiene dividiendo el monto original del préstamo hipotecario en la fecha de la nota más cualquier monto secundario de préstamo hipotecario revelado por el Vendedor por el menor valor de la hipoteca   de la propiedad en la fecha de la nota o su precio de compra").grid(row=17, column=1, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Original debit to income ratio").grid(row=18, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="La relación deuda / ingresos se basa en (1) la suma de la deuda mensual del prestatario pagos, incluidos los gastos mensuales de vivienda que incorporan el pago de la hipoteca que el prestatario está haciendo al momento de la entrega del préstamo hipotecario a Freddie Mac, dividido por (2) el total mensual ingresos utilizados para suscribir el préstamo a partir de la fecha de origen del préstamo").grid(row=18, column=1, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Original interest rate").grid(row=19, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="La tasa de nota original indicada en la nota de hipoteca").grid(row=19, column=1, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Original loan term").grid(row=20, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="Un cálculo de la cantidad de pagos mensuales programados de la hipoteca en función de la primera fecha de pago y fecha de vencimiento.").grid(row=20, column=1, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Original loan to value").grid(row=21, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="La tasa de nota original indicada en la nota de hipotecaEn el caso de un préstamo hipotecario de compra, la proporción obtenida dividiendo la hipoteca original monto del préstamo en la fecha de la nota por el menor valor tasado de la propiedad hipotecada en la fecha de la nota o su precio de compra").grid(row=21, column=1, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Original UPB").grid(row=22, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="El UPB de la hipoteca a la fecha del pagaré.").grid(row=22, column=1, sticky="w", padx=5, pady=5)
  
    
    Label(frameHead, wraplength=100,text="P", font=("",10,"bold")).grid(row=23, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Postal code").grid(row=24, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="El código postal de la ubicación de la propiedad hipotecada.").grid(row=24, column=1, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=300,text="Property state").grid(row=25, column=0, sticky="w", padx=5, pady=5)
    Label(frameHead, wraplength=500,text="Una abreviatura de dos letras que indica el estado o territorio en el que se encuentra la propiedad que garantiza la hipoteca.").grid(row=25, column=1, sticky="w", padx=5, pady=5)
    
    raizVetana.update()
    can.config(scrollregion=can.bbox("all"))