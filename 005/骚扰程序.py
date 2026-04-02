import pyautogui as pag
from pyperclip import copy
import random
import time

pag.hotkey("win","d")
time.sleep(0.5)
pag.doubleClick(195,215,duration=1)
time.sleep(1)
pag.click(828,335,duration=1)
copy("杜俊杰")
pag.hotkey("ctrl",'v')
time.sleep(1)

pag.press("enter")
pag.click(1391,1031,duration=0.8)
str_list=["杜俊杰天天导管","杜俊杰我爱你","杜俊杰天天不起床","杜俊杰好丑","杜俊杰我爱你100年"]
for i in range(10):
    temp_str=random.sample(str_list,1)
    copy(temp_str[0])
    pag.hotkey("ctrl","v")
    time.sleep(1)
    pag.press("enter")
    time.sleep(2)
    