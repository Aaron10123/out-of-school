import tkinter as tk
import random
import time

masu = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
shirushi = 0


def masume():
    cvs.delete("all")
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
    cvs.update()


def click(event):
    global shirushi
    mx = int(event.x / 200)
    my = int(event.y / 200)
    if mx > 2:
        mx = 2
    if my > 2:
        my = 2
    if masu[my][mx] == 0:
        masu[my][mx] = 1
        shirushi += 1
    masume()
    time.sleep(0.5)
    if shirushi < 9:
        computer()


def computer():
    global shirushi
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if masu[y][x] == 0:
            masu[y][x] = 2
            shirushi += 1
            masume()
            time.sleep(0.5)
            break


root = tk.Tk()
root.title("Move Balloon")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()
