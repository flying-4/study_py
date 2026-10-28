##写一个电话本：添加、查找、列出联系人
##用列表套字典存一组学生，遍历并打印
#添加
phonebook={}
def add_phone(name,phone):
    phonebook[name]=phone
    print(f"成功添加{name}：{phone}")
    
#查找
def find_phone(name):
    return phonebook.get(name)
    
#列出
def list_phone():
    if not phonebook:
        print(f"电话本为空")
        return None
    for i,(name,phone) in enumerate(phonebook.items(),1) :
        print(f"{i}.{name:<10}{phone}")
        
#删除
def delete_phone(name):
        return phonebook.pop(name,None) is not None
    
def main():
    add_phone("alice", "138-0000-1111")
    add_phone("bob",   "139-0000-2222")
    add_phone("carol", "137-0000-3333")
    
    print(f"请查找")
    print(find_phone(input()))
    list_phone()
    
    print(f"请删除")
    print(delete_phone(input()))
    list_phone()
    
    students = [
    {"name": "小明", "age": 18, "score": 92},
    {"name": "小红", "age": 19, "score": 88},
    {"name": "小刚", "age": 18, "score": 76},
    ]

    # 1) 简单遍历打印
    
    
    # 2) 带序号 + 对齐打印
    

    # 3) 求平均分
    

    # 4) 筛选：成绩 >= 85
    

    # 5) 按成绩排序（不修改原列表）
    
    
    
    
if __name__=="__main__":
    main()
    