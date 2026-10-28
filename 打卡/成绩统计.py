#输入 5 个成绩，输出平均分、及格人数和不及格人数
def get_score(n=5):
    score=[]
    for i in range(n):
        while 1:
            try:
                s=float(input(f"请输入第{i+1}个成绩"))
                if 0<=s<=100:
                    score.append(s)
                    break
                else :
                    print(f"请重新输入")
            except ValueError:
                print(f"请输入数字")
    return score

def analyze(score,pass_line=60):
    avg=sum(score)/len(score)
    passed=0
    failed=0
    for s in score:
        if s>=60:
            passed+=1
        else:
            failed+=1
    return avg,passed,failed

def main():
    score=get_score()
    avg,passed,failed=analyze(score)
    print(f"成绩列表{score}")
    print(f"平均分{avg:.3f}")
    print(f"及格人数{passed}")        
    print(f"不及格人数{failed}")
                
if __name__=="__main__":
    main()                
            