print(__file__)

def show():
    for i in range(1,8,2):
        print(i)
    print("we did it")

show()

#函数的使用
#定义函数的规则
#1.函数的定义以def开头，后面跟上函数的名字，最后是括号和冒号
#2.函数的名字可以由字母、数字和下划线组成，但不能以数字开头
#3.函数的括号中可以有参数，也可以没有参数，如果有参数，参数之间用逗号分隔
#4.函数的代码块以冒号开头，缩进的方式表示函数的代码块

print("let's to see what the show function is")
show()

"""
    函数类型都有哪些：
        1.无参函数：没有参数的函数,这个函数不需要传入任何参数就可以执行
        2.有参函数：有参数的函数，这个函数需要传入参数才能执行
"""
def robot_v1():
    print("hello, I am a robot_v1")


#这里的参数是一个形式参数必须传入参数才能执行这个函数，参数的名字可以随便起，但是要有意义，能够表达这个参数的作用
def robot_v2(drink):#这里的参数就是一个变量的名字
    print("hello, I am a robot_v2")
    print(f"I can help you to get a {drink}")

robot_v1()
robot_v2("coke")#这里的参数就是一个具体的值，叫做实参
#需要传入参数的函数必须要传入一个参数才能执行，如果不传入参数或者传入的参数个数不对，就会报错
robot_v2("牛奶")

#默认参数
def robot_v3(drink="water"):
    print("I have already get the command:",drink)
    print("I can help you get the",drink)

#这个时候就可以不用传入参数使用了
robot_v3()
#如果在有默认值的情况下还传入值则覆盖默认值
robot_v3("霸王茶姬")

#可以设定多个传入值
#指定位置传参数
def robot_v4(drink="茶",sugar=5):
    if(sugar==0):
        print(f"您需要的是无糖的{drink}")
    elif(sugar):
        print(f"目前您需要的是{drink}，其中糖分是{sugar}分糖")
robot_v4()

#默认位置传入参数
robot_v4("冰红茶",0)

#指定位置传入参数
robot_v4(sugar=0,drink="coke")
