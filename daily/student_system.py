"""
学生管理系统 —— Python 版
对标 C 课程中常见的"学生信息管理系统"，展示 Python 的写法

如果你写过这个系统的 C 版本，对比一下差异：
1. 没有 struct → 用 dict
2. 没有 malloc/free → 直接 append/remove
3. 没有 printf/scanf → 用 print/input
4. 没有指针 → 变量直接引用
"""
import os
# ============================================================
# 数据层 —— C 里用 struct + 链表，Python 用 list + dict
# ============================================================

# 用一个列表存所有学生，每个学生是一个字典
students = []

# 初始化几个示例数据
students.append({"id": 1001, "name": "张三", "age": 19, "score": 88.5})
students.append({"id": 1002, "name": "李四", "age": 20, "score": 92.0})
students.append({"id": 1003, "name": "王五", "age": 18, "score": 73.5})
#append 就是在列表末尾添加一个元素

# ============================================================
# 功能函数
# ============================================================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """显示菜单 —— C 版是 printf + switch"""
    print("\n===== 学生管理系统 =====")
    print("1. 显示所有学生")
    print("2. 添加学生")
    print("3. 删除学生")
    print("4. 查找学生")
    print("5. 修改成绩")
    print("6. 统计信息")
    print("0. 退出")
    print("========================")


def show_all_students():
    """显示所有学生 —— 对应 C 版的遍历链表"""
    if not students:
        print("当前没有学生数据")
        return
    
    print(f"\n{'学号':<8}{'姓名':<8}{'年龄':<6}{'成绩':<8}")
    print("-" * 30)
    for s in students:
        # f-string 格式化输出，对应 C 的 printf
        print(f"{s['id']:<8}{s['name']:<8}{s['age']:<6}{s['score']:<8.1f}")
    print(f"\n共 {len(students)} 名学生")


def add_student():
    """添加学生 —— 对应 C 版的链表插入节点"""
    print("\n添加新学生")
    
    # input() 对应 C 的 scanf
    # int() / float() 做类型转换
    sid = int(input("请输入学号："))
    
    # 检查学号是否已存在 —— C 版需要遍历链表
    for s in students:
        if s["id"] == sid:
            print("学号已存在！")
            return
    
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    score = float(input("请输入成绩："))
    
    # 创建一个新学生（dict），加到列表 —— C 版要 malloc 一个新节点
    new_student = {
        "id": sid,
        "name": name,
        "age": age,
        "score": score
    }
    students.append(new_student)  # 不用管内存释放！
    print(f"学生 {name} 添加成功")


def delete_student():
    """删除学生 —— 对应 C 版的链表删除节点"""
    sid = int(input("请输入要删除的学号："))
    
    # Python 的列表删除，一行搞定
    # C 版需要：找到节点 → 前驱节点的 next 指向后继 → free 当前节点
    for i, s in enumerate(students):
        if s["id"] == sid:
            removed = students.pop(i)  # pop 即删除，自动调整列表
            print(f"学生 {removed['name']} 已删除")
            return
    
    print("未找到该学号")


def find_student():
    """查找学生"""
    keyword = input("请输入姓名或学号：")
    
    found = []
    for s in students:
        # 支持按姓名或学号查找
        if keyword.isdigit() and s["id"] == int(keyword):
            found.append(s)
        elif keyword in s["name"]:
            found.append(s)
    
    if not found:
        print("未找到匹配的学生")
    else:
        for s in found:
            print(f"学号：{s['id']}  姓名：{s['name']}  年龄：{s['age']}  成绩：{s['score']}")


def update_score():
    """修改成绩"""
    sid = int(input("请输入要修改的学号："))
    
    for s in students:
        if s["id"] == sid:
            new_score = float(input(f"{s['name']} 当前成绩：{s['score']}，新成绩："))
            s["score"] = new_score
            print("修改成功")
            return
    
    print("未找到该学号")


def show_stats():
    """统计信息"""
    if not students:
        print("没有数据可统计")
        return
    
    scores = [s["score"] for s in students]  # 列表推导式，Python 特色
    avg = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    passed = len([s for s in students if s["score"] >= 60])
    
    print(f"\n===== 统计信息 =====")
    print(f"学生总数：{len(students)}")
    print(f"平均成绩：{avg:.1f}")
    print(f"最高分：{max_score}")
    print(f"最低分：{min_score}")
    print(f"及格人数：{passed} / {len(students)}")
    print(f"及格率：{passed / len(students) * 100:.1f}%")


# ============================================================
# 主循环 —— 对应 C 的 int main() + while + switch
# ============================================================

def main():
    """主函数"""
    print("欢迎使用学生管理系统（Python 版）")
    
    while True:
        show_menu()
        choice = input("请选择操作：")
        clear_screen()
        # Python 没有 switch，用 if-elif 代替
        if choice == "1":
            show_all_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            find_student()
        elif choice == "5":
            update_score()
        elif choice == "6":
            show_stats()
        elif choice == "0":
            print("感谢使用，再见！")
            break
        else:
            print("无效选择，请重新输入")
        
        input("\n按回车键继续...")  # 暂停，方便看结果
        clear_screen()

# ============================================================
# 程序入口
# ============================================================

# Python 的习惯写法：当文件被直接运行时执行 main()
# 被别的文件 import 时不执行
if __name__ == "__main__":
    main()
