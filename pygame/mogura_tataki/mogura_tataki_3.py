import time
import random


def mogura(r):
    m = ""
    n = ""
    for i in range(5):
        ana = "."
        if i == r:
            ana = "O"
        m = m + " _" + ana + "_ "
        n = n + " |" + str(i) + "| "
    print(m)
    print(n)


print("歡迎來到打地鼠遊戲")
print("請在地鼠出現的位置輸入數字來打地鼠")
print("============遊戲開始============")
hit = 0
ts = time.time()
for i in range(10):
    r = random.randint(0, 4)
    mogura(r)
    a = int(input("請輸入位置："))
    if a == r:
        print("打到了")
        hit = hit + 1
    else:
        print("沒打到")
t = int(time.time() - ts)
bonus = 0
if t < 60:
    bonus = 60 - t
print("============遊戲結束============")
print("TIME", t, "sec")
print("HIT", hit, "*BONUS", bonus)
print("SCORE", hit * bonus)
