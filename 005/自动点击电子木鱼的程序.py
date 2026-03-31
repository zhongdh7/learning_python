import pyautogui as pag

import time
import pyperclip

pyperclip.copy("https://www.lddgo.net/common/wooden-fish")
pag.click(1689,1578,duration=1)
pag.click(1521,90,duration=0.5)
pag.hotkey("ctrl",'v')
pag.press('enter')
for i in range(100):
    pag.doubleClick(1307,978)

pag.click(2390,41)