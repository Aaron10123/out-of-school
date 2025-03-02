import tkinter as tk  # 匯入 tkinter 模組, 並使用 tk 作為別名

root = tk.Tk()  # 建立視窗物件
root.title("在畫布顯示圖片")  # 設定視窗標題
cvs = tk.Canvas(width=540, height=720)  # 建立畫布
dog = tk.PhotoImage(file="pygame\lesson4\shepherd.png")  # 讀取圖片檔案
cvs.create_image(270, 360, image=dog)  # 在畫布上顯示圖片
cvs.pack()  # 顯示畫布
root.mainloop()  # 開始視窗的處理
