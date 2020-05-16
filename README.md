# Dclassifier (Reverse Image Search Based Object Recognition)
A Reverse Image Search Based Object Recognition Tool

D-Classifier is a tool for recognizing objects using "Reverse Image Search by Google Combined with Segmentation Algorithm and 
Selenium automation tool"

This is basically a "An object recognizer with the help of Reverse Image Search",D-classifier takes pictures from your
webcam ,chops its up into multiple segments depending on your window size and step size you have set then it uses
Selenium Web browser automation tool to send these chopped image to google image search ,
Then results from google are extracted using selenium tools (Actually the links are extracted )from that google page,
These links (URLS) contains information about the item searched ,so these links are analyzed and meaningful data 
is extracted which tells us about the thing that the webcam saw-By this way we could recognize different objects with the
help of this!

System/Setup Requirements: 
You should have the following libraries on your system cv2 numpy PIL selenium webdriver for Chrome/Firefox 
re 
pyautogui
Selenium

---------
