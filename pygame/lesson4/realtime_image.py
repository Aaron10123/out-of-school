import tkinter as tk  # 匯入 tkinter 模組, 並使用 tk 作為別名

x = 300
y = 100
xp = 10


def animation():
    global x, xp
    x += xp
    if x <= 30:
        xp = 5
    if x >= 770:
        xp = -5
    cvs.delete("all")
    cvs.create_image(400, 200, image=bg)
    if xp < 0:
        cvs.create_image(x, y, image=ap1)
    if xp > 0:
        cvs.create_image(x, y, image=ap2)
    root.after(50, animation)


root = tk.Tk()  # 建立視窗物件
root.title("及時處裡2")  # 設定視窗標題
cvs = tk.Canvas(width=800, height=400)  # 建立畫布
cvs.pack()  # 顯示畫布
bg = tk.PhotoImage(file="pygame\lesson4/bg.png")
ap1 = tk.PhotoImage(file="pygame\lesson4/airplane1.png")
ap2 = tk.PhotoImage(file="pygame\lesson4/airplane2.png")
animation()  # 呼叫動畫函數
root.mainloop()  # 開始視窗的處理
