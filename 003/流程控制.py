#in,not in检查某个元素是否在某个容器中
a=[1,2,3,4,5]
dicts={"name":"zdh","age":19,"height":182.1,"school":"中山大学"}
strs="12345678910"
print(1 in a)
print(6 in a)
print("name" in dicts)
print("zdh" in dicts)
print("zdh" in dicts.values())
print("zdh" not in dicts.values())
print("a" in "abcd")#字符串也是一个容器，可以用in检查某个字符是否在字符串中

#只要在容器中有一个元素满足条件就返回True
print(1 in a or 6 in a)
print("name" not in dicts)#这里直接用键来检查是否在字典中，默认检查的是键
print(("name","zdh") in dicts.items())#items()方法可以把字典转换为一个由键值对组成的列表，每个键值对是一个元组