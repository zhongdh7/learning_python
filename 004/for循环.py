#range 类型
#for循环的语法
#for 变量 in 可迭代对象:
"""
    for循环:
    1.可迭代对象:字符串、列表、元组、字典、集合等
    2.变量:用来接收可迭代对象中的每一个元素
    3.循环体:用来处理每一个元素的代码块
"""

#range()函数可以生成一个整数序列，常用来生成一个指定范围的整数序列
#range(start,stop,step) start:起始值，默认是0；stop:结束值，不包含；step:步长，默认是1
for i in range(1,10,2):#这个函数生成的整数序列是从1开始到10结束，步长是2，即1,3,5,7,9
    print(i)
for i in range(10):#这个函数生成的整数序列是从0开始到10结束，步长是1，即0,1,2,3,4,5,6,7,8,9
    print(f"循环第{i}次")


for i in range(1,10,1):#左闭右开区间，和切片比较类似
    print(i)
a=[1,2,3,4,5,6,7,8,9,10]
print(a[:9:1])
print(a[-1::-1])#切片倒序遍历

for i in range(1,10,2):
    print(i)

for i in range(1,10):
    print(i)
    #这里不加最后的步长，默认是1
for i in range(10):
    print(i)
for i in range(101):
    print(i)
#打印1到100的所有奇数
for i in range(1,100,2):
    print(i)

#打印10-1
for i in range(10,0,-1):
    print(i)

#continue和break
#continue:跳过当前循环的剩余代码，直接进入下一次循环
for i in range(1,10):
    if i==5:
        print("第五次不打印")
        continue#加上关键字之后第五次的时候不会再执行后面的程序
    print(i)
#break
for i in range(10):
    if i==4:
        print("stop")
        break
    print(i)



#对于可遍历的数据类型可以直接全部遍历
student=["first","second","third","fourth","fifth"]

for i in student:
    print(i)

for i in "what can i say":
    print(i)#字典也可以遍历

#字典遍历的是键
print("下面是字典的遍历")
data={
    "name":"zdh",
    "id":"25307227",
    "age":18,
    "sex":"male",
}

for i in data:
    print(f"{i}: {data[i]}")