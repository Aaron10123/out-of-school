import random  # 匯入random模組

hand = ["石頭", "剪刀", "布"]  # 定義hand串列

for i in range(5):  # 重複五次
    print("第", i + 1, "局")  # 輸出第i+1局
    c = random.randint(0, 2)  # 隨機產生0~2的整數
    print("電腦出：", hand[c])  # 輸出電腦出的手勢
