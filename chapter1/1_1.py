#多对多 赋值
mounth = ["jan","Feb","Mar"]
yue1 ,yue2,yue3 = mounth
print( yue1,yue2,yue3)

#可迭代对象 一对多赋值
name = "apple"
ch1,ch2,ch3,ch4,ch5 = name

print(ch1,ch2,ch3)

#对于  可丢弃 一般 用 _ 赋值


data = ["error",12,12,"error"]
_,num1,num2,_ = data
print( num1,num2)