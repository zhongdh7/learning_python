#B 
#A
#B
#B
#C
import pyautogui as pag
import time 
from pyperclip import copy


copy("https://pvp.qq.com/")
pag.hotkey("win","s")
time.sleep(0.5)
pag.hotkey("ctrl",'v')
pag.press('enter')
time.sleep(1.5)
pag.moveTo(837,175,duration=1)
pag.moveRel(0,150,duration=1)
pag.click()
time.sleep(1.5)
pag.scroll(-500)
pag.click(1037,704,duration=1)
pag.click(546,1310,duration=1)
pag.moveTo(477,570,duration=1)
pag.dragRel(2181-477,1469-570,duration=0.5)

pag.hotkey("ctrl",'c')

pag.click(2141,350,duration=0.5)

pag.hotkey("win","s")
pag.write("word")
time.sleep(0.5)
pag.press("enter")

time.sleep(6)
pag.click(399,317,duration=0.5)
pag.hotkey("ctrl","v")
time.sleep(2)
pag.hotkey("ctrl","s")
pag.click(1049,948,duration=1)
time.sleep(2)
pag.click(494,810,duration=1)

copy("E:\自学编程\python\\005")
time.sleep(2)
pag.click(813,80,duration=1)
pag.hotkey("ctrl",'v')
pag.press('enter')
time.sleep(1.5)
pag.doubleClick(1002,771,duration=1)
time.sleep(1)
pag.hotkey("ctrl","s")
pag.click(2537,30,duration=0.5)