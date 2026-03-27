#B
#这里不清楚题目描述的情况下有没有缩进，如果没有缩进就是无数次，否则为B一次
#A D
#C
def v1():
    print("this is the first version")
v1()

def v2(ability):
    print("this is the second version")
    print("and i can do",ability)

v2("sleep")

def v3(ability=None):
    print("this is the second version")
    if not ability:
        print("But I can do nothing")
    else:
        print(f"and i can do {ability}")

v3()
v3("drink the water")

def v4(version,ability):
    print(f"this is the {version} version")
    print("and i can do",ability)

v4(4,"wash my hand")
v4(ability="wash my hand",version=4)