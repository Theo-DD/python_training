# 4.用函数实现100-200之间的素数
def sushu(m, n):
    a = list()
    for i in range(m, n+1):
        div = 0
        for j in range(2, i):
            if i % j == 0:
                div = 1
        if div == 0:
            print(i,end=' ')
            a.append(i)
    return a

if __name__ == '__main__':
    m = 100
    n = 200
    a = sushu(m, n)
    print(f"\n{m}到{n}之间的所有素数共有{len(a)}个")






