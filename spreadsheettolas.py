import os, re

readFile = %filename%
readFrom = %pathname%

fileEdit= open(readFrom + "/" + readFile)

idList=[]
splitList=[]


def lasser (startVal,endVal,UWI,name,valueList):
    readto = "C:/Users/noyahr/Desktop/Auto SH Core/"

    
    newLas = open(readto + UWI + ".las","w+")
    
    newLas.write("""# LAS format log file from PETREL
# Project units are specified as depth units
#==================================================================
~Version information
VERS.   2.0:
WRAP.   NO:
#==================================================================
~Well
STRT .m      """ + startVal + """ :
STOP .m      """ + endVal + """ :
STEP .m     0.00000000 :
NULL .        -999.250000 :
COMP.           : COMPANY,
WELL.  """ + name + """   : WELL
FLD.            : FIELD
LOC.            : LOCATION
SRVC.           : SERVICE COMPANY
DATE.  2019-03-12 23:58:29   : Log Export Date {yyyy-MM-dd HH:mm:ss}
PROV.           : PROVINCE
UWI.   """ + UWI + """   : UNIQUE WELL ID
API.            : API NUMBER
#==================================================================
~Curve
DEPT .m                   : DEPTH
Permeability .mD          : Permeability
Porosity .m3/m3           : Porosity
~Parameter
#==================================================================
~Ascii\n"""
+ valueList)


    newLas.close()


for eachLine in fileEdit:

    strippedLine = eachLine.strip("\n")
    x=strippedLine.split(",")

    splitList.append(x)

j=0
startVal = 0
valueList=""          
for i in range (0,len(splitList)-1):
    
    if(splitList[j][0]==splitList[j+1][0]):
        valueList=valueList + " " + splitList[j][7] + " " + splitList[j][8] + " " + splitList[j][10] + "\n"
    else:
        valueList= valueList + " " + splitList[j][7] + " " + splitList[j][8] + " " + splitList[j][10]
        lasser(splitList[startVal][7],splitList[j][7],re.sub("[\/\-]",'',splitList[j][0]),splitList[j][1],valueList)
        valueList=""
        startVal=j+1
    j=j+1


valueList= valueList + " " + splitList[j][7] + " " + splitList[j][8] + " " + splitList[j][10]

lasser(splitList[startVal][7],splitList[j][7],re.sub("[\/\-]",'',splitList[j][0]),splitList[j][1],valueList)

print ("finito")
