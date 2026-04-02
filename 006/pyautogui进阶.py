"""
    消息框-1：
        警告框：
            pag.alert来使用警告框

        选择框：
"""
import pyautogui as pag
import time
import random



#-------------------------------------------
#警告框
# pag.alert(text="警告信息",title="标题",button="按钮文本")
# #text对应文本,title警告框的标题,button展示按钮的文本
# pag.alert(text="你想不想学好？",title="拷打是否学习",button="of course")
# #参数不是一定要写
# pag.alert()

#警告框只有一个按钮


#-------------------------------------------
#选择框
#多个按钮
# pag.confirm(text="提示信息",title="标题",buttons=["按钮1","按钮2","按钮3"])
#这里buttons传入一个列表



#-------------------------------------------
#输入框 prompt
# pag.prompt(text="提示信息",title="标题",default="默认的输入的文字")


#-------------------------------------------
#密码框 password
# pag.password(text="信息",title="标题",default="默认",mask="*")#mask参数是指敲什么数据用什么字符来掩盖



#小案例

#1.欢迎的弹窗提示+规则说明
wether_begin=pag.alert(text="欢迎来到猜数字游戏\n规则是：猜1-100的数字，最多猜10次",
                       title="猜数字小游戏",
                       button="开始游戏")
#不是专业的弹窗做不了这个

#直接下一步

answer=random.randint(1,100)

guess=pag.prompt(text="请输入你猜测的数字,这是你第1次猜",title="猜数字游戏",default="在这里输入数字")

#给到十次机会开始
for i in range(9):
    #获取用户的输入

    #验证一下输入的有效性
    try:
        guess=int(guess)

        #判断一下输入的数字对不对
        if guess==answer:
            pag.alert(text="猜对了",title="猜数字游戏")
            break
        elif guess>answer:
            guess=pag.prompt(text=f"猜大了,这是你的第{i+2}",title="猜数字游戏",default="在这里输入数字")
        else:
            guess=pag.prompt(text=f"猜小了,这是你的第{i+2}",title="猜数字游戏",default="在这里输入数字")

    except:
        pag.prompt(text=f"请输入1-100的整数，第{i+2}次",title="类型错误",default="请输入整数")

if guess!=answer:
    pag.confirm(text=f"机会都用完了，正确答案是{answer}",title="猜数字游戏",buttons=["确定","取消"])
