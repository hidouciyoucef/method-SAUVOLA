

import numpy as np
from PIL import Image
import pylab as plt

#chargement en mode NDG et conversion en matrice NUMPY
imNDG = Image.open('peppers.bmp').convert('L')

imgMat = np.array(imNDG) #convertion d l'image vers une matrice

sizeM = int(input('get size Masque '))
filtre = np.ones((sizeM,sizeM))/(sizeM**2)
sizeF = len(filtre)
sizeF2 = len(filtre)//2

#calculer Mean de chaque pixel
def Mean(imageIn, filtre):
    imageOut= np.array(Image.new("L", (imageIn.shape[0], imageIn.shape[1])))
    
    
    for i in range(sizeF2,imageIn.shape[0]-sizeF2):
        for j in range(sizeF2,imageIn.shape[1]-sizeF2):
            somme = 0
            for m in range(sizeF):
                for n in range(sizeF):
                    somme += imageIn[i+m-sizeF2,j+n-sizeF2]*filtre[m,n]
            imageOut[i,j] = somme
    return imageOut


#calculer ECART-TYPE (STD) de chaque pixel
def STD(imageIn,MeanIn):
    VAR1= np.array(Image.new("L", (imageIn.shape[0], imageIn.shape[1])))
    
    for i in range(sizeF2,imageIn.shape[0]-sizeF2):
        for j in range(sizeF2,imageIn.shape[1]-sizeF2):
            somme = 0
            for m in range(sizeF):
                for n in range(sizeF):
                    somme += (int(imageIn[i+m-sizeF2,j+n-sizeF2])-int(MeanIn[i,j]))**2
            VAR1[i,j] = np.sqrt(somme//(sizeF**2))
    return VAR1


#Appliquer la methode sauvola sur chaque pixel (thresholding)
def MET_SAUVOlA(imageIn,STDIN,MeanIn):
    imageOut= np.array(Image.new("L", (imageIn.shape[0], imageIn.shape[1])))
    k=0.2
    R=128
    for i in range(sizeF2,imageIn.shape[0]-sizeF2):
        for j in range(sizeF2,imageIn.shape[1]-sizeF2):
            imageOut[i,j]=(MeanIn[i,j]*(1+k*((STDIN[i,j]/R)-1))) 
                  
    return imageOut    

#Comparer entre chaque pixel de l'image original et chaque pixel de nouvelle matrice contiene les valeurs de tech sauvola
def BINARIZATION(imageIn,TIN):
    imageOut= np.array(Image.new("L", (imageIn.shape[0], imageIn.shape[1])))
    for i in range(sizeF2,imageIn.shape[0]-sizeF2):
        for j in range(sizeF2,imageIn.shape[1]-sizeF2):
            if imageIn[i,j]>=TIN[i,j]:
                imageOut[i,j]=255
            else:
                imageOut[i,j]=0
    return imageOut           
        
MATMean = Mean(imgMat, filtre)
MATSTD = STD(imgMat,MATMean )
T = MET_SAUVOlA(imgMat,MATSTD,MATMean)
B = BINARIZATION(imgMat,T)


plt.figure(1)
plt.imshow(imNDG)

plt.figure(2)
plt.imshow(Image.fromarray(B))


plt.show()

