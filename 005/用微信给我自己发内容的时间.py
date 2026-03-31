import pyautogui as pag
import time
import pyperclip

pyperclip.copy("这个是自动发给你的一个内容")

pag.doubleClick(180,213,duration=1)
pag.doubleClick(880,623,duration=1)
pag.click(498,1278,duration=1)
pag.hotkey('ctrl','v')
pag.press('enter')
pag.click(1212,474,duration=1)