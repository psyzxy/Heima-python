# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:11:05 2024

@author: 10852
"""

# type
print(type(66))
string_type = type("黑马")
print(string_type)

# 数据类型的转换
int(x)# 整数
float(X) 浮点数
str(C)字符串
int("11")
intnum = int(11.234)

# P19 标识符
11//2
9%2
#复合赋值运算符
num = 1
num += 1
print('result:',num)

# 单引号 双引号 三引号
"""注释 如果被接收 就不是注释 """

name = '"黑马字符"'
#转义字符\
# 字符串拼接
print("学的好"+"要坚持")
name = '好啊'
adress = 'BNU'
Tel = 666
print("我是:"+name)  %s %d 整数 %f 浮点型

# 通过占位的形式拼接
name='subject1'
message = 'corr '

# 
name = 'BNU'
setyear = 2009
price = 9.99
message = '%s,成立于:%d,我今天的股价是:%f'%(name,setyear,price)
print(message) 

# 格式化的精度控制 
# 使用m.n控制数据的宽度和精度 n对小数做精度控制的同时会四舍五入
num1=11
num2=11.234
print('数字11宽度限制3，是：%5d'%num1) 
print('11.234宽度5，是：%7.2f' %num2)
print('11.234宽度，是：%.2f' %num2)

# 快速格式化字符串
name = 'BNU'
year = 2013
price = 13.44
print(f'我是{name},成立于{year},价格是{price}')
#双引号和单引号好像都行
      
name = "我的"
set = 2006
stock = 19.19
print(f"我是{name},是{set}年的")

#对表达式进行格式化
print("1*1的结果是：%d" %(1*1))

name = '传智'
sprice = 19.99
scode = "003004"
growsfact = 1.2
growsday = 7

print(f"公司{name},股代码为{scode},股价为{sprice}")
print("每日增长系数：%.1f,经过%d天的增长后,股价达到了：%2.f" % (sprice,growsday,growsfact))

## 数据输入
print('woshishui')
name= input()
print('nishi:%s'%name)

name = input("告诉我你是谁")  #不管写什么 都会变成字符串 需要自行转换
name = int(name)
# 练习
username = input("输入用户名")
usertype = input("输入你类型")
print('尊敬的HM，您的用户名为：%s,是尊贵的%s用户，欢迎您的登陆'%(username,usertype))

# P29 布尔类型和比较运算符 True = 1
#==是否相等 !=是否不相等 
bool_1 = True
bool2_2 = False
print(f'1的变量内容是:{bool_1},类型是:{type(bool_1)}')
name1 = "zhao"
name2 = "Zhao"
print(f"结果是{name1==name2}")

# P30 if语句的基本格式
age =int(input("多大了"))
if age>18:
    print("成年啦")

age =30
if age>=18:  ##:不要忘了：
    print("成年")
print("时间过得真快")# 没有缩进 不影响

print("欢迎")
age = int(input("输入您的年龄："))
age = input("输入年龄")
if int(age)>18:
    print("你补票")
print("愉快")

if age>18:
    print("成年")
else:
    print("未成年")
## 不需要end
height = int(input("身高"))
vip = int(input("级别"))
day = int(input("日期"))
if height <120:
    print("free")
elif vip>3:
    print("vip free")
elif day ==1:
    print("day free")
else:
    print("都不行")
    
if int(input("身高"))<120:
    print("矮免费")

# 判断是互斥有序的 

num = 5
exnum = int(input("输入数字"))
if int(input("输入数字")) ==10    

#嵌套判断语句
if int(input("年龄"))>120 & 
    print("超过了")
    print("vip免费")
    if int(iput()):

# 实战案例 猜数字
import random
num = random.randint(1,10)
guess = int(inupt("输入猜测"))
if guess==num:
    print("第一次就对了")
else:
    if guess>num:
        print("猜大了再来")
    else:
        print("小了")
    guess = int(input("第二次猜"))
    if guess==num:
        print("第二次对了")
    else:
        if guess>num:
            print("猜大了再来")
        else:
            print("小了")
        guess = int(input("第二次猜"))
# 不想猜了 不想写了

 #P 38 循环功能
 i = 0
 while i<100:
     print("加油")
     i = i+1
     i+=1

i=1
sum = 0
while i<=100:
    sum = i+sum
    i+=1
print(sum)

# P 39
import random
num = random.randint(1, 100)
count = 0
flag = True
while flag:
    guess = int(input("你猜"))
    count+=1 
    if guess==num:
        print("对了")
        flag = False
    elif guess>num:
        print("大了")
    else:
        print("小了")
print(f'你猜了{count}次')
# 视频里用的是 if else 而我用的elif

#p 40
i = 1 
while i<=100:
    print(f"今天是第{i}天")
    j = 1
    while j <=10:
        print(f"第{j}朵")
        j+=1
    print("Love you")
    i+=1
print(f"第{i-1}天成功了")
# 注意缩进

# P41 
# 不让print换行
print("hello",end="")
print('wo',end='')
\t制表符
print("hi\two")
print('hollo\tni')
#P42 乘法表
i = 1
while i<=9:
    j = 1
    while j<=i:
        #内层循环不换行
        print(f"{j}*{i}={j*i}\t",end="")
        j+=1
    i+=1
    print()


#P43 for 循环
name = "hema"
for x in name:
    print(x,end="")

#  for 临时变量 in 待处理数据集:
count = 0
name="ithheima is a brand of itcast"
for x in name:
    if x =="a":
        count+=1
print(count)

#P 45
range(10) #0到10 不包含10
for i in range(10):
    print(i)
for x in range(5,10) 不包含10:
for x in rang(5,10,2) 步长为2:

i = 0
for i in range(5):
    print(i)
print(i)#按照规范不能 但是提前定义了i就可以

i=0
for i in range(1,101):
    print(f"今天是第{i}天")
    for j in range(1,11):
        print(f"送你{j}朵")
    print("Love you")
print(f"第{i}天成了")
#这个案例可以用for 和while相互嵌套使用达成目的

# P47 for循环打印9 9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end="")
    print()

# 49 break和continue
continue 中断本次 进入下一次
for i in range(1,100):
    print("语句1")
    continue
    print("语句2")


for i in range(1,6):
    print("1")
    for j in range(1,6):
        print("2")
        continue
    print("3")
print("4")


for i in range(1,100):
    print("语句1")
    break
    print("2")
print("语句3")

#P 50 综合案例 发工资 学这个的时候状态不好
money = 10000
import random
num = random   
for i in range(1,21):
    score = random.randint(1, 10)
    if score<5:
        print(f"余额不足，当前余额还有{money}元")
        continue
    if money >=1000:
        money-=1000
        print(f"员工{i},发放1000，公司余额{money}")
    else:
        print(f"余额不足，当前余额{money}元，不足以发工资，下个月再发")
        break
    
### P51
str1 = "wohaofan"
str2 = "nishishui"
count = 0
for i in str1:
    count+=1
print(f"长度{count}")

def my_len(data):
    count =0
    for i in data:
        count+=1 
    print(f"字符串{data}的长度是{count}")

my_len(str1)    

# P52 
def sayhi():
    print("hiIamHema")
# 调用函数
sayhi()

# P53

print("欢迎\n出示健康")


# P54 传入参数 
def add(x,y):
    result  = x+y 
    print(f"结果是{result}")

add(5,6)  
    x,y为形式参数，5,6为实际参数

# 可以不使用也可以使用任意N个参数 

# P55
def hs(t):
    if t<37.5:
        print('合格')
    else:
        print("不合格")    
hs(30)

## P56函数返回值
def add(x,y):
    result  = x+y 
    print(f"结果是{result}")
    return result
    print("dwwd")# 不会执行
# return 关键字后都不执行了！！！！！
r = add(2,3)
print(r)

# P57 None 特殊字面量
不写return会返回None
def sayhi():
    print("hiIamHema")

result =sayhi()
print(result)
type(result)

在 if判断中 None 等同于False

def cheakage(a):
    if a>18:
        return "success"
    else:
        return None
    
result = cheakage(17)
if not result:
    # 能够进入if说明result是None
    print("fobidden")

# None用于声明无初始内容的变量
name = None

#P58 函数说明文档
def func(x,y):
    """
    函数说明
    ：paraX blala
    : param Y blabla 
    : return 一个很菜的函数
    """
悬停可以查看说明文档

# P59 嵌套调用
def fa():
    print("1")
def fb():
    print("2")
    fa()    
    print(3)       
fb()
    
# P60 
局部变量 全局变量

def testa():
    num=100
    print(num)
test()
局部变量 全局变量

num = 200
def testa():
    print(f"testa:{num}")
print(num)

#在函数内修改全局变量
num = 200
def testb():
    #global关键字声明a是全局变量
    global num
    num = 500
    print(num)
print(num)

# 61 如果这一章只看一节 就看这一节
money = 50000
name = None
name = input("输入姓名")
def query(show_header):
    if show_header:
        print("查询余额")
    print(f"您好{name}剩余{money}")
def saving(num):
    global money
    money+=num
    print(f"存款{num}")
    query(False)
def getmoney(num):
    global money
    money-=num
    print("---取款-----")
    query(False)
def main():
    print("--主菜单---")
    print(f"{name},您好，欢迎来到ATM")
    print("--主菜单---")
    print("查询余额\t输入1")
    print("存款\t\t输入2")
    print("取款\t\t输入3")
    print("退出\t\t输入4")
    return input("请输入你的选择")
while True:
    keyboardinput = main()
    if keyboardinput =="1":
        query(True)
        continue
    elif keyboardinput == "2":
        num=int(input("请输入您要存多少"))
        saving(num)
        continue
    elif keyboardinput == "3":
        num = int(input("取多少"))
        getmoney(num)
        continue
    else:
        break
           
main()
  
 
# 第六章 数据容器
 # list 列表
 []作为标识
 空列表 变量=[]或者=list()
 
 nalist = ["wo",'shi',"傻"]
 print(nalist)
 type(nalist)
嵌套列表 
mylist = [[1,2,3],[4,5,6]]
mylist = ['hema',666,True]
print(mylist)

# 下标索引
namelsit=['tom','lily','rose']
print(namelist)
print(namelsit[0])
print(namelsit[-1])     

嵌套列表的下标索引
mylist = [[1,2,3],[4,5,6]]
print(mylist[1][2])
从0开始 从-1开始
 # P65 列表的常用操作
方法和函数 调用形式不太一样
#查询下标 index
mylist = [[1,2,3],[4,5,6]]
mylist = ["it",'jijl','dwaf']
mylist.index("it")
# 修改下标索引的值
mylist = ["it",'jijl','dwaf']
mylist[0]="nnn"
print(mylist)
# 在列表中进行元素的插入
mylist.insert(1, 'wowoowo')
print(mylist)
# 在列表中追加元素 （添加到最后）
mylist.append("pppp") 
print(mylist)
# 追加一批 元素
mylist2 = [1,2,3]
mylist.extend(mylist2)
print(mylist)
# 元素的删除
mylist = ["it",'jijl','dwaf']
del mylist[2]
element = mylist.pop(2)         
print(mylist)  
print(element) # pop 可以删掉元素并且把元素返回出来
#mylist = ["it",'jijl','dwaf']
mylist = ["it",'jijl','dwaf','it']
mylist.remove('it')
print(mylist) # 删除第一个it 只能删除一个

# 请空列表
mylist.clear()
print(mylist)

# 统计某一个元素的数量
mylist = ["it",'jijl','dwaf','it']
count = mylist.count("it")
print(count)
## 统计列表中多少个元素
count = len(mylist)
print(count)

calist = [21,25,21,23,22,20]
calist.append(31)
calist.extend([23,35,36])
num1 = calist[0]
num2 = calist[-1]
num3 = calist.index(25)

#P67 循环遍历 遍历就是依次取出处理  使用两种语言
def listf():
    mylist = [21,25,21,23,22,20]
    index = 0
    while index<len(mylist):
        element = mylist[index]
        print(f"列表：{element}")
        index+=1

listf()

def list_for_func():
    mylist = [21,25,21,23,22,20]
    for num in mylist:
        print(num)
        
list_for_func()
        
# if num%2 = =0
# P68 元组能储存不同的元素  但不能修改
元组使用小括号
a = ()
a = (1,2,3,5,6,5)
a = tuple() 
print(a)    
t1 = (1,"hrllp","e3e")
t2 = ("hello")
print(type(t2))
只有一个数据需要添加逗号
t2 = ("hello",)
嵌套元组
t5 = ((1,2,3),(4,5,6))
下标索引取出内容 6
num = t5[1][2]
print(num)

元组的操作 
index count len
t6 = ("传智教育","黑马程序员","python")
index = t6.index("黑马程序员")
num= t6.count("传智教育")
len(t6)

元组的遍历
ind = 0
while ind<len(t6):
    print(f"元组的元素有:{t6[ind]}")
    ind+=1

for i in t6:
    print(i)

和matlab的循环不太一样
#
t9 = (1,2,["it","wo"])
t9[2][0] = "ooo" 
print(t9)
!!!!!!元组里嵌套list,list可以修改

# P 69 字符串
name = "itheima"
my_str = "jjijh"
#下标索引
m = my_str[4]
m = my_str[-1]
print(m)
# 同元组一样 无法修改
my_str[2] = "H"会报错 不能修改
#index
va = my_str.index('jh')
print(va) 
#replace方法
n = my_str.replace("jj","KKK")     
print(n)
#
mystr = "  hh kkk www  "
mm = mystr.split(" ")
print(mm)     
#字符串的规整方法     
strip()
nn = mystr.strip()  #去除收尾空格
print(f"将{mystr}分割后得到的{nn}")

mystr="12hh and ww21"
ne = mystr.strip("12")# 去除字符串1和字符串2
print(ne)

#统计字符串中某字符串出现次数
cc = mystr.count("21")
print(cc)
ss = len(mystr)
print(ss)

index = 0
while index<len(mystr):
    print(mystr[index])
    index+=1

for i in mystr:
    print(i)

#P 70
mystr = "itheima itcast boxuegu"
co = mystr.count("it")
cc = mystr.replace(" ","|")
ne = mystr.split("|")
print(co,cc,ne)

#P71 序列
#切片操作
[起始下标：结束下标：步长]
左闭右开 
# list切片
mylist = [0,1,2,3,4,5,6]
print(mylist[1:4])
# tuple

tuple2 = (0,1,2,3,4,5)
print(type(tuple2))
mytuple = tuple2[:]
print(mytuple)

mystr = "itheima itcast boxuegu"
mys=mystr[::2]
print(mys)

mystr = "01234567"
res = mystr[::-1] #相当于翻转
print(res)

tuple2 = (0,1,2,3,4,5)
tu=tuple2[::-1]
print(tu)

astr = "万过薪月,员序程黑马来,nohtyP学"
res1 = astr[::-1][9:14]
res2 = astr[5:10][::-1]
## 可以这样连这写！
sp = astr.split(",")[1].replace("来","")[::-1]
print(res1,res2,sp)


# P73集合 无序 不能重复 允许修改
myset = {"wadawe","我","的回答","wadawe","我","的回答","wadawe","我","的回答"}
myset2 = set()
print(myset)
不能重复 内容无序
myset.add("python")
myset.add("我")
myset.remove("wadawe")
print(myset)
el = myset.pop() 随意取 没有 索引
print(el)
myset.clear() 清空
取出差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)# 1有2没有的
print(set3)

set4 = set1.difference_update(set2)
print(set1)

set5 = set1.union(set2)
print(set5)
#统计元素数量
cou = len(set1)
print(cou) #是去重的 因此重复值不会计算
while #不支持下标索引 因此不能用
for e in set2:
    print(e)

mylist = ["黑马","传智","it","heima",'it']
set0=set()
for i in mylist:
    set0.add(i)
print(set0)

# P75 字典
key：value 使用{}
空{} 或者dict()
mydict = {"王力宏":99,"周杰伦":93,"林俊杰":97}
mydict2={}
print(mydict,mydict2)
字典的key不可以重复
mydict = {"王力宏":99,"周杰伦":93,"林俊杰":97}
不可以使用下标索引
print(mydict["王力宏"])
key不能为字典 可以嵌套
mydict = {"王力宏":99,"周杰伦":93,"林俊杰":97}

mydict3 = {"王力宏":{
    "语文":99,
    "数学":67},
    "周姐":{"语文":93,
          "数学":57}
          }
print(mydict3["周姐"]["语文"])
print(mydict3["王力宏"]["数学"])
# 键值对

# P76字典的常用操作
mydict = {"王力宏":99,"周杰伦":93,"林俊杰":97}
mydict["赵子"]=66
mydict["王力宏"]=88
print(mydict)
#删除
mydict = {"王力宏":99,"周杰伦":93,"林俊杰":97}
score= mydict.pop("王力宏")
print(mydict,score)
mydict.clear()
#取出全部的keys
keys =mydict.keys()
print(keys)
for key in keys:
    print(mydict[key])

for k in mydict:
    print(mydict[k]) ##这种写法
num = len(mydict)
print(num)

# P77
infodict ={
    "王丽":{
        "部门":"科技部",
        "工资":3000,
        "级别":1   
          },
    "周姐":{"部门":"市场部",
            "工资":5000,
            "级别":2 },
    "林俊":{"部门":"市场部",
            "工资":7000,
            "级别":3 },
    "张雪":{"部门":"科技部",
            "工资":4000,
            "级别":1},
    "刘德":{"部门":"市场部",
            "工资":6000,
            "级别": 2}
    }
print(infodict)
for name in infodict:
    if infodict[name]["级别"] ==1:
        epinfodict = infodict[name]
        epinfodict["级别"]=1 
        epinfodict["工资"]+=1000
        infodict[name] = epinfodict
print(f"加薪后{infodict}")

# P78 总结课  
从486行开始-810行

# P 79
都支持for循环
len max min 
字符串比较大
使用 list() str tuple set 转换
dict 需要键值对
sorted(容器)
mylist = [1,2,3,4,5,9,6]
print(sorted(mylist,reverse=True))#默认是FALSE

# P80 字符串大小比较
基于 ASCII码对应 
按 位置比较
print(f'{"abd">"abc"}')

# p81 第七章 Python进阶 
# 多返回值 我tmd终于学到进阶了
def testre():
    return 1,2,3 
x,y,z = testre() 按照 顺序
print(x,y,z) 

# P 82 函数的多种参数使用方式

def userinfo(name,age,)

关键字参数 
def user_info(name,age,gender):
    print(f"名字是：{name}，年龄是{age},性别是{gender}")

#位置参数
user_info("小米",20,"难")
user_info(age=20, name="小王", gender="女")#可以不按顺序
user_info("天天", age=99, gender="难")

# 缺省参数 可覆盖
def usinf(name,age,gender = "难"):
    print(f"名字是：{name}，年龄是{age},性别是{gender}")
usinf("我", 22)
默认值必须放在最后 

# 不定长参数 可变参数
#1位置不定长 
def useinf(*args):#不一定叫这个args
    print(args)
useinf(1,2,2,"大河")

# 关键字不定长keyword 数量不受限
# 形式必须是key-word
def useinf(**kwargs):
    print(kwargs)
useinf(name="wew", age=12)

# P83 函数作为参数传递
# 逻辑不确定 数据确定 传入计算逻辑
def test_func(compute):
    result=compute(1,2)
    print(type(compute))
    print(result)
def compute(x,y):
    return x+y
test_func(compute)

#P84 匿名函数
lambda关键字 定义无名称函数
def test_func(compute):
    result=compute(1,2)
    print(result)
test_func(lambda x,y:x+y)# 无法写多行 自带return功能

# P85 第八章 文件编码概念 这个应该对我很有用
# 使用不同的编码 UTF-8 现在最常用

#P86 文件的读取操作
open(name,mode,encoding)
C:\Users\10852\Desktop\服务器
f = open('C:/Users/10852/Desktop/服务器/todonback2.txt')

f= open("python.txt",'r',UTF-8)
r只读 w 写入  a 追加



























