#解压 可迭代数 大于变量数
import  math
#成绩平均分 ，去掉 第一，最后一科目
def score(grades):
    first,*middle,last = grades
    return  sum(middle)/len(middle)

print (score((1,92,93,94,99)))

#有八个月 销售额 看前7个月平均值
money = [1,2,3,4,5,6,7,8]
*qian ,_ = money
print (sum(qian)/len(qian))


#星号解压 用于 切割字符串
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
name,*fields ,homedir,sh = line.split(':')
print(fields)

#丢弃多个数据
str1,*_, str2 = line.split(':')
print( str1,str2, end="")