import pandas as pd

#PRUEBAS DE PREDICCION

#Error Percentage
#Description: This function give to result the percentage of error for the predict value
def errorPercentage(realValue,predictValue):
    difference=abs(realValue-predictValue)
    percentage=(100*difference)/realValue
    return percentage
#Get Reak Value
#Description: This function give the real value of the pay in the month that i want to know
def getRealValue(month,historicalInformation):
    value=historicalInformation[month]
    return value
#Month Value of Prediction
#Description: This function give the month where it applies the predicted value
def monthValueOfPrediction(predictValue,historicalInformation):
   months=list(filter(lambda x: errorPercentage(x,predictValue)<=10,historicalInformation))
   month=0
   if len(months)==0:
       month=0
   menor=100
   
   for i in months:
       error=errorPercentage(i,predictValue)
       if error < menor:
           menor=error
           month=historicalInformation.index(i)+1
           
   print(month)
   return month

#PRUEBAS DE CLASIFICACION 
def cs(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def oir(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def oltv(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def mip(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def ocltv(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def oupb(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def olt(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def grup0(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
    
def grup1(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def grup2(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def grup3(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def grup4(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def grup5(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def grup6(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def grup7(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
def grupBelongs(val,realVar):
    if val==realVar:
        print("BUENO")
    else:
        print("MALO")

#PRUEBAS DE CERCANOS

def coincidence(var,realVar):
    error=errorPercentage(realVar,var)
    if error<=20:
        print("BUENO")
    if 20<error and error<=35:
        print("REGULAR")
    if error>35:
        print("MALO")
        
def similar(resultList,realList):
    count=0
    for i in resultList:
        for j in realList:
            if i.lsqn==j.lsqn:
                count+=1
    error=errorPercentage(len(resultList),resultList)
    if error<=10:
         print("BUENO")
    if 10<error and error<=25:
        print("REGULAR")
    if error>25:
        print("MALO")