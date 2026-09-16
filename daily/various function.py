#数据类型，type判断数据类型
message="hellow world"#字符串
age=10                #整型
pi=3.14               #浮点数
judge=True            #布尔值
print(message,age,pi,judge)
print(type(message),type(age),type(pi),type(judge))


#列表list
fruits=['苹果','香蕉','橘子']
fruits[0]='李子'                #元素可修改
                                #注释快捷键ctr+/
print(fruits[0])

fruits.append('西瓜')           #在末尾添加元素,列表被改变
print(fruits) 

#元组（不可以被修改，例如添加元素操作或赋值操作
fruits_tuple=('苹果','香蕉','橘子')
print(type(fruits),type(fruits_tuple))


#for循环
for f in fruits:
    print(f)          #f代表fruits里的每一个元素且依次遍历
    print(fruits)     

for i in range(10):    #0到9，步长为1
    print(i)
    print(i**2)        #计算i的平方
    print(range)
#range 是一个类型/函数，不是一个变量名
#range(10) 才是你生成的数字序列对象
#如果你打印 range 本身，会得到 <class 'range'>
#如果你想查看 range(10) 里的内容，可以用 list(range(10)) 转换成列表查看
#如果你想打印 1 到 10，可以写成 for i in range(1, 11):（1到11，步长为1）。
#如果你想每隔 2 打印一次，比如 0, 2, 4, 6, 8，可以写成 for i in range(0, 10, 2):（步长为 2）
    
num=[1,2,3,4]
print(type(num))
total=0
for i in num:          #累加运算
    total+=i
print(total)


#if语句,从上往下依次做判断
number =66
if number<18:
    print('未成年')
elif number<65:         #如果成立则意味着18<=number<65
    print('成年人')
else:
    print('老年人')


#字典（像c语言的结构体）key->value映射关系，键值对
person={'name':'王晓二','age':18,'city':'杭州'}
print(person['name'])     #打印单个键的值
print(person.keys())      #打印所有键
print(person.values())    #打印所有值
print(person.items())     #打印所有键值对（每个键值对是一个元组）

for k,v in person.items():
    print(k,':',v)    #k对应键，v对应值


#函数
def hello1(name):
    return 'hello,'+name    #name表示参数

def hello2(name):
    return f'hello,{name}'  # 返回一个格式化字符串，f表示格式化字符串

print(hello1('王晓二'))
print(hello2('里芳芳'))

def square(x):
    return x**x

print(square(5))
    

#面向对象OOP
#类
class Calculate:                # 定义一个名为 Calculate 的类
    def __init__(self,num):     # 初始化方法（构造函数）
        self.num=num            # 将参数 num 存储为实例属性
        
    def sum(self): 
        total=0
        for i in self.num:
            total +=i
        return total
    
    def avg(self):
        return self.sum()/len(self.num)

nums=[1,2,3,4]
calc=Calculate(nums)
print(calc.sum())
print(calc.avg())

#print

#..........................................print函数
# 基本用法
print("Hello World")

# 多个参数，自动用空格分隔
print("Hello", "World", 123)  # 输出：Hello World 123

# 自定义分隔符 sep
print("Hello", "World", sep="---")  # 输出：Hello---World

# 自定义结束符 end（默认是 \n 换行）
print("Hello", end=" ")
print("World")  # 输出：Hello World

# 输出到文件
with open("test.txt", "w") as f:
    print("Hello", file=f)

#...................................字符串格式化输出
# f-string
name = "张三"
age = 25
print(f"我叫{name}，今年{age}岁")
print(f"10年后我{age + 10}岁")  # 可执行表达式

#format
print("我叫{}，今年{}岁".format(name, age))
print("我叫{0}，今年{1}岁".format(name, age))  # 位置索引
print("我叫{name}，今年{age}岁".format(name=name, age=age))  # 关键字参数

#%格式化，不推荐新项目使用
print("我叫%s，今年%d岁" % (name, age))
print("圆周率：%.2f" % 3.14159)  # 输出：3.14

#...................................#sys.stdout.write()
import sys
sys.stdout.write("Hello World\n")  # 需要手动添加换行符
sys.stdout.write("第二行")


#...................................日志输出（logging 模块）
import logging

logging.basicConfig(level=logging.INFO)
logging.info("信息输出")
logging.warning("警告输出")
logging.error("错误输出")

#..................................文件输出
# 写入文件
with open("output.txt", "w") as f:
    f.write("写入内容\n")
    f.writelines(["第一行\n", "第二行\n"])

#..................................调试输出
from pprint import pprint

data = {"name": "张三", "hobbies": ["读书", "游泳", "编程"], "info": {"age": 25, "city": "北京"}}
pprint(data)  # 美化打印复杂数据结构