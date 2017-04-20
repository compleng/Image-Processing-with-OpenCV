#!/usr/bin/env python
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import time


img = cv2.imread("crowd.png",cv2.IMREAD_GRAYSCALE)
#-------------------------------------------------------------------------
def flipImage(im,indic):
  if (indic==0):
    horizontal_img = cv2.flip( im, 0 )
    cv2.imwrite( "output/horizontal.jpg", horizontal_img )
   
  elif (indic==1):
    vertical_img = cv2.flip( img, 1 )
    cv2.imwrite( "output/vertical.jpg", vertical_img )
   
#-------------------------------------------------------------------------
def takeNeg(im):

 im2 = (255-im)
 cv2.imwrite('output/negative_image.jpg',im2)
 
#-------------------------------------------------------------------------
def averageIntensity(im):
 average_color_per_row = np.average(im, axis=0)#calculation for rows.if it is 1 then for columns
 average_color = np.average(average_color_per_row, axis=0)

 average_color = np.uint8(average_color) #convert floating point to int
 average_color_img = np.array([[average_color]*100]*100, np.uint8)
 print "Average intensity is:%s" % average_color
 cv2.imwrite( "output/average_intensity.jpg", average_color_img )

 return average_color
#-------------------------------------------------------------------------
def thresholdImage(im,val):
 value=val
 maxValue = 255
 th,dst = cv2.threshold(im, value, maxValue, cv2.THRESH_BINARY);
 cv2.imwrite("output/thresholded_image.jpg",dst)

#-------------------------------------------------------------------------
def thresholdWithAvg(im):
 average_color_per_row = np.average(img, axis=0)#calculation for rows.if it is 1 then for columns
 average_color = np.average(average_color_per_row, axis=0)
 average_color = np.uint8(average_color) #convert floating point to int
 thresh = average_color
 maxValue = 255
 th,dst = cv2.threshold(img, thresh, maxValue, cv2.THRESH_BINARY);
 cv2.imwrite( "output/threshold_with_average.jpg", dst )
 
#-------------------------------------------------------------------------
def generateHistogram(im):
 height=im.shape[0]
 width=im.shape[1]
 histog = [0,0]*128
 for i in range(height):
   for j in range(width):
     histog[im[i,j]]+=1
 print "histogram:%s" % histog
 plt.hist(im.ravel(),256,[0,256]); 
 plt.show()
 
 
#-------------------------------------------------------------------------
def equalizeHistogram(im):
 height=im.shape[0]
 width=im.shape[1]
 histog = [0,0]*128
 for i in range(height):
   for j in range(width):
     histog[im[i,j]]+=1

 divide = np.array(histog) /(height*width*1.0)
 sum=0

 my_list=list()
 for i in divide:
     sum=float(i)+sum
   
     my_list.insert(len(my_list),sum)
     
 my_new_list = [math.floor(int(i * 255)) for i in my_list]

 last_list= np.zeros_like(im)
 a=0
 b=0

 for a in range(0,height):
   for b in range(0,width):
	
     last_list[a,b]=my_new_list[im[a,b]]	



 last_list_hist=[0,0]*128
 for i in range(height):
   for j in range(width):
     last_list_hist[last_list[i,j]]+=1

 plt.title("Before Equalization")
 plt.hist(im.ravel(),256,[0,256]); 
 plt.show()
 plt.title("After Equalization")
 plt.hist(last_list.ravel(),256,[0,256]);

 
 plt.show()
 
 cv2.imwrite("output/equalized_picture.jpg",last_list)


#-------------------------------------------------------------------------
print "\n------------------------------WELCOME-----------------------------------\n"
print "For flipImage() function, type 1:"
print "For takeNeg() function, type 2:"
print "For averageIntensity() function, type 3:"
print "For thresholdImage() function, type 4:"
print "For thresholdWithAvg() function, type 5:"
print "For generateHistogram() function, type 6:"
print "For equalizeHistogram() function, type 7:"
print "Type Q to end program.." 
print"-------------------------------------------------------------------------"

while(True):
 inp=raw_input("Please choose the function you want...\n")

 if(inp=='1'):
  inp_type=input("For horizontal type 0,for vertical type 1:\n")
  flipImage(img,inp_type)
  print"Done.."
  print"Your picture is saved into project/output/ "
  print"-------------------------------------------------------------------------"
 elif(inp=='2'):
  takeNeg(img)
  print"Done.."
  print"Your picture is saved into project/output/ "
  print"-------------------------------------------------------------------------"
 elif(inp=='3'):
  averageIntensity(img)
  print"Done.."
  print"Your picture is saved into project/output/ "
  print"-------------------------------------------------------------------------"
 elif(inp=='4'):
  inp_type=input("Please type threshold value:")
  thresholdImage(img,inp_type)
  print"Done.."
  print"Your picture is saved into project/output/ "
  print"-------------------------------------------------------------------------"
 elif(inp=='5'):
  thresholdWithAvg(img)
  print"Done.."
  print"Your picture is saved into project/output/ "
  print"-------------------------------------------------------------------------"
 elif(inp=='6'):
  generateHistogram(img)
  print"Done.."
  print"-------------------------------------------------------------------------"
 elif(inp=='7'):
  equalizeHistogram(img)
  print"Done.."
  print"Your picture is saved into project/output/ "
  print"-------------------------------------------------------------------------"
 elif(inp=="q" or inp=="Q"):
  break;
 else:
  print "You type something wrong"
  print"-------------------------------------------------------------------------"
