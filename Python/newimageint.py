import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg
from matplotlib.pyplot import figure
import numpy as np
from skimage.measure import profile_line
from skimage import io
import math
from scipy.optimize import curve_fit

image=r"C:\Users\Tim Stechel\OneDrive\Dokumente\Photonics\InnovationMethods\Images\20.06\laser engraved grid, 13.5cm, 0.12 ms exposure time.tif"

filenameraw=image.split('\\')                  ##extract filename for saving later on
filenamevirt=filenameraw[9].split('.ti')
filename=filenamevirt[0]


l=150 #distance Lens-sensor in mm
width=1600  #image parameters
height=1200

center=width/2
pixelsize=0.0045 #pixelsize in mm 7.11mm/1600pixels

h=height/2 #y height of profile to be examined


figure(figsize=(8, 6), dpi=200)

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
    
angle_dep_array=np.array(angle_dep)
normalized_p_array=np.array(normalized_p)


###curvefit of angular dependence
def func(x, a, b):

    return -a*x**2+b
popt, pcov = curve_fit(func, angle_dep_array, normalized_p_array)



# Extract values from image directly for comparison
#i = I[0:1599]

img=mpimg.imread(image)



'''
plt.subplot(221)
plt.title('Original Image')
plt.imshow(img)
plt.ylabel('y [pixels]')
plt.xlabel('x [pixels]')
***'''
plt.subplot(121)
plt.title('Int. distribution in center')
plt.plot(normalized_p,label='normalized')
plt.plot(p,label="non normalized")
plt.ylabel('Intensity [a.u.]')
plt.xlabel('Line path [pixels]')
plt.legend()

plt.subplot(122)
plt.title('Angular Intensity Distribution')
plt.plot(angle_dep,normalized_p)
plt.plot(angle_dep,func(angle_dep_array, *popt), 'r-', label='fit: -%5.3f*x^2+%5.3f' % tuple(popt))
plt.ylabel("Intensity normalized")
plt.xlabel("Angle from center of image [°]")
plt.legend()



plt.savefig(r"C:\Users\Tim Stechel\OneDrive\Dokumente\Photonics\InnovationMethods\Images\\20.06\\"+filename+".png")
plt.show()  


