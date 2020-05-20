# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:28:57 2020

@author: NICOLAS
"""

import pandas as pd

import matplotlib.pylab as plt
import csv
import numpy as np
from sklearn.externals import joblib
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('fast')
import seaborn as sns
import scipy as sp
import scipy.stats as st
import seaborn as sns
import numpy as np, matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import scipy.stats

STEPS=8
EPOCHS=80

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h
def createValue(x_test,newVal):
    size=x_test.shape[2]-1
    for i in range(size):
        x_test[0][0][i] = x_test[0][0][i+1]
    x_test[0][0][x_test.shape[2]-1]=newVal
    return x_test
def series(data, initial=1, out=1, dropnan=True):
    cantVar=0
    cols=list()
    names=list()
    if type(data) is list :
        cantVar=1 
    else: 
        cantVar=data.shape[1]
    df=pd.DataFrame(data)
    for i in range(initial, 0, -1):
        cols.append(df.shift(i))
        for j in range(cantVar):
           names.append('var%d(t-%d)' % (j+1, i))
    for i in range(0, out):
        cols.append(df.shift(-i))
        if i==0:
            for j in range(cantVar):
               names.append('var%d(t)' % (j+1))
        else:
            for j in range(cantVar):
                names.append('var%d(t+%d)' % (j+1, i))
    serie=pd.concat(cols, axis=1)
    serie.columns = names
    if dropnan:
        serie.dropna(inplace=True)
    return serie

def predict(archivo):
    scaler=MinMaxScaler(feature_range=(-1, 1))
    lastMonts=pd.read_csv(archivo)
    values=lastMonts.values
    values=values.astype('float32')
    values=values.reshape(-1, 1)
    scaled=scaler.fit_transform(values)
    reframed=series(scaled, STEPS, 1)
    reframed.drop(reframed.columns[[7]], axis=1, inplace=True)
    reframed.head(7)
    values=reframed.values
    x_test=values[6:, :]
    x_test=x_test.reshape((x_test.shape[0], 1, x_test.shape[1]))
    modelo_TR = joblib.load('modelo_TrackIt.pkl')
    results=[]
    for i in range(7):
        predictMonths=modelo_TR.predict(x_test)
        results.append(predictMonths[0])
        x_test=createValue(x_test,predictMonths[0])
    adimen = [x for x in results]    
    inverted = scaler.inverse_transform(adimen)
    predictionLastMonths = pd.DataFrame(inverted)
    predictionLastMonths.columns = ['Prediction']
    x=st.t.interval(0.95, len(inverted)-1, loc=np.mean(inverted), scale=st.sem(inverted))
    predictionLastMonths.plot()
    predictionLastMonths.to_csv('Prediction.csv')
    return inverted
predict('historial.csv')


       