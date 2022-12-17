import os
import shutil

readFrom =%pathname%
dst=%dstpath%
fileList = os.listdir(readFrom)
idList=[]
files=[]
test= [1,1,1,1,1,2,3,4,4]
appendList =[[],[],[],[]]



appendList.append
def checkPath (path,dirName):
    if (not (os.path.isdir(path + "/" + dirName))):
        os.mkdir(path + "/" + dirName)
    

for eachLine in fileList:
    if eachLine.endswith(".tiff"):
        stripLine= eachLine.strip ("\n")
        x=stripLine.split ("_")
        idList.append (x[0])
     

counter=0
i=1

#checkPath(dst,"0")
#shutil.move(readFrom + "/" + fileList[0], dst + "/0/" + fileList[0])
appendList[0].append(idList[0]);

while (i < len(idList)):
    
                
    if (idList[i]==idList[i-1]):
        counter=counter+1
    else:
        counter=0
    print(counter)
    
    appendList[counter].append(idList[i]);
    #checkPath(dst,str(i))
    #shutil.move(readFrom + "/" + fileList[i], dst + "/" + str(counter) + "/" + fileList[i])

    i=i+1




