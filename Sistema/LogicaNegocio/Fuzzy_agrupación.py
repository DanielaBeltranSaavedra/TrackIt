

#Pre-procesamiento de datos
import numpy as np
import pandas as pd
import skfuzzy as fuzz
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import skfuzzy as fuzz
import numpy
import csv

"""
Description: Method for calculating missing data
inputs: x - data set
outputs:
""" 
def calcular_datos_flatantes(x):
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer = imputer.fit(x.values[:, 1:3])
    x.iloc[:, 1:3] = imputer.transform(x.values[:, 1:3])

"""
Description: Método para asignar valores numéricos a variables categóricas.
inputs: datAgru - data set
outputs: data set with categorical variables with assigned numerical values.
""" 
def codificar(datAgru):
    label_encoder_x = LabelEncoder()
    datAgru.iloc[:, 2] = label_encoder_x.fit_transform(datAgru.values[:, 2])
    datAgru.iloc[:, 7] = label_encoder_x.fit_transform(datAgru.values[:, 7])
    datAgru.iloc[:, 28] = label_encoder_x.fit_transform(datAgru.values[:, 28])
    
    return datAgru

"""
Description: Method to encode values between -1 and 1
inputs: fthf - fthf column of the dataset
        os - os column of the dataset
        rep_flag - rep_flag column of the dataset
        cs - cs column of the dataset
        mip - mip column of the dataset
        odtir - odtir column of the dataset
        oltv - oltv column of the dataset
        cur_flag - cur_flag column of the dataset
outputs:
""" 
def codificacion_completa(fthf,os,rep_flag,cs,mip,odtir,oltv,cur_flag):
    # Codificacion de variables categoricas
    label_encoder_x = LabelEncoder()
    fthf = label_encoder_x.fit_transform(fthf)
    os = label_encoder_x.fit_transform(os)
    rep_flag = label_encoder_x.fit_transform(rep_flag)
    
    # Transformación de escalas
    sc_x = StandardScaler()
    cs = sc_x.fit_transform(cs.values.reshape(-1, 1))
    fthf = sc_x.fit_transform(fthf.reshape(-1, 1))
    mip = sc_x.fit_transform(mip.values.reshape(-1, 1))
    os = sc_x.fit_transform(os.reshape(-1, 1))
    odtir = sc_x.fit_transform(odtir.values.reshape(-1, 1))
    oltv = sc_x.fit_transform(oltv.values.reshape(-1, 1))
    rep_flag = sc_x.fit_transform(rep_flag.reshape(-1, 1))
    cur_flag = sc_x.fit_transform(cur_flag.values.reshape(-1, 1))
    
    datAgru.iloc[:,0] = cs
    datAgru.iloc[:,2] = fthf
    datAgru.iloc[:,5] = mip
    datAgru.iloc[:,7] = os
    datAgru.iloc[:,9] = odtir
    datAgru.iloc[:,11] = oltv
    datAgru.iloc[:,28] = rep_flag
    datAgru.iloc[:,29] = cur_flag
"""
Description: Method to group the values ​​in different 'n' clusters groups and save the 
            information in a .csv file
inputs: datAgru - data set
        clusters - number of clusters
outputs: distance of each value in the dataset
""" 
def agrupar_Guardar(datAgru,clusters):
    
    alldata = np.vstack((datAgru.values[:,0],datAgru.values[:,2],datAgru.values[:,5],datAgru.values[:,7],datAgru.values[:,9],datAgru.values[:,11],datAgru.values[:,28],datAgru.values[:,29]))
        
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(alldata, clusters, 2, error=0.005, maxiter=1000, init=None)
    
    #Función de invertir
    colum = np.size(u,1)
    filas = np.size(u,0)
    matAux = np.empty([colum,filas])
    
    #Imprimir distancias
    for i in range(filas):
        for j in range(colum):
            matAux[j,i] = u[i,j]
    
    numpy.savetxt("Pertenencia.csv",matAux,delimiter=",")
    
    return d
"""
Description: Method to save in a .csv file the information of the distances of each one 
             of the values of the data set
inputs: d - distance of each value in the dataset
outputs:
"""   
def mas_cercanos(d):
    colum = np.size(d,1)
    filas = np.size(d,0)
    numFila = []
    
    for i in range(filas):
        mini = 100
        for j in range(colum):
            if d[i,j] < mini:
                lisInt = []
                lisInt.insert(1,j)
                mini = d[i,j]
            if d[i,j] == mini:
                lisInt.insert(len(lisInt),j)
        numFila.insert(i,lisInt)
    
    prototi = [["CS","FPD","FTHF","MD","MSA","MIP","NOU","OS","OCLTV","ODTIR","OUPB","OLTV","OIR","CHANNEL","PPMFMF","PT","PS","PT2","PC","LSQN","LP","OLT","NOB","SN","SEN","SCF","PHLSN","LSQN2","REPURCHASE_FLAG","CURRENT_LOAN_DELINQUENCY_STATUS_REPURCHASE_FLAG","LATER_PAYMENT_FLAG","CURRENT_LOAN_DELINQUNCY_STATUS_LATER_PAYMENT","TIMES_REPURCHASE_FLAG","TIMES_LATER_PAYMENT","Grupo"]]
    for i in range(len(numFila)):
        for j in range(len(numFila[i])):
            lisInt = numFila[i]
            aux = datAgru.values[lisInt[j],:].tolist()
            aux.insert(len(aux),i+1)
            prototi.insert(i+1,aux)
            
    with open("Prototipos_escalados.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(prototi)

#Cargamos el conjunto de datos
dataset = pd.read_csv('CSV.csv')

"""
cs = dataset.iloc[:, 0]
fthf = dataset.iloc[:, 2]
mip = dataset.iloc[:, 5]
os = dataset.iloc[:, 7]
odtir = dataset.iloc[:, 9]
oltv = dataset.iloc[:, 11]
rep_flag = dataset.iloc[:, 28]
cur_flag = dataset.iloc[:, 29]
"""

datAgru = dataset.iloc[:,0:35]

datAgru = codificar(datAgru)

distancias = agrupar_Guardar(datAgru,6)

mas_cercanos(distancias)


