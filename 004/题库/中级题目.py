#成绩判断题目
grade=int(input("请输入你的成绩："))
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
else:
    print("F")

#闰年判断
def is_run(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    return False
year=int(input("请输入一个月份"))
if is_run(year):
    print("是闰年")
else:
    print("不是闰年")