import tkinter as tk  # 匯入 tkinter 模組, 並使用 tk 作為別名

root = tk.Tk()  # 建立視窗物件
root.title("在畫布顯示字串")  # 設定視窗標題
cvs = tk.Canvas(width=600, height=400, bg="white")  # 建立畫布
cvs.create_text(
    300, 200, text="Hello would", font=("Times New Roman", 40)
)  # 在畫布上顯示字串
cvs.pack()  # 顯示畫布
root.mainloop()  # 開始視窗的處理
