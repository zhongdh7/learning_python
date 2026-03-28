#复杂逻辑判断
def is_run(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    return False

def first():
    year=int(input("请输入一个年份"))
    month_dict={
        "January":31,
        "February":None,
        "March":31,
        "April":30,
        "May":31,
        "June":30,
        "July":31,
        "August":31,
        "September":30,
        "October":31,
        "November":30,
        "December":31
    }
    month=input("请输入一个月份")
    if month=="Feburary":
        if is_run(year):
            month_dict[month]=29
        else:
            month_dict[month]=28
    print(f"第{year}年的{month}有{month_dict[month]}天")

# first()


#多条件组合判断
def second():
    str1=input("请输入一个字符串")
    flag={"flag1":False,"flag2":False,"flag3":False}
    dict1=["1234567890","abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    if len(str1)>=6 and len(str1)<=12:
        for i in str1:
            if not i in dict1[0] and not i in dict1[1] and not i in dict1[2]:
                return False
            
            if i in dict1[0] and not flag["flag1"]:
                flag["flag1"]=True
            if i in dict1[1] and not flag["flag2"]:
                flag["flag2"]=True
            if i in dict1[2] and not flag["flag3"]:
                flag["flag3"]=True
            if flag["flag1"] and flag["flag2"] and flag["flag3"]:
                return True
    else:
        return False
    if flag["flag1"] and flag["flag2"] and flag["flag3"]:
        return True
    else: 
        return False

               
# print(second())


#复杂逻辑嵌套
def third():
    time=input("请输入一个时间用:分隔开小时，分钟，秒:")
    time=time.split(":")
    t=0
    for i in time:
        time[t]=int(i)
        t+=1
    flag=False
    if time[0]<=24 and time[0]>=0 and time[1]<=60 and time[1]>=0 and time[2]>=0 and time[2]<=60:
        flag=True
    if flag:
        print("合法")
        if time[0]<12:
            print("上午")
        elif time[0]<18:
            print("下午")
        else:
            print("晚上")
    else:
        print("非合法")

third()