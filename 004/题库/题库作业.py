#变量赋值
name="Alice"
age=30
is_student=False

#列表操作
fruits=["apple","banana","cherry"]
print(fruits[1])
fruits.append("date")
print(fruits)

#简单的if语句
score=85
if score>=60:
    print("Pass")
temperature=20
if temperature>25:
    print("Hot")
else:
    print("Cool")

grade='B'
if grade=='A':
    print("Excellent")
elif grade=="B":
    print("Good")
else:
    print("Needs Improvement")

age=22
if age>18 and age<30:
    print("Young Adult")
else:
    print("Other Age Group")

#算数运算
a=10
b=5
print(a+b,a-b,a*b,a/b)

#比较运算
a=10
b=20
print(a<b)
print(a==b)
print(a>b)
x=True
y=False
print(x and y, x or y,not x)

#判断成绩等级
score=88
if score>=90:
    print("A")
elif score>=80 and score<=89:
    print("B")
elif score>=70 and score<=79:
    print("C")
elif score>=60 and score<=69:
    print("D")
else:
    print("F")


#计算折扣
price=100
discount_rate=0.1
if price>10:
    result=price*discount_rate
else:
    result=price
print(result)


#循环题目
for i in range(2,101,2):
    print(i)

temp=0
for i in range(1,100,2):
    temp+=i
print(temp)

i=1
while i<=10:
    print(i)
    i+=1


#自定义函数题目
def add(a,b):
    return a+b

from math import sqrt
def is_prime(n):
    """
        这个函数是用来判断n是不是一个质数的，传入一个整数返回bool值
    """
    if n==2 or n==1:
        return True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

for i in range(1,101):
    print(f"{i}是不是质数？{is_prime(i)}")

#从一个列表当中随机选取三个不重复的元素
list1=[1,"name",90.2,"5%",["what",True],9,8,{"name":"zz","age":89,7:"id"},9,10]

import random
rd=random.sample(list1,3)
print(rd)

#创建两个不同有不同元素的列表
list1=list()#这样初始化的是一个空列表
for i in range(1,1001):
    list1.append(i)

list2=list()
for i in range(1,10001):
    list2.append(i)

import time
begin=time.time()
for i in list1:
    p=None
end=time.time()
print("遍历1000个数据需要的时间是:",end-begin)
begin=time.time()
for i in list2:
    p=None
end=time.time()
print("遍历10000个数据所需要的时间是:",end-begin)

#创建一个含有多个字符串的列表
str_list=["hello","world","i","really","like","you"]
str1='\n'.join(str_list)
print(str1)


