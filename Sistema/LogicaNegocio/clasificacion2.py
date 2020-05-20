from DTO import Origination
from readFiles import readFile
#Defining the structure of classification rules for the CS variable
def porcentcs(cs):
    csporcent=[0,0,0,0,0,0,0,0] #Storage of percentages for each group
    if cs <= 668:
        if 422<= cs and cs<=560:
            csporcent[5]=1 #Storing group detection
            if 548<=cs and cs<=660:
                csporcent[2]=1#Storing group detection
                if 562<=cs and cs<=642:
                    csporcent[7]=1#Storing group detection
                    if 597<=cs and cs <=617:
                        csporcent[3]=1     #Storing group detection           
        else:
            if 548<=cs and cs<=660:
                csporcent[2]=1  #Storing group detection
                if 562<=cs and cs<=642:
                    csporcent[7]=1  #Storing group detection
                    if 597<=cs and cs <=617:
                        csporcent[3]=1  #Storing group detection
    else:
        csporcent[0]=1  #Storing group detection
        if 706<=cs and cs<=738:
            csporcent[1]=1  #Storing group detection
        else:
            if 739<=cs and cs<=817:
                csporcent[6]=1  #Storing group detection
                if 756<=cs and cs<=805:
                     csporcent[4]=1  #Storing group detection
            else:
                if 756<=cs and cs<=805:
                    csporcent[4]=1  #Storing group detection
    return csporcent
#Defining the structure of classification rules for the OIR variable
def porcentoir(oir):
    oirporcent=[0,0,0,0,0,0,0,0] #Storage of percentages for each group
    if oir <= 4.375:
        if 2.875<=oir and oir <=5.875:
            oirporcent[3]=1#Storing group detection
            if 3<= oir and oir<=4.37:
                oirporcent[7]=1#Storing group detection
            if 3.625<=oir and oir<=5:
                oirporcent[0]=1#Storing group detection
            if 4.25<=oir and oir<=5.125:
                oirporcent[2]=1#Storing group detection
    else:
        if 4.375<=oir and oir<=5.875:
            oirporcent[1]=1#Storing group detection
            if 4.375<=oir and oir<=5.375:
                oirporcent[6]=1#Storing group detection
                if 4.375<=oir and oir<= 4.875:
                    oirporcent[4]=1#Storing group detection
                if 4.875<=oir and oir<=5.375:
                    oirporcent[5]=1#Storing group detection
        if 2.875<=oir and oir <=5.875:
            oirporcent[3]=1#Storing group detection
            if 3.625<=oir and oir<=5:
                 oirporcent[0]=1#Storing group detection
                 if 4.25<=oir and oir<= 5.125:
                    oirporcent[2]=1#Storing group detection
    return oirporcent
#Defining the structure of classification rules for the OLTV variable
def porcentoltv(oltv):
    oltvporcent=[0,0,0,0,0,0,0,0] #Storage of percentages for each group
    if oltv<109:
        if 99 <=oltv and oltv<=109:
            oltvporcent[4]=1#Storing group detection
        if 81 <=oltv and oltv<=108:
            oltvporcent[3]=1#Storing group detection
            if 82<=oltv and oltv<=108:
                oltvporcent[7]=1#Storing group detection
                if 91 <=oltv and oltv<=97:
                    oltvporcent[5]=1#Storing group detection
                if 92 <=oltv and oltv<=105:
                    oltvporcent[0]=1#Storing group detection
                    if 98 <=oltv and oltv<=101:
                        oltvporcent[2]=1#Storing group detection
    else:
        if 85 <=oltv and oltv<=115:
            oltvporcent[1]=1#Storing group detection
        if 87 <=oltv and oltv<=135:
            oltvporcent[6]=1#Storing group detection

    return oltvporcent
    #Defining the structure of classification rules for the MIP variable
def porcentmip(mip):
    mipporcent=[0,0,0,0,0,0,0,0] #Storage of percentages for each group
    if mip<=25:
        mipporcent[1]=1#Storing group detection
        mipporcent[3]=1#Storing group detection
        if 0<=mip and mip <=35:
            mipporcent[2]=1#Storing group detection
            mipporcent[6]=1#Storing group detection
            mipporcent[7]=1#Storing group detection
            if 0<=mip and mip<=22:
                mipporcent[0]=1#Storing group detection
    else:
        if mip<=25 and mip<=41:
            mipporcent[5]=1#Storing group detection
            mipporcent[4]=1#Storing group detection
        else:
            if 0<=mip and mip <=35:
                mipporcent[2]=1#Storing group detection
                mipporcent[6]=1#Storing group detection
                mipporcent[7]=1#Storing group detection
    return mipporcent
    #Defining the structure of classification rules for the OCLTV variable
def porcentocltv(ocltv):
    ocltvporcent=[0,0,0,0,0,0,0,0] #Storage of percentages for each group
    if ocltv<90:
        if 82<=ocltv and ocltv<=153:
            ocltvporcent[7]=1#Storing group detection
            if 85<=ocltv and ocltv<=115:
                ocltvporcent[1]=1#Storing group detection
            if 87<=ocltv and ocltv<=135:
                ocltvporcent[6]=1#Storing group detection
    else:
        if ocltv<=90 and ocltv <=136:
            ocltvporcent[3]=1#Storing group detection
            if ocltv<=92 and ocltv<=105:
                ocltvporcent[0]=1#Storing group detection
            if ocltv<=90 and ocltv<=98:
                ocltvporcent[2]=1#Storing group detection
                if ocltv<=95 and ocltv<=97:
                    ocltvporcent[5]=1#Storing group detection
            if ocltv<=99 and ocltv<=109:
                ocltvporcent[4]=1#Storing group detection
        if 82<=ocltv and ocltv<=153:
            ocltvporcent[7]=1#Storing group detection
            if 85<=ocltv and ocltv<=115:
                ocltvporcent[1]=1#Storing group detection
            if 87<=ocltv and ocltv<=135:
                ocltvporcent[6]=1#Storing group detection
    return ocltvporcent
    #Defining the structure of classification rules for the OUPB variable
def porcenoupb(oupb):
    oupbporcent=[0,0,0,0,0,0,0,0] #Storage of percentages for each group
    if oupb<299000:
        if 115000 <=oupb and oupb<=144000:
            oupbporcent[6]=1#Storing group detection
        if 123000 <=oupb and oupb<=162000:
            oupbporcent[4]=1#Storing group detection
        if 170000<=oupb and oupb<=210000:
            if 172000<=oupb and oupb<=208000:
                oupbporcent[1]=1#Storing group detection
            else:
                oupbporcent[3]=1#Storing group detection
        else:
            if 245000<=oupb and oupb<=278000:
                oupbporcent[5]=1#Storing group detection
    else:
        if 299000<=oupb and oupb<=355999:
            oupbporcent[7]=1#Storing group detection
        if 356000<=oupb and oupb<=397000:
            if 358000<=oupb and oupb<=394000:
                oupbporcent[2]=1#Storing group detection
            else:
                oupbporcent[0]=1#Storing group detection
    return oupbporcent
#Defining the structure of classification rules for the OLT variable
def porcentolt(olt):
    oltporcent=[0,0,0,0,0,0,0,0] #Storage of percentages for each group
    if olt<180:
        if 81<=olt and olt<=142:
            oltporcent[5]=1#Storing group detection
            oltporcent[7]=1#Storing group detection
            if 81<=olt and olt<=121:
                oltporcent[1]=1#Storing group detection
        if 88<=olt and olt<=180:
            oltporcent[2]=1#Storing group detection
        if 120<=olt and olt<=340:
            oltporcent[6]=1#Storing group detection
        if 140<=olt and olt<=450:
            oltporcent[4]=1#Storing group detection
    else:
        if 180<=olt and olt<=594:
            oltporcent[3]=1#Storing group detection
            if 180<=olt and olt<=360:
                oltporcent[0]=1#Storing group detection
        if 88<=olt and olt<=180:
            oltporcent[2]=1#Storing group detection
        if 120<=olt and olt<=340:
            oltporcent[6]=1#Storing group detection
        if 140<=olt and olt<=450:
            oltporcent[4]=1#Storing group detection
    return oltporcent

#Function to apply importance percentages for group 0, receives as parameter the group detection array
def porcentgrup0(cs,oir,fthf,oltv,mip,ocltv,nob,oupb,olt):
    total=0
    cs=cs*10#Applying percentages
    oir=oir*5#Applying percentages
    if fthf==1:
        fthf=1
    else:
        fthf=0

    fthf=fthf*3#Applying percentages
    oltv=oltv*15#Applying percentages
    mip=mip*15#Applying percentages
    ocltv=ocltv*20#Applying percentages
    if nob==1:
        nob=1
    else:
        nob=0
    nob=nob*2#Applying percentages
    oupb=oupb*25#Applying percentages
    olt=olt*5#Applying percentages
    total=cs+oir+fthf+oltv+mip+ocltv+nob+oupb+olt #sum of percentages
    return total #membership percentage return
#Function to apply importance percentages for group 1, receives as parameter the group detection array
def porcentgrup1(cs,oir,fthf,oltv,mip,ocltv,nob,oupb,olt):
    total=0
    cs=cs*13#Applying percentages
    oir=oir*2#Applying percentages
    if fthf==1:
        fthf=1
    else:
        fthf=0

    fthf=fthf*3
    oltv=oltv*10#Applying percentages
    mip=mip*15
    ocltv=ocltv*25#Applying percentages
    if nob==1:
        nob=1
    else:
        nob=0
    nob=nob*2#Applying percentages
    oupb=oupb*25#Applying percentages
    olt=olt*5#Applying percentages
    total=cs+oir+fthf+oltv+mip+ocltv+nob+oupb+olt #sum of percentages
    return total#membership percentage return
#Function to apply importance percentages for group 2, receives as parameter the group detection array
def porcentgrup2(cs,oir,fthf,oltv,mip,ocltv,nob,oupb,olt):
    total=0
    cs=cs*5#Applying percentages
    oir=oir*5#Applying percentages
    if fthf==1:
        fthf=1
    else:
        fthf=0

    fthf=fthf*3#Applying percentages
    oltv=oltv*15#Applying percentages
    mip=mip*15#Applying percentages
    ocltv=ocltv*20#Applying percentages
    if nob==1:
        nob=1
    else:
        nob=0
    nob=nob*2#Applying percentages
    oupb=oupb*30#Applying percentages
    olt=olt*5#Applying percentages
    total=cs+oir+fthf+oltv+mip+ocltv+nob+oupb+olt#sum of percentages
    return total#membership percentage return
#Function to apply importance percentages for group 3, receives as parameter the group detection array
def porcentgrup3(cs,oir,fthf,oltv,mip,ocltv,nob,oupb,olt):
    total=0
    cs=cs*5
    oir=oir*2#Applying percentages
    if fthf==1:
        fthf=1
    else:
        fthf=0

    fthf=fthf*3#Applying percentages
    oltv=oltv*10#Applying percentages
    mip=mip*15#Applying percentages
    ocltv=ocltv*33#Applying percentages
    if nob==1:
        nob=1
    else:
        nob=0
    nob=nob*2#Applying percentages
    oupb=oupb*25#Applying percentages
    olt=olt*5#Applying percentages
    total=cs+oir+fthf+oltv+mip+ocltv+nob+oupb+olt#sum of percentages
    return total#membership percentage return
#Function to apply importance percentages for group 4, receives as parameter the group detection array
def porcentgrup4(cs,oir,fthf,oltv,mip,ocltv,nob,oupb,olt):
    total=0
    cs=cs*13#Applying percentages
    oir=oir*2#Applying percentages
    if fthf==1:
        fthf=1
    else:
        fthf=0

    fthf=fthf*3#Applying percentages
    oltv=oltv*10#Applying percentages
    mip=mip*15
    ocltv=ocltv*30#Applying percentages
    if nob==1:
        nob=1
    else:
        nob=0
    nob=nob*2#Applying percentages
    oupb=oupb*20#Applying percentages
    olt=olt*5#Applying percentages
    total=cs+oir+fthf+oltv+mip+ocltv+nob+oupb+olt#sum of percentages
    return total#membership percentage return
    #Function to apply importance percentages for group 5, receives as parameter the group detection array
def porcentgrup5(cs,oir,fthf,oltv,mip,ocltv,nob,oupb,olt):
    total=0
    cs=cs*5#Applying percentages
    oir=oir*2#Applying percentages
    if fthf==1:
        fthf=1
    else:
        fthf=0

    fthf=fthf*3#Applying percentages
    oltv=oltv*10#Applying percentages
    mip=mip*18#Applying percentages
    ocltv=ocltv*30#Applying percentages
    if nob==1:
        nob=1
    else:
        nob=0
    nob=nob*2#Applying percentages
    oupb=oupb*25#Applying percentages
    olt=olt*5#Applying percentages
    total=cs+oir+fthf+oltv+mip+ocltv+nob+oupb+olt#sum of percentages
    return total#membership percentage return
#Function to apply importance percentages for group 6, receives as parameter the group detection array
def porcentgrup6(cs,oir,fthf,oltv,mip,ocltv,nob,oupb,olt):
    total=0
    cs=cs*13#Applying percentages
    oir=oir*2#Applying percentages
    if fthf==1:
        fthf=1
    else:
        fthf=0

    fthf=fthf*3#Applying percentages
    oltv=oltv*10#Applying percentages
    mip=mip*15#Applying percentages
    ocltv=ocltv*25#Applying percentages
    if nob==1:
        nob=1
    else:
        nob=0
    nob=nob*2#Applying percentages
    oupb=oupb*25#Applying percentages
    olt=olt*5#Applying percentages
    total=cs+oir+fthf+oltv+mip+ocltv+nob+oupb+olt#sum of percentages
    return total#membership percentage return
#Function to apply importance percentages for group 7, receives as parameter the group detection array
def porcentgrup7(cs,oir,fthf,oltv,mip,ocltv,nob,oupb,olt):
    total=0
    cs=cs*5#Applying percentages
    oir=oir*5#Applying percentages
    if fthf==1:
        fthf=1
    else:
        fthf=0

    fthf=fthf*3#Applying percentages
    oltv=oltv*15#Applying percentages
    mip=mip*15#Applying percentages
    ocltv=ocltv*20#Applying percentages
    if nob==1:
        nob=1
    else:
        nob=0
    nob=nob*2#Applying percentages
    oupb=oupb*30#Applying percentages
    olt=olt*5#Applying percentages
    total=cs+oir+fthf+oltv+mip+ocltv+nob+oupb+olt#sum of percentages
    return total#membership percentage return
    
def grupoPertence(cs,oir,fthf,oltv,mip,ocltv,nob,oupb,olt):
    #Applying the percentages for each group, using percentage functions
    csp=porcentcs(cs)
    oirp=porcentoir(oir)
    oltvp=porcentoltv(oltv)
    mipp=porcentmip(mip)
    ocltvp=porcentocltv(ocltv)
    oupbp=porcenoupb(oupb)
    oltp=porcentolt(olt)
    #Saving the percentage of each group
    cero=porcentgrup0(csp[0],oirp[0],fthf,oltvp[0],mipp[0],ocltvp[0],nob,oupbp[0],oltp[0])
    uno=porcentgrup1(csp[1],oirp[1],fthf,oltvp[1],mipp[1],ocltvp[1],nob,oupbp[1],oltp[1])
    dos=porcentgrup2(csp[2],oirp[2],fthf,oltvp[2],mipp[2],ocltvp[2],nob,oupbp[2],oltp[2])
    tres=porcentgrup3(csp[3],oirp[3],fthf,oltvp[3],mipp[3],ocltvp[3],nob,oupbp[3],oltp[3])
    cuatro=porcentgrup4(csp[4],oirp[4],fthf,oltvp[4],mipp[4],ocltvp[4],nob,oupbp[4],oltp[4])
    cinco=porcentgrup5(csp[5],oirp[5],fthf,oltvp[5],mipp[5],ocltvp[5],nob,oupbp[5],oltp[5])
    seis=porcentgrup6(csp[6],oirp[6],fthf,oltvp[6],mipp[6],ocltvp[6],nob,oupbp[6],oltp[6])
    siete=porcentgrup7(csp[7],oirp[7],fthf,oltvp[7],mipp[7],ocltvp[7],nob,oupbp[7],oltp[7])
    lista = [cero,uno,dos,tres,cuatro,cinco,seis,siete]
    #Findig the biggest percentage in the list
    maximo = max(lista)
    grupo = lista.index(maximo)
    return grupo #Return the results of the group, index=number of the group