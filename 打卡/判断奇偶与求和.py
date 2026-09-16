n=int(input("请输入数字"))
if n%2==0:
    print("偶数")
else:
    print("奇数")
    
print("*"*20)
sum=0    
for i in range(1,101):
    sum+=i
print(sum)
