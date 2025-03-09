import tkinter as tk

root = tk.Tk()
root.title("Canvas Text")
cvs = tk.Canvas(root, width=400, height=400)
cvs.create_text(200, 200, text="請投給我", font=("Arial", 24))
cvs.pack()
root.mainloop()
