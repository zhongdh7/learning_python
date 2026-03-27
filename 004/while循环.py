#while循环是按照条件循环的
i=0
while i<=9:
    print(i)
    i+=1

#random模块随机产生数字
import random#random.randint 在数据范围内随机生成一个整数
secret=random.randint(1,100)#这个数据范围是左闭右闭区间，即1和100都包含在内
guess=None
while guess!=secret:
    guess=int(input("输入一个整数"))
    if guess>secret:
        print("大了")
    else:
        print("小了")
print("猜对了！")
for i in range(10):
    guess=random.randint(1,90)
    print(guess)