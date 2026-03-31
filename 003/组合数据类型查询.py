tuples=(1,2,3,4,5,6,7,8,9,10)
lists=[1,2,3,4,5,6,7,8,9,10]
strs="12345678910"
dicts={"name":"zdh","age":19,"height":182.1,"school":"中山大学"}
#len函数可以查询数据类型的长度
print(len(strs))
print(len("你好"))

#求和只能求数值类型的和
print(sum(lists))
print(sum(tuples))

#最大值最小值
print(max(lists))
print(min(tuples))
# print(max(dicts.values()))#求字典的最大值最小值只能求字典的值的最大值最小值，不能求字典的键的最大值最小值


