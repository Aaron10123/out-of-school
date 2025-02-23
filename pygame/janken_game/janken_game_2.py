import random  # 匯入random模組

hand = ["石頭", "剪刀", "布"]  # 定義hand串列

for i in range(5):  # 重複五次
    print("第", i + 1, "局")  # 輸出第i+1局
    y = int(input("請出拳\n0石頭、1剪刀、2布"))  # 輸入出拳
    c = random.randint(0, 2)  # 隨機產生0~2的整數
    print("電腦出：", hand[c])  # 輸出電腦出的手勢
    if y != 0 and y != 1 and y != 2:
        print("請輸入0、1或2")
    elif y == c:  # 判斷是否平手
        print("平手")  # 輸出平手
    elif y == 0 and c == 1 or y == 1 and c == 2 or y == 2 and c == 0:  # 判斷是否玩家贏
        print("你贏了")  # 輸出你贏了
    else:  # 否則
        print("你輸了")  # 輸出你輸了
