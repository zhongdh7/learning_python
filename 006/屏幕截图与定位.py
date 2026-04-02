import pyautogui as pag

#pyautogui也可以截屏

#screenshot 截了屏幕之后不传入后面的字符串保存位置得话就没有任何的效果
#需要传入保存图片的路径
#图片后缀 jpg png 

#绝对路径保存
# pag.screenshot("E:\\自学编程\\python\\006\\绝对路径测试.jpg")#斜杠\的时候打出必须要用转义字符

#避免\无法被识别可以在前面加一个r
# pag.screenshot(r"E:\自学编程\python\006\r的测试.jpg")

#相对路径
# pag.screenshot("相对路径.jpg")#默认保存到当前打开的目录下面

#pag.screenshot是截取全屏幕


#增加区域部分的参数
#坐标分别传入左上角的xy和宽和高的参数
# pag.screenshot(r"E:\自学编程\python\006\区域截图.jpg",region=(622,71,431,122))
# a=(1,2,3,4,5,6,3,3,3,3,3)#元组不能够修改值
# print(type(a))
# print(pag.size())
# pag.screenshot(r"E:\自学编程\python\006\获取左半边屏幕截图.jpg",region=(0,0,1280,1599))


#定位
