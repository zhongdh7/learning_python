import pyautogui as pag
import time
from pyperclip import copy

pag.hotkey("win","d")
pag.doubleClick(177,195,duration=1)
pag.click(1023,236,duration=1)
copy("杜俊杰")
time.sleep(1)
pag.hotkey("ctrl","v")
time.sleep(1)
pag.press("enter")
pag.click(1329,1023,duration=1)
for i in range(1000):
    copy(f"杜俊杰起床了！！！\n你已经睡了{i}秒了")
    pag.hotkey("ctrl","v")
    time.sleep(0.1)
    pag.press("enter")
