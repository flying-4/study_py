# 变量赋值 —— 不需要声明类型
score=80.6
age=90
name='华强'
print(f"score:{score}\nage:{age}\nname:{name}")
print('*'*20)
# 列表 —— 等于 C 的数组 + 动态容量
score=[20.3,56.4,89.4656,646.4546]
score.append(48786.546)
print(score[2])
print(len(score))
print('*'*20)
# 条件和循环
for i in range(5):
    print(i)
    print(score[i])
    if score[i] >=60:
        print('及格')
    else:
        print('不及格')
print('*'*20)    


# while 循环
cout=0
while cout<5:
    print(cout)
    cout+=1
print('*'*20)

#函数
def add(a,b):
    return a+b
print(f'{add(5,6)}')
print('*'*20)

#字符串操作
person='刘华强'
print(person[0])# 张
print(len(person))# 2
print(person+'同学')# 张三同学
print(f'姓名：{person}')# f-string，最常用的格式化方式
print('*'*20)

text='hellow,world'
print(text.split(','))# 分割成列表
print(text.upper())# 大写
print(text.replace('hellow','shan'))# 替换
print('*'*20)

# 输入 5 个学生的成绩，计算平均分，打印及格和不及格的人数
def main():
    scores = []
    for i in range(5):
        s = int(input(f"请输入第{i+1}个学生的成绩："))
        scores.append(s)
    
    avg = sum(scores) / len(scores)
    passed = len([s for s in scores if s >= 60])
    failed = 5 - passed
    
    print(f"平均分：{avg}")
    print(f"及格人数：{passed}")
    print(f"不及格人数：{failed}")

main()
