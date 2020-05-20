
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import numpy
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
 
#CSV load for analysis
datos_cargados = pd.read_csv(r"ORIGINAL_DATA_POR_COMAS.csv")
#View of the number of rows and columns selected in the arrays
#Selection of relevant data, and label
datos_reelevantes = np.array(datos_cargados[["CS","MIP","OCLTV","OUPB","OIR","NOB"]])
etiqueta = np.array(datos_cargados['OLTV'])
datos_reelevantes.shape #rows,columns
#Finding the value of K
Nc = range(1, 20) #Generating range from 1 to 20
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(datos_reelevantes).score (datos_reelevantes) for i in range(len(kmeans))]
score 
#plt.plot(Nc,score )#The values ​​to graph,in notebook
#Assigning the labels to the graph
plt.xlabel('Numero de Clusters')
plt.ylabel('Valor')
plt.title('Curva')
#plt.show() #Graph,in notebook
#Implemented Kmeans, and feeding it with array X of the data, and entering the number of clusters	
kmeans = KMeans(n_clusters=6).fit(datos_reelevantes)
#Generating centroids
centroids = kmeans.cluster_centers_
#Show centroids
print(centroids)
#Generating the clients and their respective clusters
labels = kmeans.predict(datos_reelevantes)
colores=['red','green','blue','cyan','yellow','pink','black']
copia =  pd.DataFrame()
copia['LSQN']=datos_cargados['LSQN'].values
copia['OCLTV']=datos_cargados['OCLTV'].values
copia['Grupo'] = labels;
cantidadGrupo =  pd.DataFrame() #Saving clients and their group
cantidadGrupo['color']=colores
cantidadGrupo['cantidad']=copia.groupby('Grupo').size()
#cantidadGrupo #Generate table,in notebook
#We look at the clients of the group 0,1,2,3,4,5,6.....
for index, fila in copia.iterrows():
    if fila["Grupo"] == 0:
            print(fila["LSQN"],fila["Grupo"])
    if fila["Grupo"] == 1:
            print(fila["LSQN"],fila["Grupo"])
    if fila["Grupo"] == 2:
            print(fila["LSQN"],fila["Grupo"])
    if fila["Grupo"] == 3:
            print(fila["LSQN"],fila["Grupo"])
    if fila["Grupo"] == 4:
            print(fila["LSQN"],fila["Grupo"])
    if fila["Grupo"] == 5:
            print(fila["LSQN"],fila["Grupo"])
    if fila["Grupo"] == 6:
            print(fila["LSQN"],fila["Grupo"])
#Generating table with # of clients and their respective group
labels = kmeans.predict(datos_reelevantes)
colores=['red','green','blue','cyan','yellow','pink','black']
copia =  pd.DataFrame()
copia['LSQN']=datos_cargados['LSQN'].values
copia['OCLTV']=datos_cargados['OCLTV'].values
copia['label'] = labels;
cantidadGrupo =  pd.DataFrame()
cantidadGrupo['color']=colores
cantidadGrupo['cantidad']=copia.groupby('label').size()
#cantidadGrupo #Generate table,in notebook     
#We see the representative of the group, the user close to his centroid
cercanos, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, datos_reelevantes)
cercanos
#We look for the id of the closest clients
usuarios=datos_cargados['LSQN'].values
for fila in cercanos:
    print(usuarios[fila])
#Now we associate the centroid with its id passing as a parameter the list of centroids
labels = kmeans.predict(datos_reelevantes)
colores=['red','green','blue','cyan','yellow','pink','black']
copia =  pd.DataFrame()
copia['LSQN']=datos_cargados['LSQN'].values
copia['OCLTV']=datos_cargados['OCLTV'].values
copia['Grupo'] = labels;
cantidadGrupo =  pd.DataFrame()
cantidadGrupo['color']=colores
cantidadGrupo['cantidad']=copia.groupby('Grupo').size()
cantidadGrupo
#We look at the centroids, or representative users of each cluster
for index, fila in copia.iterrows():
    if fila["LSQN"] == 'F109Q2678262':
            print(fila["LSQN"],fila["Grupo"])
    if fila["LSQN"] == 'F110Q4414878':
            print(fila["LSQN"],fila["Grupo"])
    if fila["LSQN"] == 'F112Q3428892':
            print(fila["LSQN"],fila["Grupo"])
    if fila["LSQN"] == 'F113Q3529837':
            print(fila["LSQN"],fila["Grupo"])
    if fila["LSQN"] == 'F111Q3280960':
            print(fila["LSQN"],fila["Grupo"])
    if fila["LSQN"] == 'F112Q2357370':
            print(fila["LSQN"],fila["Grupo"])