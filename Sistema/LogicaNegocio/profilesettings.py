import collections
import csv
from DTO import Origination
from DTO import Perfil
from readFiles import readFile
def insertion(val):
    for i in range(1, len(val)):
        aux = val[i]
        j=i-1
        while (j>=0 and aux<val[j]):
            val[j+1]=val[j]
            j=j-1
        val[j+1]=aux

def bucket_sort(val):
    largest=max(val)
    size=largest/len(val)
    result = []
    buckets = [[] for _ in range(len(val))]
    for i in range(len(val)):
        j=int(val[i]/size)
        
        if j!=len(val):
            buckets[j].append(val[i])
        else:
            buckets[len(val) - 1].append(val[i])
    for i in range(len(val)):
        insertion(buckets[i]) 
    for i in range(len(val)):
        result = result + buckets[i]
 
    return result
 
def minor(sorted_list):
    sorted_list= bucket_sort(sorted_list)
    counter=collections.Counter(sorted_list[:len(sorted_list)//12])
    counterOrder=collections.OrderedDict(counter)
    valor10=((len(sorted_list)*0.3)/100)
    minimum=list(filter(lambda x: counterOrder[x]>=valor10,counterOrder.keys()))[0]
    print("minor", minimum)
    return minimum
def higher(sorted_list):
    sorted_list= bucket_sort(sorted_list)
    counter=collections.Counter(sorted_list[len(sorted_list)//12:])
    counterOrder=collections.OrderedDict(counter)
    valor10=((len(sorted_list)*0.3)/100)
    max=list(filter(lambda x: counterOrder[x]>=valor10,counterOrder.keys()))
    maxResult=max[len(max)-1]
    print("higher", maxResult)
    return maxResult
def percentageGroup(group1,group2):
    percent=0.0
    csRange=list(filter(lambda x: x>=group2.cs[0] and x<=group2.cs[((len(group2)-1))] ,group1))
    csPercentage=getPercentage(csRange,len(group1))
    if csPercentage>=50:
        percent+=((csPercentage*30)/100)
        oirRange=list(filter(lambda x: x>=csRange.oir[0] and x<=csRange.oir[((len(csRange)-1))] ,csRange))
        oirPercentage=getPercentage(oirRange,len(csRange))
        if oirPercentage>=55:
            percent+=((oirPercentage*8)/100)
            oltvRangeOir=list(filter(lambda x: x>=oirRange.oltv[0] and x<=oirRange.oltv[((len(oirRange)-1))] ,oirRange))
            oltvPorcentOir=getPercentage(oltvRangeOir,len(oirRange))
            if oltvPorcentOir>=65:
                percent+=((oltvPorcentOir*10)/100)
                oupbRange=list(filter(lambda x: x>=oltvRangeOir.oupb[0] and x<=oltvRangeOir.oupb[((len(oltvRangeOir)-1))] ,oltvRangeOir))
                oupbPorcent=getPercentage(oupbRange,len(oltvRangeOir))
                if oupbPorcent>=30:
                    percent+=((oupbPorcent*9)/100)
            oltRange=list(filter(lambda x: x>=oltvRangeOir.olt[0] and x<=oltvRangeOir.olt[((len(oltvRangeOir)-1))] ,oltvRangeOir))
            oltPorcent=getPercentage(oltRange,len(oltvRangeOir))
            if oltPorcent>=70:
                percent+=((oltPorcent*10)/100)
                ocltvRange=list(filter(lambda x: x>=oltRange.ocltv[0] and x<=oltRange.ocltv[((len(oltRange)-1))] ,oltRange))
                ocltvPorcent=getPercentage(ocltvRange,len(oltRange))
                if ocltvRange >=60:
                    percent+=((ocltvRange*8)/100)
        mipRange=list(filter(lambda x: x>=csRange.mip[0] and x<=csRange.mip[((len(csRange)-1))] ,csRange))
        mipPercentage=getPercentage(mipRange,len(csRange))
        if mipPercentage>=15:
            percent+=((mipPercentage*25)/100)
    return percent   
def toSearchNewGroup(group,listToSearch):
    listToSearch.append(group)
def searchGroup(group,listGroups):
    percentageG0=percentageGroup(group,listGroups[0])
    percentageG1=percentageGroup(group,listGroups[1])
    percentageG2=percentageGroup(group,listGroups[2])
    percentageG3=percentageGroup(group,listGroups[3])
    percentageG4=percentageGroup(group,listGroups[4])
    percentageG5=percentageGroup(group,listGroups[5])
    percentageG6=percentageGroup(group,listGroups[6])
    percentageG7=percentageGroup(group,listGroups[7])
    listPercen = [percentageG0,percentageG1,percentageG2,percentageG3,percentageG4,percentageG5,percentageG6,percentageG7]
    maximum = max(listPercen)
    groupClass= listPercen.index(maximum)
    listGroups[groupClass].append(group)
    return maximum
        
def getPercentage(listInput,orginalsize):
    suma=len(listInput)
    percentage=((suma*100)/orginalsize)
    return percentage
def rank(listInput,mini,maxi):
    listInput=list(filter(lambda x:x>=mini and x<= maxi,listInput))
    return listInput
def csRange(grupo,csmedio,listToSearch,listToEval):
    csminor=minor(list(map(lambda x:x.cs,grupo)))  
    cshigher=higher(list(map(lambda x:x.cs,grupo)))
    csRange1=list(filter(lambda x: x.cs>=csminor and x.cs<=csmedio ,grupo))
    csRange2=list(filter(lambda x: x.cs>=csmedio and x.cs<=cshigher ,grupo))
    csPorcent1=getPercentage(csRange1,grupo)
    csPorcent2=getPercentage(csRange1,grupo)
    if csPorcent1==50 and csPorcent2==50:
        listToEval.append(csRange2)
        return csRange1
    if csPorcent1==50 and csPorcent2<50:
        csRange1.append(csRange2[:(len(csRange2)//2)])    
        return csRange1
    if csPorcent2==50 and csPorcent1<50:
        csRange2.append(csRange1[(len(csRange1)//2):])
        return csRange2
    if csPorcent1 >=60:
        toSearchNewGroup(csRange2,listToSearch)
        return csRange1
    if csPorcent2 >=60:
        toSearchNewGroup(csRange1,listToSearch)
        return csRange2
   
def oirRange(csRange):
    oirCsListRange=collections.Counter(list(map(lambda x: x.oir,csRange)))
    oirminor=minor(list(map(lambda x: x.oir,csRange)))
    oirhigher=higher(list(map(lambda x: x.oir,csRange)))
    oirRange=list(filter(lambda x: x.oir>=oirminor and x.oir<=oirhigher ,csRange))
    oirPorcent=getPercentage(oirRange,len(oirCsListRange))
    return oirRange
def oltvOir(oirRange):
    oltvOirminor=minor(list(map(lambda x: x.oltv,oirRange)))
    oltvOirhigher=higher(list(map(lambda x: x.oltv,oirRange)))
    oltvOirListRange=collections.Counter(list(map(lambda x: x.oltv,oirRange)))
    oltvRangeOir=list(filter(lambda x: x.oltv>=oltvOirminor and x.oltv<=oltvOirhigher ,oirRange))
    oltvPorcentOir=getPercentage(oltvRangeOir,len(oltvOirListRange))
    return oltvRangeOir   
def oltOir(oirRange):
    oltOirListRange=collections.Counter((list(map(lambda x: x.olt,oirRange))))
    oltOirminor=minor((list(map(lambda x: x.olt,oirRange))))
    oltOirhigher=higher((list(map(lambda x: x.olt,oirRange))))
    oltRangeOir=list(filter(lambda x: x.olt>=oltOirminor and x.olt<=oltOirhigher ,oirRange))
    oltPorcentOir=getPercentage(oltRangeOir,len(oltOirListRange))
    return oltRangeOir
def oupbOir(oirRange):
    oupbOirListRange=collections.Counter((list(map(lambda x: x.oupb,oirRange))))
    oupbOirminor=minor((list(map(lambda x: x.oupb,oirRange))))
    oupbOirhigher=higher((list(map(lambda x: x.oupb,oirRange))))
    oupbRange=list(filter(lambda x: x.oupb>=oupbOirminor and x.oupb<=oupbOirhigher ,oirRange))
    oupbPorcent=getPercentage(oupbRange,len(oupbOirListRange))
    return oupbRange                
def oltOupb(oupbRange):
    oltOupbListRange=collections.Counter((list(map(lambda x: x.olt,oupbRange))))
    oltOupbminor=minor((list(map(lambda x: x.olt,oupbRange))))
    oltOupbhigher=higher((list(map(lambda x: x.olt,oupbRange))))
    oltRangeOupb=list(filter(lambda x: x.olt>=oltOupbminor and x.olt<=oltOupbminor ,oupbRange))
    oltPorcentOupb=getPercentage(oltRangeOupb,len(oltOupbListRange))
    return oltRangeOupb          
def nobOupb(oupbRange):
    nobOupbListRange=collections.Counter((list(map(lambda x: x.nob,oupbRange))))
    nobOupbminor=minor((list(map(lambda x: x.nob,oupbRange))))
    nobOupbhigher=higher((list(map(lambda x: x.nob,oupbRange))))
    nobRange=list(filter(lambda x: x.nob>=nobOupbminor and x.nob<=nobOupbhigher ,oupbRange))
    nobPorcent=getPercentage(nobRange,len(nobOupbListRange))
    return nobRange          
def ocltvOupb(oupbRange):
    ocltvOupbListRange=collections.Counter((list(map(lambda x: x.ocltv,oupbRange))))
    ocltvOupbminor=minor((list(map(lambda x: x.ocltv,oupbRange))))
    ocltvOupbhigher=higher((list(map(lambda x: x.ocltv,oupbRange))))
    ocltvRangeOupb=list(filter(lambda x: x.ocltv>=ocltvOupbminor and x.ocltv<=ocltvOupbhigher ,oupbRange))
    ocltvPorcentOupb=getPercentage(ocltvRangeOupb,len(ocltvOupbListRange))
    return ocltvRangeOupb
def oltvCs(csRange):
    oltvCsListRange=collections.Counter((list(map(lambda x: x.oltv,csRange))))
    oltvCsminor=minor((list(map(lambda x: x.oltv,csRange))))
    oltvCsbhigher=higher((list(map(lambda x: x.oltv,csRange))))
    oltvRange=list(filter(lambda x: x.oltv>=oltvCsminor and x.oltv<=oltvCsbhigher ,csRange))
    oltvPorcent=getPercentage(oltvRange,len(oltvCsListRange))
    return oltvRange  
def ocltvOltv(oltvRange):
    ocltvOltvListRange=collections.Counter((list(map(lambda x: x.ocltv,oltvRange))))
    ocltvOltvminor=minor((list(map(lambda x: x.ocltv,oltvRange))))
    ocltvOltvhigher=higher((list(map(lambda x: x.ocltv,oltvRange))))
    ocltvRangeOltv=list(filter(lambda x: x.ocltv>=ocltvOltvminor and x.ocltv<=ocltvOltvhigher ,oltvRange))
    ocltvPorcentOltv=getPercentage(ocltvRangeOltv,len(ocltvOltvListRange))
    return ocltvRangeOltv
def mipOltv(oltvRange):
    mipOltvListRange=collections.Counter((list(map(lambda x: x.mip,oltvRange))))
    mipOltvminor=minor((list(map(lambda x: x.mip,oltvRange))))
    mipOltvhigher=higher((list(map(lambda x: x.mip,oltvRange))))
    mipRange=list(filter(lambda x: x.mip>=mipOltvminor and x.mip<=mipOltvhigher ,oltvRange))
    mipPorcent=getPercentage(mipRange,len(mipOltvListRange))
    return mipRange
def oltMip(mipRange):   
    oltMipListRange=collections.Counter((list(map(lambda x: x.olt,mipRange))))
    oltMipminor=minor((list(map(lambda x: x.olt,mipRange))))
    oltMiphigher=higher((list(map(lambda x: x.olt,mipRange))))  
    oltRangeMip=list(filter(lambda x: x.olt>=oltMipminor and x.olt<=oltMiphigher ,mipRange))
    oltPorcentMip=getPercentage(oltRangeMip,len(oltMipListRange))
    return oltRangeMip
def ranges(grupo,mid,idGrupo,listToSearch,listToEval):
    listCs=csRange(grupo,mid,listToSearch,listToEval)
    csminor=listCs[0].cs
    cshigher=listCs[(len(listCs)-1)].cs
    listOltvCs=oltvCs(listCs)
    oltvCsminor=listOltvCs[0].oltv
    oltvCshigher=listOltvCs[(len(listOltvCs)-1)].cs
    listOir=oirRange(listCs)
    oirminor=listOir[0].oir
    oirhigher=listOir[len(listOir)-1].oir
    listOltvOir=oltvOir(listOir)
    oltvCsOirRange=list(filter(lambda x: x.oltv>=oltvCsminor and x.oltv<= oltvCshigher ,listOltvOir))
    oltvCsOirPorcent=getPercentage(oltvCsOirRange,len(listOltvCs))
    oltvminor=oltvCsOirRange[0].oltv
    oltvhigher=oltvCsOirRange[len(oltvCsOirRange)-1].oltv
    listOcltvOltv=ocltvOltv(listOltvCs)
    ocltvoltvminor=listOcltvOltv[0].ocltv
    ocltvoltvhigher=listOcltvOltv[len(listOcltvOltv)-1].ocltv
    listMip=mipOltv(listOltvCs)
    mipminor=listMip[0].mip
    miphigher=listMip[len(listMip)-1].mip
    listOltMip=oltMip(listMip)
    oltMipminor=listOltMip[0].olt
    oltMiphigher=listOltMip[len(listOltMip)-1].olt
    listOupb=oupbOir(listOir)   
    oupbminor=listOupb[0].oupb
    oupbhigher=listOupb[len(listOupb)-1].oupb
    listNobOupb=nobOupb(listOupb)
    nobminor=listNobOupb[0].nob
    nobhigher=listNobOupb[len(listNobOupb)-1].nob    
    listOcltvOupb=ocltvOupb(listOupb)
    ocltvOupbminor=listOcltvOupb[0].ocltv
    ocltvOupbhigher=listOcltvOupb[len(listOcltvOupb)-1].ocltv
    listOltOupb=oltOupb(listOupb)
    oltOuobminor=listOltOupb[0].olt
    oltOuobhigher=listOltOupb[len(listOltOupb)-1].olt
    listOltOir=oltOir(listOir)
    oltOirminor=listOltOir[0].olt
    oltOirhigher=listOltOir[len(listOltOir)-1].olt
    ocltvOltvOupbRange=list(filter(lambda x: x.ocltv>=ocltvoltvminor and x.ocltv<=ocltvoltvhigher ,listOcltvOupb))
    ocltvOltvOupbPorcent=getPercentage(ocltvOltvOupbRange,len(listOcltvOltv))               
    oltMipOupbRange=list(filter(lambda x: x.olt>=oltOuobminor and x.olt<=oltOuobhigher ,listOltMip))
    oltMipOupbPorcent=getPercentage(oltMipOupbRange,len(listOltOupb))
    if oltMipOupbPorcent >=70 :
        oupbMipOirRange=list(filter(lambda x: x.olt>=oltOirminor and x.olt<=oltOirhigher ,oltMipOupbRange))
        oupbMipOirPorcent=getPercentage(oupbMipOirRange,len(listOltOir))
        oltminor=oltOuobminor
        olthigher=oltOuobhigher    
    else:
        oltMipOirRange=list(filter(lambda x: x.olt>=oltOirminor and x.olt<=oltOirhigher,listOltMip))
        oupbMipOirPorcent=getPercentage(oltMipOirRange,len(listOltOir))
        oltOupbOirRange=list(filter(lambda x: x.olt>=oltOirminor and x.olt<=oltOirhigher,listOltOupb))
        oupbOltOirPorcent=getPercentage(oltOupbOirRange,len(listOltOir))        
        if oupbMipOirPorcent <= oupbOltOirPorcent: 
            oltminor=oltOupbOirRange[0].olt
            olthigher=oltOupbOirRange[len(oltOupbOirRange)-1].olt            
        else:
            oltminor=oltMipOirRange[0].olt
            olthigher=oltMipOirRange[len(oltMipOirRange)-1].olt
    rangs=Perfil(csminor,cshigher,oirminor,oirhigher,oltvminor,oltvhigher,mipminor,miphigher,ocltvoltvminor,ocltvoltvhigher,nobminor,nobhigher,oupbminor,oupbhigher,oltminor,olthigher,idGrupo)
    return rangs

data=[]
data=readFile()
perfiles=[]
listToSearch=[]
listToEval=[]
grupo0complete=(list(filter(lambda x: x.grupo==0 ,data)))
grupo0final=(list(filter(lambda x: x.cs>= 660 ,grupo0complete)))
perfiles.append(ranges(grupo0final,832,0,listToSearch,listToEval))
grupo1complete=(list(filter(lambda x: x.grupo==1 ,data)))
grupo1final=(list(filter(lambda x: x.cs>=660 ,grupo1complete)))
perfiles.append(ranges(grupo1final,850,1,listToSearch,listToEval))
grupo2complete=(list(filter(lambda x: x.grupo==0 ,data)))
grupo2final=(list(filter(lambda x: x.cs>=510 ,grupo2complete)))
perfiles.append(ranges(grupo2final,660,2,listToSearch,listToEval))
grupo3complete=(list(filter(lambda x: x.grupo==1 ,data)))
grupo3final=(list(filter(lambda x: x.cs>=428 ,grupo3complete)))
perfiles.append(ranges(grupo3final,660,3,listToSearch,listToEval))
grupo4complete=(list(filter(lambda x: x.grupo==2 ,data)))
grupo4final=(list(filter(lambda x: x.cs>=660  ,grupo4complete)))
perfiles.append(ranges(grupo4final,826,4,listToSearch,listToEval))
grupo5complete=(list(filter(lambda x: x.grupo==3 ,data)))
grupo5final=(list(filter(lambda x: x.cs>=420  ,grupo5complete)))
perfiles.append(ranges(grupo5final,660,5,listToSearch,listToEval))
grupo6complete=(list(filter(lambda x: x.grupo==4 ,data)))
grupo6final=(list(filter(lambda x: x.cs>=660  ,grupo6complete)))
perfiles.append(ranges(grupo6final,820,6,listToSearch,listToEval))
grupo7complete=(list(filter(lambda x: x.grupo==5 ,data)))
grupo7final=(list(filter(lambda x: x.cs>=520 ,grupo7complete)))
perfiles.append(ranges(grupo7final,820,7,listToSearch,listToEval))
cantGroup=7
if len(listToSearch)>0:
    for i in listToSearch:
        porcentG=searchGroup(i,perfiles)
if len(listToEval)>0:
    for i in listToEval:
        porcentG=searchGroup(i,perfiles)
        if porcentG<70:
            cantGroup+=1
            perfiles.append(ranges(i,i[len(i)-1].cs,cantGroup,listToSearch,listToEval))
            
outputFile=open("perfilesFinalesgrupo.txt","w+") 
for person in perfiles:
        outputFile.write(str(person.csminor)+ "|" +  str(person.cshigher) + "|" +   str(person.oirminor) + "|" +   str(person.oirhigher)+ "|" +str(person.oltvminor) + "|"  + str(person.oltvhigher) + "|" +    str(person.mipminor) + "|" +    str(person.miphigher) + "|" +   str(person.ocltvminor) + "|" +    str(person.ocltvhigher) + "|" +    str(person.nobminor) + "|" +   str(person.nobhigher) + "|" +  str(person.oupbminor) + "|" +    str(person.oupbhigher) + "|" +    str(person.oltminor) + "|" +    str(person.olthigher)+ "|" +   str( person.grupo ))
outputFile.close() 