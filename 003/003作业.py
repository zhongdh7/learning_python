#C
#D
#B
#B

"""
    打字小游戏：
        1.输入命令开始游戏
        2.程序生成随机的字符
        3.显示随机字符，接收用户的输入
        4.判断用户输入的字符是否正确
"""
import random#导入random模块,用于随机生成字符串
import time
print("========================")
print("欢迎来到打字小游戏！")
print("========================")
# strs=input("请输入“开始游戏”来开启游戏：")
strs="开始游戏"
if strs=="开始游戏":
    print("========================")
    print("游戏开始！")
    print("========================")
else:
    print("输入错误，游戏结束！")
    print("========================")
    exit()

num=random.sample("khkahsuidhkjsjknmzmn+aKJDKLKKJ829LJ9012K",15)#这里的一个参数可以传入一个链表，可遍历的数据或者直接一个数据都可以

num=''.join(num)
print("请打出以下字符：")
print(num)
#用time模块来做计时操作
begin=time.time()
user_str=input("请开始输入结果：")
end=time.time()#这个函数是直接返回运行到这里的时候到1970年1月1日0:0:0:0的时候的时间
if user_str==num:
    print("结果正确")
    print(f"一共用了{end-begin}s哟！")
    print("一共用时了",-begin+end)#可以直接使用,号来拼接后面的数据
    print("一共用时",round(end-begin,2))#用这个函数可以保证保留指定位数的小数
else:
    print("不正确哟")
