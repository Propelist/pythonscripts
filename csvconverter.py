
import os

#defines a class where functions carried out will be carried on entire stack


filepath=%srcfolder%;

fileList=os.listdir(filepath);
fileNames=[]
for each in fileList:
    print(each)
    fileNames.append(each.split(".")[0])

i=0

for eachFile in fileList:
    newStr=""
    
    fileEdit=open(filepath+eachFile,"r")

    j=0
    for eachLine in fileEdit:
        if j==0:
            j=j+1
        else:
            for eachChar in eachLine:
                if (eachChar==" "):
                    pass
                if (eachChar==","):
                    newStr=newStr + "\t"
                else:
                    newStr=newStr+ eachChar

    newFile=open(filepath + fileNames[i] + ".txt","w")
    newFile.write(newStr)
    newFile.close()
    fileEdit.close()
    i=i+1
