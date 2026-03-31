#基础使用
#我的电脑显示配置是2560*1600
#最左上角的坐标是(0,0)
#最右下角的坐标是(2559,1599)

#获取当前鼠标的位置
import pyautogui

# pos=pyautogui.position()
# print(pos)
# print(type(pos))


# # 手动定位鼠标坐标的程序
# for i in range(10):
#     input("请将你的鼠标移动到指定的位置，然后按下回车键")
#     pos=pyautogui.position()
#     print(pos)

"""
    移动鼠标:
        1.相对移动，相对当前的位置移动
        2.绝对移动，就是移动到指定的坐标位置
    拖拽鼠标:(左键按住不懂得移动方法)
        1.dragTo()绝对移动
        2.相对移动
    鼠标点击:
        单击左键
        双击左键
        单机右键
    鼠标的滚动：
        上下滚动
        左右滚动
"""

#绝对移动 moveTo()
# pyautogui.moveTo(1,1,duration=2)#前面的是指把鼠标移动到的坐标，duration是指完成移动的时间
# from pyautogui import moveTo
# moveTo(2528,199,duration=0)#不能从边角开始移动，边角都是检测不到的，边角无法控制

#相对移动moveRel
# from pyautogui import moveRel
# moveRel(400,0,duration=1)#相对当前的位置移动的位置
# moveRel(0,500,duration=1)#向下为y轴+，向右为x轴+
# moveRel(-400,0,duration=1)


#绝对拖拽dragTo
# from pyautogui import dragTo
# dragTo(100,100,duration=2)

#相对拖拽dragRel
# pyautogui.dragRel(200,100,duration=1)

#单击左键click()
#可以传入指定的坐标，也可以不写就是点击当前位置
import time
# time.sleep(2)
# pos=pyautogui.position()
# print(pos)
# pyautogui.click(pos)

#双击左键doubleClick()
# time.sleep(5)
# pyautogui.doubleClick(140,222)
# pyautogui.doubleClick(171,349)

#右键rightClick()
# time.sleep(2)
# pyautogui.rightClick(pos,duration=2)

#电子木鱼自动敲击
# for i in range(100):
#     pyautogui.doubleClick(657,980)

#上下滚动
# pyautogui.scroll(1000)#这里正数是向上滚动
# pyautogui.scroll(-1000)


#水平滚动
# time.sleep(1)
# pyautogui.hscroll(100)

"""
    键盘操作：
        按下一个键 press('win')按下win键
        按下多个键
        键盘输入内容
"""

#按下单个键
# pyautogui.press('win')
# pyautogui.press('A')


#按下多个键
# pyautogui.hotkey('win','r')#同时按下win和r
# pyautogui.hotkey('alt','A')
# pyautogui.hotkey('ctrl','a')
# pyautogui.hotkey('ctrl','c')
# pyautogui.click(duration=1)
# pyautogui.hotkey('ctrl','v')
# time.sleep(1)
# pyautogui.hotkey('ctrl','z')

#键盘输入内容
#write()#不支持中文
# pyautogui.write("you are handsome")
#在光标的位置直接键盘输入括号里面的内容

#输入中文
#pip install pyperclip -i https://mirrors.aliyun.com/pypi/simple/
# import pyperclip
# pyperclip.copy("好帅")#这个是自动把括号里面的内容复制到剪贴板里面，然后用ctrl+v就可以直接复制






