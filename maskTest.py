########################
#                      #
# TEC Watermark Test   #
#                      #
########################

import cv2
import numpy

# read in image
#     get size
# read in prime fwd -- byte to insert
#     read for size only
# read in prime bckwrd -- position
#     read in for size only
# modify matrix
#     
# write out new image


# read in image
img=cv2.imread("TEC Watermark Test 001.jpg")
# get size
numPixels=img.size

addPixel=open("M77232917.txt","r")

maskPixels=[]
maskPos=[]

#for x in range(0,numPixels):
#     maskPixels.append(addPixel.read(1))
#for x in range(numPixels,0,-1):
#     maskPos.append(maskPixesls[x])

# append q or ~q
for x in range(0,numPixels):
     q=addPixel.read(1)
     if (q!='\n'):
          maskPixels.append(255-int(q))

for x in range(numPixels-1,-1,-1):
     maskPos.append(maskPixels[x])

rows, cols, atype = img.shape
z=0
for row in range(0,rows-1):
     for col in range(0,cols-1):
          for pVal in range(0,2):
               img[row,col,pVal]=img[row,col,pVal]+int(maskPixels[z])
               z=z+1

rows, cols, atype = img.shape
z=0
for row in range(0,rows-1):
     for col in range(0,cols-1):
          for pVal in range(0,2):
          img[row,col,pVal]=img[row,col,pVal]+int(maskPixels[z])
          z=z+1

rows, cols, atype = img.shape
z=0
for row in range(0,rows-1):
     for col in range(0,cols-1):
          img[row,col,2]=img[row,col,2]+int(maskPixels[z])
          z=z+1

cv2.imwrite("outfile3.jpg",img)


