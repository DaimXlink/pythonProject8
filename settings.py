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
btn1 = tk.Button(root, text=f'+{i}',
                 command=qwe)
btn1.grid(row=2, column=2)
btn2 = tk.Button(root, text=f'+{i}',
                 command=qwe)
btn2.grid(row=2, column=3)
btn3 = tk.Button(root, text=f'+{i}',
                command=qwe)
btn3.grid(row=1, column=2)
btn4 = tk.Button(root, text=f'+{i}',
                 command=qwe)
btn4.grid(row=0, column=2)
btn5 = tk.Button(root, text=f'+{i}',
                 command=qwe)
btn5.grid(row=2, column=3)
root.mainloop()
