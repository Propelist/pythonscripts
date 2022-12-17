import os
import time
import datetime

dir =%pathname%
file=%filename%
nameList=os.listdir(dir)
newFile=open(dir + filename,"w")

for each in nameList:
    t =os.path.getmtime(dir+ "/" + each)
    #datetime.datetime.strptime(str(t), "%a %b %d %H:%M:%S %Y")
    date=time.strftime("%a %b %d %H:%M:%S %Y",time.gmtime(t))
    newFile.write(each +"\t" + str(date) + "\n")

newFile.close()
