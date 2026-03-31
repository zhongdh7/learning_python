print(__file__)
a="what can i say"
b=a.split(' ')
if type(b)==type([1,2,3]):
    print(b)
    print(b[-1])
else:
    print(type(b))
print(a)
a='--'.join(b)
print(b)
b.append("hello")
print(b)
b.append(90)
b.append({"name":"小明","age":18})
b.append(90.29)
print(b)
print("------------------")
import random
a=random.sample(b,1)#永远返回的是一个数组
if type(a[0])==type([1,2,3]):
    print(a)
    print(a[0])
elif type(a[0])==type("hello"):
    print(a)
    print("this is a string")
elif type(a[0])==type(dict()):
    print(a)
    print("this is a dict")
else:
    print(a)
    print(type(a[0]))

a=[i for i in range(10)]
p=random.sample(a,3)
print(p)
s="what can i say"
b=s.split(' ')
print(b)
b=' '.join(b)
print(b)

b=random.sample(s,2)
print(b)

a={"name":"小明","age":18,"gender":"男","city":"北京","height":1.889,"is_student":True}
b=random.sample(list(a.items()),3)
print(b)
print(type(b[0]))

# a=input() 这里input函数输入的任何内容都会被当做字符串处理，所以无论输入什么，a的类型都是str
# print(type(a))

strs="123.90"
# print(int(strs))#这里会报错，因为字符串的内容是一个浮点数形式的字符串，不能直接转换为整数
print(int(float(strs)))#如果要将一个浮点数形式的字符串转换为整数，那么需要先将其转换为浮点数，再将浮点数转换为整数
str1="what can i say"
str1+="what"
print(str1)
dicts={"name":"小明","age":18}
dicts["id"]=1001
print(dicts)
import numpy
print(numpy.__version__)  # 应显示 1.x，如 1.26.4