
import os 
readFile=%filename%
readFrom =%pathname%

fileList= os.listdir(readFrom);
fileEdit= open(readFrom + "/" + readFile)

i=0
for eachLine in fileEdit:
    

    strippedLine = eachLine.strip("\n")
    x=strippedLine.split(",")
    print(readFrom + "/" + fileList[i])
    #print(readFrom + "/" + x[0] + "_" + x[1] +"__" + x[4] + "___" +x[5] +".tiff")
    #os.rename(readFrom + "/" + fileList[i],readFrom + "/" + x[0] + "_" + x[1] +"__" + x[4] + "___" +x[5] +".tiff")
    #print (fileList)
    i=i+1 



