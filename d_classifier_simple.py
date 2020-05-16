from PIL import Image
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import pyautogui
import time
import cv2
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import os

cap = cv2.VideoCapture(0)

cnt=Counter()

def most_common(my_lis):
 for my_list in my_lis:
     cnt[my_list] += 1
 for i in cnt.most_common(1):
     j=0
     for x in i:
         lis=['','']
         lis[j]=x
         j=j+1
         return(lis[0])

def d_classifier(frame):  
 driver = webdriver.Chrome(r'C:\Users\Yousuf Traders\Desktop\chromedriver')
 driver.get("https://www.labnol.org/internet/mobile-reverse-image-search/29014/")
 time.sleep(10)
 driver.find_element_by_class_name("mks_button.mks_button_medium ").click()
 time.sleep(2)
 pyautogui.typewrite(frame)
 pyautogui.press('enter')
 time.sleep(20) #20
 driver.find_element_by_class_name("mks_button.mks_button_medium").click()
 time.sleep(10) #10
 driver.switch_to.window(driver.window_handles[1])
 driver.get(driver.current_url)
 continue_link = driver.find_element_by_tag_name('a')
 #elems = driver.find_elements_by_xpath("//a[@href]")
 elems = driver.find_elements_by_xpath("//*[@class]")
 f='.*?'
 u=0
 e=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']  
 #e=[]
 for elem in elems:
     k=elem.get_attribute("href")
     #p='\''+str(k)+'\''
     #print(k)
     findLinks=re.findall('&q'+f+'&',str(k))
     #print(findLinks)
     #e=['','','','','','','','','','',''] 
     for eachthing in findLinks:
         i=eachthing.replace('&q=', '')
         #print(i)
         a = i
         for k in a.split("\n"):
             e[u]=re.sub(r"[^a-zA-Z0-9]+", ' ', k)
         u=u+1         
 g=most_common(e)
 print(g)
 time.sleep(5)
 driver.quit()
 return(g) 
 print('Data Capture sucessfully')

 

i=0
while(True):
    ret, frame = cap.read()
    cv2.imwrite(r'C:\Users\Yousuf Traders\Desktop\sample.jpg',frame)
    d_classifier(r"C:\Users\Yousuf Traders\Desktop\sample.jpg")
    break

    #i=i+1
    #if cv2.waitKey(1) & 0xFF == ord('q') & i==2:
    #    break
