a=10
b=20
print(a)

c=a+b
print(c)

#分支结构允许程序根据不同的条件执行不同的代码块，常见的分支结构有if语句和if-else语句
height=180
if height>=185:
    print("你很高")
else :
    print("你不高")

man="帅哥"
if man=="美女":
    print("你是美女")
else:
    print("你不是美女")
#多分支判断

age=18
if age>60:
    print("你是老年人")
elif age>18 and age<=60:
    print("你是成年人")
elif age>14 and age<=18:
    print("你是青少年")
#中间的elif语句可以有任意多个，最后的else语句是可选的，如果没有else语句，那么当所有的条件都不满足时，程序就不会执行任何代码块
else:
    print("你是儿童")
print(__file__)