import tkinter as tk

FNT = ("Times New Roman", 40)


def motion(e):
    cvs.delete("all")
    s = "座標: (" + str(e.x) + "," + str(e.y) + ")"
    cvs.create_text(200, 200, text=s, font=FNT)


root = tk.Tk()
root.title("Event Motion")
cvs = tk.Canvas(width=400, height=400, bg="white")
cvs.bind("<Motion>", motion)
cvs.pack()
root.mainloop()
