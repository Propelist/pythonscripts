
from PIL import Image
import os
from Image import ANTIALIAS


#defines a class where functions carried out will be carried on entire stack
class imgStack:
    
    
    #takes a directory which 
    def __init__(self, directory):
        self.directory=directory
        self.imgList=self.cleanseDir(os.listdir(directory))

    def contraster(self,name):
        
        i=0
        print(self.imgList)
        for each in self.imgList:
            
            im = Image.open(self.directory + each)
            ogPixels=im.getdata()
            edPixels = []
            
            
            for eachPixel in ogPixels:
                self.makeAlpha(edPixels,eachPixel)
            
            
            im2=Image.new("L",im.size)
            #print(edPixels)
            im2.putdata(edPixels)
            if not os.path.exists(self.directory+"/corrected/"):
                os.makedirs(self.directory+"/corrected/")
            im2.save(self.directory + "/corrected/" + name + str(i) +".png");
            print("Image" + str(i) +" Complete!")
        
            i= i+1
        
        print("Contrasting done")
  
        
    def makeAlpha(self,edPixels,eachPixel):
    
        if (eachPixel<= 130 or eachPixel>= 155):
            
            edPixels.append(0)
        else:
            edPixels.append(eachPixel)
    
        return eachPixel;

   #directory, which is path of directory
    #imgList, which is list of images in directory
    #square is a 4 tuple defining square B,L,T,R
    #name is the desired name of the output directory
        #arenicolites dimensions
        #im=im.crop((254,932,570,1206))
        #Macaronichnus1 dimensions
        #im=im.crop((454,678,1260,1410))
    def cropper(self,square,name):
    
        i=0
        
        for eachImg in self.imgList:
            
            im=Image.open(self.directory + eachImg)
            
            
            #arenicolites dimensions
            im=im.crop(square)
            #Macaronichnus1 dimensions
            #im=im.crop((454,678,1260,1410))       
            
            if not os.path.exists(self.directory+"/cropped/"):
                os.makedirs(self.directory+"/cropped/")
                                
            im.save(self.directory +"/cropped/" + name + str(i) + ".png")


            i=i+1
        
        print("Crop Complete!")
    
    
    #directory, which is path of directory
    #imgList, which is list of images in directory
    #sizer is 2-tuple w,h, in my case 2954,1557
    def resizer(self,sizer):
        
        i=0
        
        for eachImg in self.imgList:
            
                im=Image.open(self.directory + eachImg)
                
                im=im.resize(sizer,ANTIALIAS)
                
                if not os.path.exists(self.directory+"/resize/"):
                    os.makedirs(self.directory+"/resize/")
                im.save(self.directory+"/resize/"+eachImg)
                    
                i=i+1
        print("Resize Finished")
            
    def cleanseDir(self,dirItems):
        
        cleansedList= []
        for eachItem in dirItems:
            if eachItem.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp','gif','.tiff')):
                cleansedList.append(eachItem)
        
        return cleansedList



directory="D:/chris n/set7-20170221T001814Z/"
directory2="C:/Users/Chris/workspace/PILprocessor/CROPPED ORIGINALS/"
directory3="C:/Users/Chris/workspace/PILprocessor/CROPPED ORIGINALS/resize/8BIT/"
newStack1= imgStack(directory3)
newStack1.contraster("fixed");

