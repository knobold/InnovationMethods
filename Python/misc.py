image=r"C:\Users\Tim Stechel\OneDrive\Dokumente\Photonics\InnovationMethods\Images\20.06\0.5mm grid 13.5cm 0.67 ms.tif"



filenameraw=image.split('\\')

print(filenameraw)

filenamevirt=filenameraw[9].split('.ti')
filename=filenamevirt[0]
print(filename)

#pathtosaveto="C:\Users\Tim Stechel\OneDrive\Dokumente\Photonics\InnovationMethods\Images\20.06"+filename+".png"

print(r"C:\Users\Tim Stechel\OneDrive\Dokumente\Photonics\InnovationMethods\Images\20.06"+str(filename)+".png")