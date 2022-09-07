import tkinter as tk
import random

i = 0
col = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
v = random.randint(1, 5)


def qwe():
    global v
    global i
    i += 1
    v = random.randint(1, 5)
    root.config(bg=col[v])
    btn['text'] = f'+{i}'


root = tk.Tk()
root.title('calculator')
root.config(bg='red')
root.geometry('720x500+650+0')
root.resizable(False, False)
btn = tk.Button(root, text=f'+{i}',
                command=qwe)
btn.grid(row=2, column=1)
root.mainloop()
