import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np





img2=cv2.imread("/home/ahmed/Desktop/wafer.jpg")
print(img2.shape)
img2_resized = cv2.resize(img2, (1200,1200), interpolation=cv2.INTER_LINEAR)
print(img2_resized.shape)
rows,cols,chan=img2_resized.shape
gap=300
p=0
for l in range(0,rows,gap):
 for i in range(0,cols,gap):
    j=i+gap
    m=l+gap
    face=img2_resized[l:m,i:j]
    y=m-l
    x=j-i
    img1 = Image.new('RGB', (cols , y), color = 'white')
    img1=face
    cv2.imwrite("/home/ahmed/Desktop/data/frame"+str(p)+".jpg",face)
    p=p+1








