import tkinter as tk  # 匯入 tkinter 模組, 並使用 tk 作為別名

root = tk.Tk()  # 建立視窗物件
root.title("在畫布顯示圖形")  # 設定視窗標題
cvs = tk.Canvas(width=720, height=400, bg="black")  # 建立畫布
cvs.create_line(20, 40, 120, 360, fill="red", width=8)  # 畫直線
cvs.create_rectangle(160, 40, 260, 360, fill="orange")  # 畫矩形
cvs.create_oval(300, 100, 500, 300, outline="yellow", width=12)  # 畫圓
cvs.create_polygon(
    560, 40, 620, 360, 680, 40, fill="green", outline="lime", width=16  # 畫多邊形
)
cvs.pack()  # 顯示畫布
root.mainloop()  # 開始視窗的處理
