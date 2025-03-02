chinese = [
    "蘋果",
    "香蕉",
    "橘子",
    "梨子",
    "西瓜",
]  # 建立一個清單，裡面有五個中文水果名稱
english = [
    "apple",
    "banana",
    "orange",
    "pear",
    "watermelon",
]  # 建立一個清單，裡面有五個英文水果名稱
n = len(chinese)  # 計算清單中有幾個元素
right = 0
for i in range(n):  # 用迴圈依序列出清單中的元素
    a = input("請輸入" + chinese[i] + "的英文名稱：")  # 輸入中文水果名稱的英文名稱
    if a == english[i]:  # 判斷是否正確
        print("答對了")  # 如果是，則輸出答對了
        right = right + 1
    else:  # 否則
        print("答錯了")  # 輸出答錯了
        print("正確答案是：", english[i])
print("你總共答對了", right, "題")
print("你總共答錯了", n - right, "題")
