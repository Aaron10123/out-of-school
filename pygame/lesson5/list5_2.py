import tkinter as tk

masu = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 2],
]


def masume():
    for i in range(1, 3):
        cvs.create_line(0, i * 200, 600, i * 200, fill="gray", width=8)
        cvs.create_line(i * 200, 0, i * 200, 600, fill="gray", width=8)
    for y in range(3):
        for x in range(3):
            X = x * 200
            Y = y * 200
            if masu[y][x] == 1:
                cvs.create_oval(
                    X + 20, Y + 20, X + 180, Y + 180, outline="blue", width=12
                )
            elif masu[y][x] == 2:
                cvs.create_line(X + 20, Y + 20, X + 180, Y + 180, fill="red", width=12)
                cvs.create_line(X + 20, Y + 180, X + 180, Y + 20, fill="red", width=12)


root = tk.Tk()
root.title("Move Balloon")
root.resizable(False, False)
cvs = tk.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()
