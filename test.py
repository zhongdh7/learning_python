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