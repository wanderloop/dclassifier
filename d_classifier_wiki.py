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
 time.sleep(20) #20 yeh tum khud apney mutabiq set karlo dodno mein
 driver.find_element_by_class_name("mks_button.mks_button_medium").click()
 time.sleep(10) #10
 
 driver.switch_to.window(driver.window_handles[1])
 driver.get(driver.current_url)
 
 continue_link = driver.find_element_by_tag_name('a')
 #elems = driver.find_elements_by_xpath("//a[@href]")
 elem = driver.find_elements_by_xpath("//*[@href]")
 elems = driver.find_elements_by_xpath("//a[@href]")
 f='.*?'
 for elem in elems:
  k=elem.get_attribute("href")
  p='\''+k+'\''
  findLinks=re.findall('https://en.wikipedia.org/wiki/'+f+'&',p)
  for eachthing in findLinks:
          
     i=eachthing.replace('https://en.wikipedia.org/wiki/', '')
     print(i)
     findLinks=re.findall('https://www.amazon.co.uk/'+f+'/',p)
  for eachthing in findLinks:
     i=eachthing.replace('https://www.amazon.co.uk/','')
     print(i)
 driver.quit()
i=0
while(True):
    ret, frame = cap.read()
    cv2.imwrite(r'C:\Users\Yousuf Traders\Desktop\sample.jpg',frame)
    d_classifier(r"C:\Users\Yousuf Traders\Desktop\sample.jpg")
    break
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
