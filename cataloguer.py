import os, csv
readFile=%filename%
readFrom =%pathname%

fileEdit= open(readFrom + "/" + readFile)
idList=[]
newList=[[],[],[],[]]
y=0

for eachLine in fileEdit:

    if (y != 0): 

        strippedLine = eachLine.strip("\n")
        x=strippedLine.split(",")
        idList.append((x[0],x[4],x[5]))

    y=y+1

i=1
counter=0

newList[0].append(idList[0])

while (i < len(idList)):
    

    
    if (idList[i][0]==idList[i-1][0]):
        counter=counter+1
    else:
        counter=0
    
    newList[counter].append(idList[i])
    i=i+1
    print(counter)
d=0

for each in newList:
    print each


for each in newList:
    with open(readFrom + "/new" + str (d) + ".csv","wb") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(each)
    d=d+1

    
print ("Completed")

