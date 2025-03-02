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
for i in range(n):  # 用迴圈依序列出清單中的元素
    print(chinese[i], ":", english[i])  # 列出中英文水果名稱
