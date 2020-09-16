import pyautogui
import numpy as np 
import pytesseract

import time
import cv2
import os
from PIL import Image, ImageGrab 
time.sleep(2)
filename = 'Image.png'
x=1

while(True):
    
    screen = np.array(ImageGrab.grab(bbox=(610 ,1035 ,748 ,1060)))
    
    cv2.imshow('window',cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
    cv2.imwrite(filename,screen)
    img = cv2.imread('Image.png')
    text = pytesseract.image_to_string(img,lang='rus')
    text1 = text.split()
    for t in text1: 
      
      for te in t:
       
       if te == "В":
           print("привет маме адиля")
   

   
    time.sleep(0.1)
    print(x)    
    if x==2:
       cv2.destroyAllWindows()
       break

