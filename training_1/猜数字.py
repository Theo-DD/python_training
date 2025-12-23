# 1.猜数字，这个数字是3位数
import random

def guass():
    ran = random.randint(100, 999)
    n = 0
    while True:
        inp = int(input('请输入您猜测的数:'))
        if inp>ran:
            print('大了！')
        elif inp<ran:
            print('小了！')
        elif inp == ran:
            print('恭喜您，猜对了！')
            break
        if abs(inp-ran)<=10:
            print('接近了')
        n += 1
    return ran,n

if __name__ == '__main__':
    ran,n = guass()
    print(f'最终答案是{ran},您共答题{n}次')