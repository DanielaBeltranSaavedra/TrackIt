from DTO import Origination
from DTO import Origination
from DTO import Historical
import csv
from clasificacion2 import grupoPertence
from readFiles import readFile
import pandas as pd
from joblib import Parallel, delayed
import os,xlrd,xlwt
#Getting data to process 
def enteredPerson(lsqn,data):
    person=list(filter(lambda x:x.lsqn==lsqn,data))
    return person
#using filter
def myGroup(personGroup,resultList):
   listMyGroup=list(filter(lambda x: x.grupo==personGroup ,resultList))
   return listMyGroup#List o nearest person
   #Method to find coincidences using a person, and his historical data, find coincidences in the historical file
def divDb(data,historicalMyModel): 
    lsqnHistorical=list(historicalMyModel['loan_sequence_number'])
    finaldata=(list(filter(lambda x:(x.lsqn)in lsqnHistorical,data)))
    return finaldata
def coincidences(person,element,personHistorical,historicalFile,historicalMyModelCloser):
       total=0
       cs=0
       mip=0
       oltv=0
       ocltv=0
       odtir=0
       olt=0
       if person.lsqn!=element.lsqn: 
            #Definition if the range to find the nearest person
           diferencs=abs(person.cs-element.cs)
           #Defining range for cs
           if(element.cs< person.cs**2):
              cs=(10*abs(person.cs-diferencs))/person.cs
           diferenmip=abs(person.mip-element.mip)
            #Defining range for mip
           if(element.mip< person.mip*2):
                 mip=(10*abs(person.mip-diferenmip))/person.mip
           diferenoltv=abs(person.oltv-element.oltv)
            #Defining range for oltv
           if(element.oltv< person.oltv*2):
                 oltv=(4*abs(person.oltv-diferenoltv))/person.oltv
           diferenocltv=abs(person.ocltv-element.ocltv)
            #Defining range for ocltv
           if(element.ocltv< person.ocltv*2):
                 ocltv=(5*abs(person.ocltv-diferenocltv))/person.ocltv
           diferenodtir=abs(person.odtir-element.odtir)
            #Defining range for odtir
           if(element.odtir< person.odtir*2):
                 odtir=(5*abs(person.odtir-diferenodtir))/person.odtir
           diferenolt=abs(person.olt-element.olt)
            #Defining range for olt
           if(element.olt< person.olt*2):
                 olt=(5*abs(person.olt-diferenolt))/person.olt
          #defining variables
           ps=0
           msa=0
           pc=0
           caupb=0
           cir=0
           cdupb=0
           alc=0 
           cld=0
           rmtlm=0
           colHisto=0
           rmtlmE=0
           dfrmtlm=0
           #looking differences in the historical file
           elementHistorical=historicalMyModelCloser[historicalMyModelCloser['loan_sequence_number']==element.lsqn]
           #apply range on the diferences between historical file and the person
           if len(elementHistorical)>0:
               elementHistorical['current_loan_delinquency_status']
               if(person.ps==element.ps):
                    ps=10
               else:
                    ps=2
               diferenmsa=abs(person.msa-element.msa)
               if(element.msa< (person.msa*2) and element.msa<500000 and diferenmsa<50 ):
                           msa=5
                           diferenpc=abs(person.pc-element.pc)
                           pc=(10*abs(person.pc-diferenpc))/person.pc

                           if pc >=0:     
                                #calculating the differences to find the nearest person
                              if element.msa<500000 and element.msa< (person.msa*2):
                                  msa=(5*abs(person.msa-diferenmsa))/person.msa
                              if personHistorical['remaining_months_to_legal_maturity']!=0:
                               rmtlm=float(min(list( map(lambda x: (10*abs(float(personHistorical['remaining_months_to_legal_maturity'])-abs(personHistorical['remaining_months_to_legal_maturity']-float(x))))/float(personHistorical['remaining_months_to_legal_maturity']) if ((10*abs(float(personHistorical['remaining_months_to_legal_maturity'])-abs(personHistorical['remaining_months_to_legal_maturity']-float(x))))/float(personHistorical['remaining_months_to_legal_maturity']))>=6 else 800 ,elementHistorical['remaining_months_to_legal_maturity']))))
                               if rmtlm==800:
                                   rmtlm=0
                               else:
                                 rmtlm=10
                               if personHistorical['current_actual_upb']!=0:
                                  caupb=float(min(list( map(lambda x: (5*abs(float(personHistorical['current_actual_upb'])-abs(personHistorical['current_actual_upb']-float(x))))/float(personHistorical['current_actual_upb']) if ((5*abs(float(personHistorical['current_actual_upb'])-abs(personHistorical['current_actual_upb']-float(x))))/float(personHistorical['current_actual_upb']))>=3 else 800,elementHistorical['current_actual_upb']))))
                                  if caupb==800:
                                    caupb=0
                               else:
                                 caupb=5
                                 if caupb>=1.5:
                                    if personHistorical['current_interest_rate']!=0:
                                        cir=float(min(list( map(lambda x: (5*abs(float(personHistorical['current_interest_rate'])-abs(personHistorical['current_interest_rate']-float(x))))/float(personHistorical['current_interest_rate']) if ((5*abs(float(personHistorical['current_interest_rate'])-abs(personHistorical['current_interest_rate']-float(x))))/float(personHistorical['current_interest_rate']))>=2 else 800 ,elementHistorical['current_interest_rate']))))
                                        if cir==800:
                                          cir=0
                                    else:
                                        cir=5

                                    if personHistorical['current_deferred_upb']!=0:
                                        cdupb=float(min(list( map(lambda x:(6*abs(float(personHistorical['current_deferred_upb'])-abs(personHistorical['current_deferred_upb']-float(x))))/float(personHistorical['current_deferred_upb']) if ((6*abs(float(personHistorical['current_deferred_upb'])-abs(personHistorical['current_deferred_upb']-float(x))))/float(personHistorical['current_deferred_upb']))>=4 else 800,elementHistorical['current_deferred_upb']))))
                                        if cdupb==800:
                                          cdupb=0
                                    else:
                                        cdupb=6
                                
                                    if personHistorical['actual_loss_calculation']!=0:

                                        alc=float(min(list( map(lambda x:(5*abs(float(personHistorical['actual_loss_calculation'])-abs(personHistorical['actual_loss_calculation']-float(x))))/float(personHistorical['actual_loss_calculation']) if ((5*abs(float(personHistorical['actual_loss_calculation'])-abs(personHistorical['actual_loss_calculation']-float(x))))/float(personHistorical['actual_loss_calculation']))>=3 else 800,elementHistorical['actual_loss_calculation']))))
                                        if alc==800:
                                          alc=0
                                    else:
                                        alc=5
                                    if personHistorical['current_loan_delinquency_status']!=0:

                                        if len(elementHistorical['current_loan_delinquency_status'])<0:
                                          cld=float(min(list( map(lambda x:(5*abs(float(personHistorical['current_loan_delinquency_status'])-abs(personHistorical['current_loan_delinquency_status']-float(x))))/float(personHistorical['current_loan_delinquency_status']) if ((5*abs(float(personHistorical['current_loan_delinquency_status'])-abs(personHistorical['current_loan_delinquency_status']-float(x))))/float(personHistorical['current_loan_delinquency_status']))>=2 else 800,elementHistorical['current_loan_delinquency_status']))))
                                          if cld==800:
                                             cld=0
                                    else: 
                                        cld=5


                             
                                                    
               else:
                                                  #calculating the differences to find the nearest person
                          if element.msa<500000 and element.msa< (person.msa*2):
                             msa=(5*abs(person.msa-diferenmsa))/person.msa
                          if personHistorical['remaining_months_to_legal_maturity']!=0:
                               rmtlm=float(min(list( map(lambda x: (10*abs(float(personHistorical['remaining_months_to_legal_maturity'])-abs(personHistorical['remaining_months_to_legal_maturity']-float(x))))/float(personHistorical['remaining_months_to_legal_maturity']) if ((10*abs(float(personHistorical['remaining_months_to_legal_maturity'])-abs(personHistorical['remaining_months_to_legal_maturity']-float(x))))/float(personHistorical['remaining_months_to_legal_maturity']))>=6 else 800 ,elementHistorical['remaining_months_to_legal_maturity']))))
                               if rmtlm==800:
                                rmtlm=0
                          else:
                             rmtlm=10
                          if personHistorical['current_actual_upb']!=0:
                              caupb=float(min(list( map(lambda x: (5*abs(float(personHistorical['current_actual_upb'])-abs(personHistorical['current_actual_upb']-float(x))))/float(personHistorical['current_actual_upb']) if ((5*abs(float(personHistorical['current_actual_upb'])-abs(personHistorical['current_actual_upb']-float(x))))/float(personHistorical['current_actual_upb']))>=3 else 800,elementHistorical['current_actual_upb']))))
                              if caupb==800:
                                caupb=0
                          else:
                            caupb=5
    
                          if caupb>=1.5:
                                if personHistorical['current_interest_rate']!=0:
                                    cir=float(min(list( map(lambda x: (5*abs(float(personHistorical['current_interest_rate'])-abs(personHistorical['current_interest_rate']-float(x))))/float(personHistorical['current_interest_rate']) if ((5*abs(float(personHistorical['current_interest_rate'])-abs(personHistorical['current_interest_rate']-float(x))))/float(personHistorical['current_interest_rate']))>=2 else 800 ,elementHistorical['current_interest_rate']))))
                                    if cir==800:
                                      cir=0
                                else:
                                    cir=5

                                if personHistorical['current_deferred_upb']!=0:
                                    cdupb=float(min(list( map(lambda x:(6*abs(float(personHistorical['current_deferred_upb'])-abs(personHistorical['current_deferred_upb']-float(x))))/float(personHistorical['current_deferred_upb']) if ((6*abs(float(personHistorical['current_deferred_upb'])-abs(personHistorical['current_deferred_upb']-float(x))))/float(personHistorical['current_deferred_upb']))>=4 else 800,elementHistorical['current_deferred_upb']))))
                                    if cdupb==800:
                                      cdupb=0
                                else:
                                    cdupb=6
                                
                                if personHistorical['actual_loss_calculation']!=0:
                                    
                                    alc=float(min(list( map(lambda x:(5*abs(float(personHistorical['actual_loss_calculation'])-abs(personHistorical['actual_loss_calculation']-float(x))))/float(personHistorical['actual_loss_calculation']) if ((5*abs(float(personHistorical['actual_loss_calculation'])-abs(personHistorical['actual_loss_calculation']-float(x))))/float(personHistorical['actual_loss_calculation']))>=3 else 800,elementHistorical['actual_loss_calculation']))))
                                    if alc==800:
                                      alc=0
                                else:
                                    alc=5
                                if personHistorical['current_loan_delinquency_status']!=0:

                                    if len(elementHistorical['current_loan_delinquency_status'])<0:
                                      cld=float(min(list( map(lambda x:(5*abs(float(personHistorical['current_loan_delinquency_status'])-abs(personHistorical['current_loan_delinquency_status']-float(x))))/float(personHistorical['current_loan_delinquency_status']) if ((5*abs(float(personHistorical['current_loan_delinquency_status'])-abs(personHistorical['current_loan_delinquency_status']-float(x))))/float(personHistorical['current_loan_delinquency_status']))>=2 else 800,elementHistorical['current_loan_delinquency_status']))))
                                      if cld==800:
                                         cld=0
                                else: 
                                    cld=5
               total=cs+msa+mip+oltv+ocltv+odtir+ps+pc+olt+caupb+cir+cdupb+alc+cld+rmtlm
           else: 
              total=0 
       else: 
         total=0
       return total#total percentage of the person
       #chosing the best person to compare
def similar(person,listaGrupo,personHistorical,historicalFile,historicalMyModelCloser):
       closer=[]
      
       grupoPc=(list(filter(lambda x: ((10*abs(person.pc-(abs(person.pc-x.pc))))/person.pc)>=9.5,listaGrupo)))
      
       closer=(list(filter(lambda x:coincidences(person,x,personHistorical,historicalFile,historicalMyModelCloser)>=55,grupoPc )))
      
       return closer
#looking for coincidences in the ID value LSQN
def historicalPersonLastLast(lsqn,historicalFile,r):
      i=0
      personHistorical=historicalFile[historicalFile['loan_sequence_number']==lsqn]
      modificationMonth=personHistorical[personHistorical['modification_flag']=='Y']
      
    
      informationLastMonth=[]
      if len(modificationMonth)>0:
        
          lastMonth=modificationMonth['monthly_reporting_period']
          
          h=personHistorical['monthly_reporting_period']
          tow=personHistorical['current_actual_upb']
          
          rowLastMonth=(modificationMonth.index.values[0])-1
          
        
    
          informationLastMonth=r.iloc[rowLastMonth]
          ff=informationLastMonth['current_actual_upb']
         
        
      return informationLastMonth
def listHistoricalPersonToTrain(lsqn,historicalFile,r):
      i=0
      personHistorical=historicalFile[historicalFile['loan_sequence_number']==lsqn]
      inform=[]
      modificationMonth=personHistorical[personHistorical['modification_flag']=='Y']
      
      informationLastMonth=[]
      if len(modificationMonth)>0:
          lastMonth=modificationMonth['monthly_reporting_period']
         
          h=personHistorical['monthly_reporting_period']
          tow=personHistorical['current_actual_upb']
         
          rowLastMonth=(modificationMonth.index.values[0])
          infoToWrite=tow.iloc[:rowLastMonth]
          inicio=personHistorical.iloc[1]['current_actual_upb']
          ffrow=personHistorical[personHistorical['current_actual_upb']== inicio]
          
        
          rowFirst=ffrow.index.values[0]
          
          infofo=list(r['current_actual_upb'].iloc[(rowFirst+13):(rowLastMonth+7)])
          #inform.append((r['current_actual_upb'].iloc[(rowFirst+12))-(infofo[0]))
          for i in range(len(infofo)-2):
              inform.append(infofo[i]-infofo[i+1])

              
        
          
      return inform
def listHistoricalPersonToTesting(lsqn,historicalFile,r):
      i=0
      personHistorical=historicalFile[historicalFile['loan_sequence_number']==lsqn]
      inform=[]
      modificationMonth=personHistorical[personHistorical['modification_flag']=='Y']
     
      informationLastMonth=[]
      if len(modificationMonth)>0:
          lastMonth=modificationMonth['monthly_reporting_period']
          
          h=personHistorical['monthly_reporting_period']
          tow=personHistorical['current_actual_upb']
         
          rowLastMonth=(modificationMonth.index.values[0])
          infoToWrite=tow.iloc[:rowLastMonth]
          inicio=personHistorical.iloc[len(personHistorical)-1]['current_actual_upb']
          ffrow=personHistorical[personHistorical['current_actual_upb']== inicio]
          
        
          rowFirst=ffrow.index.values[0]
         
          infofo=list(r['current_actual_upb'].iloc[rowLastMonth:rowFirst])
          #inform.append(r['current_actual_upb'].iloc[(rowFirst+12)-infofo[0])
          for i in range(len(infofo)-1):
              inform.append(infofo[i]-infofo[i+1])
         
      return inform
  
def historicalElement(lsqn,historicalMyModelCloser):
      
      personHistorical=historicalMyModelCloser[historicalMyModelCloser['loan_sequence_number']==lsqn]
     
      return personHistorical
      #Adding the ID of the nearest persons in a historial array
    
def fileCercanos(cercanos,historicalFile,lsqnPerson,historicalMyModelCloser,r):
    outExcel= (r'outFileClose.csv')
    if os.path.isfile(outExcel):os.remove(outExcel)
    workbook = xlwt.Workbook()
    sheetOut = workbook.add_sheet('DATA')
    i=0
    personH=historicalPersonLastLast(lsqnPerson,historicalFile,r)
    if len(personH)>0:
      
        upbPerson=personH['current_actual_upb']
        
        upbFirstPerson=upbPerson
        upbPorcentActualToPay=((upbFirstPerson*100)/upbPerson)
        if len(cercanos)>100:
            cercanos=cercanos[:100]
        
        for c in cercanos:
            cer=c
            inf=[]

            historialComplete=historicalElement(c.lsqn,historicalMyModelCloser)

            informacionHistorial=historialComplete['current_actual_upb']
            firstInfoH=informacionHistorial.iloc[0]
          
            
            
            historialAescribir=informacionHistorial[(10*(abs(upbFirstPerson-(abs(upbFirstPerson-historialComplete['current_actual_upb']))))/upbFirstPerson)>=9.5]
            if len(historialAescribir)>0:
                if historialAescribir.iloc[0]>upbFirstPerson:
                    if (abs(historialAescribir.iloc[0]-upbFirstPerson))<200000:
                        #el index de informacionHistorial donde sale el primero del historial a escribir 
                           
                            rowinfo=(historialAescribir.index.values[0])
                        
                                   
                            row=rowinfo
                            informacionHistorical=list(informacionHistorial.iloc[:(rowinfo-5)])
                            if len(informacionHistorical)> 1:                       
                            
                             
                                   
                                j=0
                                if len(informacionHistorical)>100:
                                    for h in range(len(informacionHistorical)/2):
                                        if i<200:
                                           
                                            sheetOut.write(j, i, informacionHistorical[h])
                                            j+=1
                                    i+=1 
                                else:
                                    j=0
                                    for h in range(len(informacionHistorical)-1):
                                        if i<200:
                                            
                                            sheetOut.write(j, i, informacionHistorical[h])
                                            j+=1
                                    i+=1 
                else:
                        
                        rowinfo=(historialAescribir.index.values[0])
                    
                               
                        row=rowinfo
                        informacionHistorical=list(informacionHistorial.iloc[:(rowinfo-5)])
                        
                        if len(informacionHistorical)>1:
                     
                               
                            j=0
                            if len(informacionHistorical)>100:
                                    for h in range(len(informacionHistorical)/2):
                                           
                                            if i<200:
                                                sheetOut.write(j, i, informacionHistorical[h])
                                                j+=1
                                        
                                    i+=1
                                        
                                            
                                           
                                         
                            else:
                                 j=0
                                 if len(informacionHistorical)>100:
                                     for h in range(len(informacionHistorical)-1):
                                              
                                                if i<200:

                                                    sheetOut.write(j, i, informacionHistorical[h])
                                                    j+=1
                                     i+=1 

                                           
                                
                

    workbook.save(outExcel)#save the result
    return i

def listClosersFinal(cols):
   
    total=0
    promedio=0
    cell_val_row=0
    promedios=[]
    h=0
    ruta_archivo = "outFileClose.csv"
    openfile = xlrd.open_workbook(ruta_archivo)
    sheet = openfile.sheet_by_name("DATA")
    for i in range(0, sheet.nrows):
      
        cell_val_row = sheet.cell_value(i,0)
        if cell_val_row != '':
           
             for j in range(cols):
             
                info=sheet.cell_value(i,j)
                
                if  info!='':
                    info=float(sheet.cell_value(i,j))
                    promedio += info
                   
        total = promedio / cols
        promedios.append(total)
        total=0
        promedio=0
   
        
    return promedios
def writeFileHistoricalPersons(listPersonsHistorical):
    outExcel= (r'historicalPersonsToTrain.xls')
    if os.path.isfile(outExcel):os.remove(outExcel)
    workbook = xlwt.Workbook()
    sheetOut = workbook.add_sheet('DATA')
    i=0
    
    for h in listPersonsHistorical:
        j=0
        for k in h:
            sheetOut.write(j, i, k)
            j+=1
        i+=1       
    workbook.save(outExcel)#save the result
   
  
def writeFileHistoricalPersonsTesting(listPersonsHistorical):
    outExcel= (r'historicalPersonsToTesting.xls')
    if os.path.isfile(outExcel):os.remove(outExcel)
    workbook = xlwt.Workbook()
    sheetOut = workbook.add_sheet('DATA')
    i=0
    
    for h in listPersonsHistorical:
        j=0
        for k in h:
            sheetOut.write(j, i, k)
            j+=1
        i+=1       
    workbook.save(outExcel)#save the result
def writeFileCloserToTrain(listPersonsHistorical):
    outExcel= (r'historicalClosersToTrain.xls')
    if os.path.isfile(outExcel):os.remove(outExcel)
    workbook = xlwt.Workbook()
    sheetOut = workbook.add_sheet('DATA')
    i=0
    
    for h in listPersonsHistorical:
        j=0
        for k in h:
            if k!=0:
                sheetOut.write(j, i, k)
            j+=1
        i+=1       
    workbook.save(outExcel)#save the result