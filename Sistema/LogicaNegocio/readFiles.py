from DTO import Origination
def readFile():
    data=[]
    with open('..\\Repositorio de datos\\data_grupos.csv','r') as filestream:
        for line in filestream:
            currrentline=line.split(",")
            CS=currrentline[0]
            FPD=currrentline[1]
            FTHF=currrentline[2]
            MD=currrentline[3]
            MSA=currrentline[4]
            MIP=currrentline[5]
            NOU=currrentline[6]
            OS=currrentline[7]
            OCLTV=currrentline[8]
            ODTIR=currrentline[9]
            OUPB=currrentline[10]
            OLTV=currrentline[11]
            OIR=currrentline[12]
            CHANNEL=currrentline[13]
            PPMFMF=currrentline[14]
            PT=currrentline[15]
            PS=currrentline[16]
            PT2=currrentline[17]
            PC=currrentline[18]
            LSQN=currrentline[19]
            LP=currrentline[20]
            OLT=currrentline[21]
            NOB=currrentline[22]
            SN=currrentline[23]
            SEN=currrentline[24]
            SCF=currrentline[25]
            PHLSN=currrentline[26]
            group=currrentline[27]
            if len(data)== 0:
                CS='450'     
            person=Origination(float(CS),FPD,FTHF,MD,float(MSA),float(MIP),float(NOU),OS,float(OCLTV),float(ODTIR),float(OUPB),float(OLTV),float(OIR),CHANNEL,PPMFMF,PT,PS,PT2,float(PC),LSQN,LP,float(OLT),float(NOB),SN,SEN,SCF,PHLSN,float(group))   
            data.append(person)
        
    return data
readFile()