# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('fast')

from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

STEPS=8
EPOCHS=80
def createModel():
    model=Sequential() 
    model.add(Dense(STEPS, input_shape=(1,STEPS),activation='tanh'))
    model.add(Flatten())
    model.add(Dense(1, activation='tanh'))
    model.compile(loss='mean_absolute_error',optimizer='Adam',metrics=["mse"])
    model.summary()
    return model
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

def redValues():
    file=pd.read_excel('..\\Repositorio de datos\\historicalClosersToTrain.xlsx',header=None)
    for i in range (50):
        df=file.iloc[:,i]
        values=df.values
        values = values.astype('float32')
        print(values)
    return values
def changeScaler(values):
        scaler = MinMaxScaler(feature_range=(-1, 1))
        values=values.reshape(-1, 1)
        scaled = scaler.fit_transform(values)
        return scaled
def reframed(scaled):
        reframed = series(scaled, STEPS, 1)
        reframed.head()
        return reframed
def splitTest(reframed):
    values = reframed.values
    return values
def trainig(values,reframed):
        trainingSize = len(values)-15
        trainList=values[:trainingSize, :]
        test=values[trainingSize:, :]
        x_train= trainList[:, :-1]
        y_train=trainList[:, -1]
        x_val=test[:, :-1]
        y_val=test[:, -1]
        x_train=x_train.reshape((x_train.shape[0], 1, x_train.shape[1]))
        x_val=x_val.reshape((x_val.shape[0], 1, x_val.shape[1]))
        model = createModel()
        MonthTrain=model.fit(x_train,y_train,epochs=EPOCHS,validation_data=(x_val,y_val),batch_size=STEPS)
        results=model.predict(x_val)
        joblib.dump(model,'modelo_TrackIt.pkl')
        return model
def predict(values,scaler,model):
    scaler=MinMaxScaler(feature_range=(-1, 1))
    modelo_TR=joblib.load('modelo_TrackIt.pkl')
    MonthsPredict = pd.read_excel('..\\Repositorio de datos\\historicalPersonsToTrain.xls')
    for i in range(50):
        values=MonthsPredict.iloc[:,i].values
        values=values.astype('float32')
        values=values.reshape(-1, 1)
        scaled=scaler.fit_transform(values)
        reframed=series(scaled, STEPS, 1)
        reframed.drop(reframed.columns[[7]], axis=1, inplace=True)
        reframed.head(7)
        values=reframed.values
        x_test=values[6:, :]
        x_test=x_test.reshape((x_test.shape[0], 1, x_test.shape[1]))
        results=[]
        for i in range(7):
            predictMonths=modelo_TR.predict(x_test)
            results.append(predictMonths[0])
            x_test=createValue(x_test,predictMonths[0])
        adimen=[x for x in results]    
        inverted=scaler.inverse_transform(adimen)
        Prediction7 = pd.DataFrame(inverted)
        Prediction7.columns = ['Prediction']
        Prediction7.plot()
        Prediction7.to_csv('Prediction.csv')
    
 
    
#values=redValues()
#scaled=changeScaler(values)
#reframed=reframed(scaled)
#splitTest(reframed)
#values=splitTest(reframed)
#model=trainig(values,reframed)
#predict(values,scaled,model)