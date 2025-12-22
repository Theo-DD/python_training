# 2.石头剪刀布
# 1）. 从控制台输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）
# 2）. 电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能
# 3）. ⽐较胜负
import random

def finger_guess():
    dict_figer = {1:'石头', 2:'剪刀',3:'布'}
    while True:
        ran = random.randint(1,3)
        inp = int(input('请输入您要出的拳的代号：（⽯头(1)/剪⼑(2)/布(3)）'))
        if determine(ran,inp) == ran:
            print(f'本次获胜的是电脑，对局详情:电脑VS人/{dict_figer[ran]}VS{dict_figer[inp]}')
            break
        if determine(ran,inp) == inp:
            print(f'本次获胜的是您，对局详情:电脑VS人/{dict_figer[ran]}VS{dict_figer[inp]}')
            break

def determine(a,b):
    if a in [1,2] and b in [1,2]:
        return 1
    if a in [1,3] and b in [1,3]:
        return 3
    if a in [2,3] and b in [2,3]:
        return 2


if __name__ == '__main__':
    finger_guess()
