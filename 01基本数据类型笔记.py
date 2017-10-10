#基本数据类型

#数值类型  4
'''
整形  int

浮点型 float

布尔型 bool

复数型  complex
'''
#整形
a = 0
b = -1
print(type(a))

#浮点型
f = 1.1
f1 = -1.1
type(f)

#布尔型
t = True   #1
f = False  #0

#复数型  complex,虚部只能用j
c = 1 + 2j

#####数值运算
a = 2
b = 2.5
a + b
a - b
a * b
a/b   # 0.8
a//b  #（整除，向下取整）
10 % 2 #取余
9**2  # 9的平方
3**3  # 3*3*3


#####序列类型
'''
字符串  str     不可变
列表    list    可变
元祖    tuple   不可变

'''
s = 's'
#s ='ss''ss'   #  'ssss'
s1 = "ss"
s3 ="ddd'aa'"   #当我们，字符串里面有单引号的时候，用双引号
s4 =''' aaa'''
s5 = ''' bbb
ddd
'''

##注释 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
1. #号，不可以换行,#后面全部被注释了
2. 三引号，可以支持换行

'''

#变量的命名规则：
'''
1. 变量名必须，字母、下划线、数字组成
2. 不能以数字开头
3. 不能用关键字
'''

#555 = 'a'  报错
#我 = 'a'   汉字也行，不符合规范
#False = 1  报错

import keyword
keyword.kwlist


# False == 1
'''
一个等于号代表复值，== 代表，判断是否相等

'''

##list  列表
li = [1,2,3,4]


#tuple  元祖
tu = (1,2,3,4)
tu2 = 1,2
tu3 =(1,)

###### 索引
li =[1,2,3,4,5]
tu = (1,3,4,5)
s='asd'
li[0]  #取出第一个元素，索引是从0开始

##正向索引
li[1]  
tu[2]
s[0]
###反向索引 ， -1：取出倒数第一个。-2：取出倒数第二个
li[-1]
s[-1]
tu[-2]


#切片 ：取出一小段  （左闭右开）

li[0:2]  #[1, 2]，左边边界能取到，右边边界不能取到
s[1:2]
tu[1:3]

#步长
tu[0:4:3]  #(1, 5)

tu[:]  # 默认是从0 - 最后

tu[1:4]
tu[1:4:]  #默认步长为1

tu[::]  ###全体输出


#负步长
tu[3:1:-1]
tu[3:1:-2]

#赋值运算
li *= 2
a +=1
a *= 4

#成员运算

#in  判断是否  在
's' in s  # True
'm' in s  # False

#not  in  判断是否  不在
's' not in s  # False
'm' not in s   # True

############3  可变  不可变
id(1)  #如果id，就说明同一个内存地址，就说明同一个对象







