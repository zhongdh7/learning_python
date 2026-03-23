import time

#获取当前的时间
#从1970年1月1日0点0分0秒到现在的秒数
print(time.time())#让程序暂停的时间
d=time.time()#这个叫做时间戳，时间戳就是指1970年1月1日0点0分0秒到现在的秒数，是一个浮点数，整数部分是秒数，小数部分是毫秒数
print(d)
print(time.ctime(d))#将时间戳转换为可读的时间格式
print(type(d))

#time.sleep(3)#括号里面是秒数，程序会暂停3秒钟
time.sleep(2)
print("程序继续执行")