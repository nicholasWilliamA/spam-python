import pyautogui
import time
import os
import keyboard

time.sleep(4)
# bot to have input from notepad
ctr = 0
os.chdir("/Users/Nicholas/Documents/Kuliah/Latihan")
f = open("testdata.txt", "r")
while f:
    ctr+=1
    line = f.readline()
    pyautogui.typewrite(line)
    if line == "":
        break
    if keyboard.is_pressed('q') == True:
        print ("key is pressed")
        break
    time.sleep(1)
f.close()

# bot to immediately run or change the message
for i in range (3): 
    pyautogui.typewrite("test\n")
    time.sleep(1)


