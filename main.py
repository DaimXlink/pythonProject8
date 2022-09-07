import tkinter as tk


def get_ent():
    asd = name.get()
    if asd:
        print(asd)
    else:
        print('Error')


def rty():
    name.delete(0, 'end')


root = tk.Tk()
root.title('calculator')
root.config(bg='gray')
root.geometry('720x500+650+0')
root.resizable(False, False)
tk.Label(root, text='Password').grid(row=0, column=0)
name = tk.Entry(root, show='*')
name.grid(row=0, column=2)
tk.Button(root, text='enter', command=get_ent).grid(row=1, column=0, sticky='w')
tk.Button(root, text='delete', command=rty).grid(row=2, column=0, sticky='w')
root.mainloop()
