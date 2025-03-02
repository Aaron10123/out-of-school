import tkinter

F = ("Times New Roman", 100)  # 字型設定
n = 0


def counter():  # 更新數字
    global n
    n += 1
    cvs.delete("all")
    cvs.create_text(270, 360, text=str(n), font=F, fill="blue")
    root.after(1000, counter)  # 每秒更新一次數字


root = tkinter.Tk()  # 建立視窗物件
root.title("即時顯示數字")  # 設定視窗標題
cvs = tkinter.Canvas(width=540, height=720, bg="white")  # 建立畫布
cvs.pack()  # 顯示畫布
counter()  # 呼叫更新數字函數
root.mainloop()  # 開始視窗的處理
