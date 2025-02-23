import time

print("計時開始")  # 輸出計時開始
ts = time.time()  # 將這個時間的epoch秒數存到ts
print("epoch秒數", ts)  # 輸出ts
input("請按Enter鍵結束")  # 利用input()命令等待使用者按下Enter鍵
te = time.time()  # 將這個時間的epoch秒數存到te
print("epoch秒數", te)  # 輸出te
print("計時結束")  # 輸出計時結束
print("經過時間", int(te - ts), "秒")  # 輸出經過時間
