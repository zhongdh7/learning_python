print("Hello, World!")
#作业评讲
lst=["帅哥",9,[1,2,3],{"name":90,90:"帅哥"},90.90]
print(lst[0])
print(lst[2][1])
print(type(lst[3]))
print(lst[3]["name"])
print(lst[-1])
#数值运算
#+ - * / 
#python中特有的 
#// 取整除，返回商的整数部分
#** 幂运算，返回x的y次幂
#% 取模，返回x除以y的余数
a=10
b=3
print(a+b)
b='s'
# print(a+b)#会报错，不能将整数和字符串相加
b=9.1
print(a+b)
b='3'
print(a+int(b))#将字符串转换为整数进行相加,但是这里字符串的转换必须是数字字符串，否则会报错
b="101.2"
# print(a+int(b))#如果要强转字符串编程整数那么字符串必须是整数形式的，否则会报错
b=101.33
a=10
print(a+int(b))#强转为整数会舍弃小数部分,只会保留整数部分

a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)#这里是计算出来的商的结果是一个浮点数，不像C语言中如果两个整数相除结果还是整数

print(a//b)#取整除，返回商的整数部分，这个就是C语言中整数相除的结果
print(a**b)#幂运算，返回a的b次幂
print(a%b)#取模，返回a除以b的余数

#赋值运算
a=10
a+=5#相当于a=a+5
print(a)
a-=3#相当于a=a-3
print(a)
a=10
a*=2#相当于a=a*2
print(a)
print(float(a))#将整数转换为浮点数

#注意在使用除法的时候所有的数据类型都会被转换为浮点数，所以结果是一个浮点数
a/=2#相当于a=a/2
print(a)#都会输出一个浮点数
a=10
print(float(a))#将整数转换为浮点数
a**=2#相当于a=a**2
print(a)

#比较运算
bool1=True
bool2=False
print(bool1)
bool1=1
print(bool(bool1))#在python中，0和空字符串、空列表、空字典、空元组等都被认为是False，其他的值都被认为是True
a=10
b=5
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)


print("下面是逻辑运算：")
#and or not
#并且 或者和非
bool1=True
bool2=False
print(bool1 and bool2)#并且，只有当两个条件都为True时，结果才为True，否则为False
print(bool1 or bool2)#或者，只有当两个条件都为False时，结果才为False，否则为True
print(not bool1)#非，取反，如果bool1为True，则结果为False，如果bool1为False，则结果为True

