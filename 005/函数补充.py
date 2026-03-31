"""
    带return的无参函数
    带return的有参函数

    计算器：计算几个值的和、积、差、商
"""

#带return的无参函数
def add():
    return 3+4
print(add())
def return_list():
    return [1,2,3,4,5]
print(return_list())
print(type(return_list()))

#带return的有参函数
def add(a,b):
    return a+b
print(add(3,4))
def lis(a,b,c):
    return [a,b,c]
list1=lis(1,2,3)
print(list1)
#没有return的函数默认返回None
def add(a,b=9):
    a+b
num=add(a=2)
print(num)
def is_num(a):
    """
    判断一个数是否为偶数
    传入的参数是一个数，如果这个数是偶数，返回True，否则返回False
    """
    return a%2==0
    print("这个函数的功能是判断一个数是否为偶数")#这个print语句永远不会被执行，因为它在return语句之后，函数一旦执行到return语句就会结束，不会继续执行后面的代码

print(is_num(3))
print(is_num(4))

#try-except语句可以用来捕获函数中的异常，如果函数中发生了异常，程序不会崩溃，而是会执行except块中的代码
#错误是语法错误
#异常是运行时错误，比如除以零、访问不存在的变量等
#没有语法错误但是报错了就是异常

"""
    捕获异常的函数
    try:
        可能会发生异常的代码  
    except:
        处理异常的代码
"""
try:
    print(1+"1")
except:
    print("发生了异常，无法将整数和字符串相加")
print(1)
def is_num(a):
    try:
        return int(a)%2==0
    except:
        print("发生了异常，无法判断这个数是否为偶数")
        return None
number=input("请输入一个数：")
print(is_num(number))