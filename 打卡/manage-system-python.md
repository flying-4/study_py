# 大学生勤工助学薪资发放管理系统（Python 重写版）

## 这是什么

这是一个把 C 语言课程综合练习“大学生勤工助学薪资发放管理系统”改写成 Python 的练习项目。

程序用于管理勤工助学岗位和学生薪资，主要功能包括：

- 管理员密码登录。
- 岗位的添加、修改、删除、查询和显示。
- 学生薪资记录管理。
- 根据工作时长和岗位时薪计算应发薪资。
- 录入扣款并计算实发薪资。
- 更新薪资发放状态。
- 按学号、部门或日期查询。
- 按实发薪资升序或降序排列。
- 统计指定部门当月薪资支出。
- 备份薪资数据并清理超过两年的旧记录。

管理员初始密码是数字 `1`。

## 怎么运行

### 1. 准备环境

需要安装 Python 3.8 或更高版本。项目只使用 Python 标准库，不需要安装额外依赖。

检查 Python 是否已经安装：

```powershell
python --version
```

如果 Windows 上 `python` 命令不可用，可以尝试：

```powershell
py --version
```

### 2. 进入项目目录

```powershell
cd manage-system-python
```

如果项目位于其他位置，请进入包含 `main.py` 和 `README.md` 的目录。

### 3. 启动程序

Windows：

```powershell
python main.py
```

也可以使用：

```powershell
py main.py
```

macOS 或 Linux：

```bash
python3 main.py
```

启动后输入管理员密码 `1`，再根据菜单输入功能编号。

### 4. 数据文件

程序会在当前项目目录读取和保存以下文件：

- `job.txt`：岗位信息。
- `salary.txt`：学生薪资记录。
- `salary_all.txt`：完整薪资备份。
- `salary_backup.txt`：导出或清理旧记录时使用的薪资备份。

数据文件使用 UTF-8 编码。不要直接用其他编码覆盖这些文件，否则中文姓名、岗位名称和扣除原因可能变成乱码。

SQLite、MySQL 或网络服务不是本项目的运行前提。

## 和 C 版本有什么区别

| C 版本 | Python 版本 |
| --- | --- |
| 使用 `struct` 表示岗位和薪资记录 | 使用 `dict` 表示一条岗位或薪资记录 |
| 使用链表以及 `malloc`、`free` 管理记录 | 使用 Python `list` 保存记录，由 Python 自动管理内存 |
| 使用 `scanf` 获取输入 | 使用 `input()` 获取输入，并增加数字格式校验 |
| 使用 `printf` 输出信息 | 使用 `print()` 和 f-string 输出信息 |
| 手动维护 `head`、`tail`、`next` 指针 | 直接遍历或追加列表元素，不再需要指针操作 |
| 使用 C 文件流读取和写入文本 | 使用 Python 标准库读取和写入 UTF-8 文本文件 |
| 使用 `system("cls")` 和 `system("pause")` | 使用跨平台的菜单循环，不依赖 Windows 命令 |
| 原始数据文件使用 GBK 编码 | 数据文件统一使用 UTF-8 编码 |
| “按部门查询薪资”菜单误调用了岗位查询 | 修正为根据岗位所属部门查询薪资记录 |
| 输入错误时可能产生未定义行为 | 对整数、浮点数、空输入和无效范围进行校验 |

Python 版保留原 C 版的主要菜单分组和业务含义，但实现方式更适合用 Python 表达：

```c
typedef struct Job {
    int number1;
    char name[100];
    char department[100];
    float wage;
    int max;
    int people;
    struct Job *next;
} Job;
```

对应 Python 数据：

```python
{
    "number1": 101,
    "name": "图书管理员",
    "department": "图书馆",
    "wage": 18.5,
    "max_hours": 40,
    "people": 8,
}
```

C 版的链表：

```c
job->next
list->head
list->tail
```

在 Python 版中由列表代替：

```python
jobs.append(job)
for job in jobs:
    if job["number1"] == number1:
        return job
```

## 项目文件

```text
manage-system-python/
├── main.py
├── job.txt
├── salary.txt
└── README.md
```

如果这是第一次运行，建议先备份 `job.txt` 和 `salary.txt`，再测试添加、修改和删除功能。

## 运行后建议检查

1. 添加一个岗位，退出程序后重新进入，确认岗位仍然存在。
2. 添加一条学生薪资记录，确认：

   ```text
   应发薪资 = 工作时长 × 岗位时薪
   实发薪资 = 应发薪资 - 扣除金额
   ```

3. 按学号查询该记录，并将发放状态改为“已发放”。
4. 退出并重新运行程序，确认岗位和薪资记录都能正常加载。
