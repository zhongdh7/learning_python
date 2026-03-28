#简单条件判断
num=int(input("请输入一个整数："))
if num>0:
    print("是正数")
elif num==0:
    print("是0")
else:
    print("是负数")

#奇偶判断
num=int(input("请输入一个整数："))
if num%2:
    print("是奇数")
else:
    print("是偶数")

#你年龄判断
age=int(input("请输入你的年龄："))
if age>=18:
    print("你已经成年了")
else:
    print("你还未成年")