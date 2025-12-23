# 3.九九乘法表
def Multiplication_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={i*j}',end='\t')
        print(end='\n')

if __name__ == '__main__':
    Multiplication_table()