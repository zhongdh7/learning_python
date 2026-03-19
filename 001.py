print("name: 001.py")
print("description: This is a simple Python script that prints its name and description.")
print(90.3940)
a=130.8
print(type(a))
a=True
print(type(a))
print(a)
#组合数据类型
#str表示字符串
#list表示列表
#tuple表示元组
#dict表示字典

#str 字符串
a="hello world"
print(a)
print(type(a))
a='hello world'
print(a)
print(type(a))
a="你好"
print(a)
print(type(a))
a="我的名字是\"小明\""
print(a)
a='我的名字是"小明"'
print(a)
print(type(a))
# name=input("请输入你的名字：")#input函数可以获取用户输入的内容，默认以字符串的形式返回
# print("你的名字是："+name)
# age=int(input("请输入你的年龄："))#将输入的字符串转换为整数
# print("你的年龄是："+str(age))#将整数转换为字符串进行拼接
#list 列表
info=["小明",18,"男","北京",1.889,True]#列表可以存储不同类型的数据，列表中的元素可以通过索引访问，索引从0开始，负数索引表示从后往前数
#     0    1   2   3     4      5
#     -6   -5  -4  -3    -2     -1
print(info)
print(info[3])
print(info[-1])
print(type(info))
print(info[-2])

#字符串也可以一个一个访问
a="hello world"
print(a[0])
print(a[-1])
a="你好"
print(a[0])
print(a[-1])

#dict 字典
info={"name":"小明","age":18,"gender":"男","city":"北京","height":1.889,"is_student":True}#字典是由键值对组成的，键必须是不可变类型，值可以是任意类型，字典中的元素可以通过键访问
print(info)
print(info["name"])
print(info["age"])
print(info["gender"])
print(info["city"])
print(info["height"])
print(info["is_student"])
#键不能重复，如果有重复的键，后面的值会覆盖前面的值
info={"name":"小明","age":18,"name":"小红"}
print(info)
info={"name":[[[[[[[[[[[[[[[[[[[[[[[1,2]]]]]]]]]]]]]]]]]]]]]]]}
print(info)
#打印info字典中的name键对应的值
print(info["name"])
a={101:'张三',102:'李四',103:'王五'}
a[101]='赵六'#修改字典中键为101的值
print(a)
a[104]='钱七'#向字典中添加键为104，值为钱七的键值对
print(a)

for key in a:#遍历字典中的键
    print(key)
for value in a.values():#遍历字典中的值
    print(value)
for key,value in a.items():#遍历字典中的键值对
    print(key,value)