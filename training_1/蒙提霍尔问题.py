import random
def sanmen_simulation(trials):  #1个用法
    win_no_switch = 0
    win_switch =0
    for _ in range(trials):
        car_door =random.randint(1,3)
        player_choice=random.randint(1,3)
        host_options = [door for door in [1,2,3] if door != car_door and door != player_choice]
        host_open =random.choice(host_options)
        switch_choice = [door for door in [1,2,3] if door != player_choice and door != host_open][0]
        if player_choice == car_door:
            win_no_switch +=1
        if switch_choice ==car_door:
            win_switch += 1
    return win_no_switch,win_switch


if __name__ == '__main__':
    while True:
        try:
            trials = int(input("请输入蒙提霍尔问题的实验次数(正整数):"))
            if trials > 0:
                break
            else:
                print("输入错误!请输入正整数。")
        except ValueError:
            print("输入错误!请输入有效的整数。")
    no_switch_win, switch_win = sanmen_simulation(trials)
    prob_no_switch =no_switch_win /trials
    prob_switch=switch_win /trials
    print("\n===== 模拟结果 ======")
    print(f"总实验次数:{trials}")
    print(f"不换门中奖次数:{no_switch_win}，中奖概率:{prob_no_switch:.2%}")
    print(f"换门中奖次数:{switch_win}，中奖概率:{prob_switch:.2%}")