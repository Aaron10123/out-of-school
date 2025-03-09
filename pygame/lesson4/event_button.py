import tkinter as tk

n = 0


def click(e):
    global n
    n += 1
    if n == 3:
        n = 0
    cvs.delete("all")
    if n == 0:
        cvs.create_oval(200, 100, 400, 300, fill="green")
    if n == 1:
        cvs.create_rectangle(200, 100, 400, 300, fill="blue")
    if n == 2:
        cvs.create_polygon(200, 100, 400, 300, 300, 100, fill="red")


root = tk.Tk()
root.title("Event Button")
root.bind("<Button>", click)
cvs = tk.Canvas(width=600, height=400, bg="white")
cvs.create_text(300, 200, text="按滑鼠左鍵有驚喜!", font=("Arial", 24))
cvs.pack()
root.mainloop()
