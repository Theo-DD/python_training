import numpy as np
import random


def starting():
    door = rand_car()
    choice = int(input('请在三个门中选择一个门：'))
    judgment(door, choice)


def rand_car():
    door1 = {
        1: '山羊',
        2: '山羊',
        3: '山羊'
    }
    q = np.random.randint(1, 4)
    door1[q] = '汽车'
    print(door1)
    return door1



def judgment(door, choice):
    if door[choice] == '山羊':
        keys = list(door.keys())
        keys.remove(choice)
        for i in keys:
            if (i != choice) & (door[i] != '汽车'):
                print(f'现在打开{i}号门，门后为:{door[i]}')
                keys.remove(i)
        re_election(choice,keys[0], door)
    if door[choice] == '汽车':
        keys = list(door.keys())
        keys.remove(choice)
        s = np.random.randint(0, 2)
        print(f'现在打开{keys[s]}号门，门后为:{door[keys[s]]}')
        keys.remove(keys[s])
        re_election(choice, keys[0], door)


def re_election(choice,key0,door):
    yn = input(f'你想改选{key0}号门么？[y/n]')
    if yn == 'y':
        ending(key0, door[key0], 1)
    else:
        ending(choice, door[choice], 0)


def ending(num,gift,x):
    print(f'你的选择是{num}号门，门后是{gift}')
    if gift == '汽车':
        print('恭喜你赢得汽车！')
    else:
        print('很遗憾你输了！')



if __name__ == '__main__':
    n = 0
    while(n<10):
        starting()
        yn = int(input('是否继续：'))
        if yn == 'y':
            n +=1
        else:
            break
