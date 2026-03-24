#拼接输出
name="zdh"
age=19
height=182.1

#1.用逗号拼接多个参数输出用逗号分隔
#变量和字符之间右空格这个方法输出
print("姓名:",name,"年龄:",age,"高度:",round(height),"cm")#round默认输出没有小数位，为四舍五入


#2.连字符+拼接
#可以解决上面的空格问题
#只能再字符串之间使用
print("姓名:"+name+"年龄:"+str(age)+"高度:"+str(height)+"cm")#str()强转为字符串
#int()强制转化为int数据类型

#f大括号连接
print(f"姓名:{name} 年龄:{age} 高度:{height} cm")