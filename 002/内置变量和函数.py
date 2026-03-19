#内置的变量
#__file__:表示获取当前文件的路径
print(__file__)
#内置函数：
#print()函数：用于输出内容到控制台，可以输出字符串、数字、变量等各种类型的数据
print("Hello, World!")
#变量的调用
#列表.append()方法：用于在列表末尾添加一个元素
#字符串.join()方法：用于将一个可迭代对象中的元素连接成一个字符串，元素之间使用指定的分隔符进行分隔
#字符串.split()方法：用于将一个字符串按照指定的分隔符进行分割，返回一个列表
#模块调用：
#random.sample()函数：用于从一个序列中随机抽取指定数量的元素，返回一个列表
#time.time()函数：用于获取当前时间的时间戳，返回一个浮点数，表示从1970年1月1日00:00:00 UTC到当前时间的秒数

#列表
a=[1,2,3,4]
a.append(5)
print(a)
a.append([90,90,2,"what"])
print(a)
a.append("hello world")
print(a)

#join()方法
a=["hello","world","python"]
b=' '.join(a)
#这里的' '表示使用空格作为分隔符，将列表中的元素连接成一个字符串
print(b)
b=','.join(a)
print(b)
b='--'.join(a)
print(b)
#但是这个操作不会改变原来的列表a，a仍然是一个列表
print(a)

#split()方法
a="hello world python"
b=a.split(' ')
#这里的' '表示使用空格作为分隔符，将字符串a按照空格
#进行分割，返回一个列表
print(b)
b=a.split(',')
print(b)
#这里的','表示使用逗号作为分隔符，但是字符串a中没有,所以返回一个包含整个字符串a的列表
a="hello=world=python"
b=a.split('=')
print(b)
a="wo====rld=python"
b=a.split('=')
print(b)#这里的'='表示使用等号作为分隔符，如果遇到连续的分隔符，会将除了第一个之后的连续分隔符每个都作为一个分隔符进行分割，所以返回的列表中会有空字符串
a="?id=33334444"
b=a.split('=')
print(b)
print(b[1])

#模块调用
#random.sample()函数
#使用之前需要导入random模块
import random
a=[1,2,3,4,5,6,7,8,9,10]
#随机抽取指定数量的元素，返回一个列表
b=random.sample(a,3)
print(b)
print(type(b))
