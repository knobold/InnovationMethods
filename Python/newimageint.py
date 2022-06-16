import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg
import numpy as np
from skimage.measure import profile_line
from skimage import io
import math

image=r"C:\Users\Tim Stechel\OneDrive\Dokumente\Photonics\InnovationMethods\Images\16.06\2MLA(0°).bmp"
l=55 #distance Lens-sensor in mm
width=800  #image parameters
height=600

center=width/2
pixelsize=0.0045 #pixelsize in mm 7.11mm/1600pixels

h=height/2 #y height of profile to be examined


I= io.imread(image, as_gray=True)
#I = mpimg.imread(image)



##### Extract intensity values along some profile line#####
p = profile_line(I, (h,1), (h,width))
norm=max(p)
c=0
for el in p:
    c+=1
    if el==max(p):
        
        print("x-center at: "+str(c)+" norm value = "+str(el))

normalized_p = p/norm




########## angle dependence ############
angle_dep=[]
c=0
for el1 in normalized_p:
    c+=1
    dif=pixelsize*(center-c)
    
    angle =math.degrees(np.arctan(dif/l))
    angle_dep.append(angle)
    






# Extract values from image directly for comparison
#i = I[0:1599]

img=mpimg.imread(image)

plt.subplot(131)
plt.plot(normalized_p,label='path at y='+str(h))
plt.plot(p,label="non normalized")
plt.ylabel('intensity [a.u.]')
plt.xlabel('line path [pixels]')
plt.legend()


plt.subplot(132)
plt.imshow(img)
plt.ylabel('y [pixels]')
plt.xlabel('x [pixels]')


plt.subplot(133)
plt.plot(angle_dep,normalized_p)
plt.ylabel("Intensity normalized")
plt.xlabel("Angle from focusing lens [°]")
plt.show()  