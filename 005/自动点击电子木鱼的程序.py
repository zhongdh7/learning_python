import pyautogui as pag

import time
import pyperclip

pyperclip.copy("https://www.lddgo.net/common/wooden-fish")
pag.hotkey("win",'s')
time.sleep(0.2)
pag.hotkey("ctrl",'v')
time.sleep(0.2)
pag.press('enter')
time.sleep(0.2)
for i in range(100):
    pag.doubleClick(1307,978)

pag.click(2390,41)