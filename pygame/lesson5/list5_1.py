import tkinter as tk


def masume():
    # cvs.create_line(200, 0, 200, 600, fill="gray", width=8)
    # cvs.create_line(400, 0, 400, 600, fill="gray", width=8)
    # cvs.create_line(0, 200, 600, 200, fill="gray", width=8)
    # cvs.create_line(0, 400, 600, 400, fill="gray", width=8)
    for i in range(1, 3):
        cvs.create_line(0, i * 200, 600, i * 200, fill="gray", width=8)
        cvs.create_line(i * 200, 0, i * 200, 600, fill="gray", width=8)


root = tk.Tk()
root.title("Move Balloon")
root.resizable(False, False)
cvs = tk.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()
