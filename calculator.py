import tkinter as tk


def de():
    q = 2
    asd = zxc.get()
    zxc.delete(zxc.index(tk.END) - 1)
    q -= 1


def dell(dels):
    return tk.Button(text=dels, bd=5, command=lambda: de(), font=('Comic sans', 11))


def all_del():
    asd = zxc.get()
    zxc.delete(0, tk.END)


def sus(qwe):
    return tk.Button(text=qwe, bd=5, command=lambda: all_del(), font=('Comic sans', 11))


def calculate():
    asd = zxc.get()
    zxc.delete(0, tk.END)
    zxc.insert(0, eval(asd))


def op(dit):
    asd = zxc.get()
    if asd[-1] in '-+/*.':
        asd = asd[:-1]
    zxc.delete(0, tk.END)
    zxc.insert(0, asd+dit)


def calc_b(oper):
    return tk.Button(text=oper, bd=5, command=lambda: op(oper), font=('Comic sans', 11))


def add_num(n):
    asd = zxc.get() + str(n)
    zxc.delete(0, tk.END)
    zxc.insert(0, asd)


def add_but(n):
    return tk.Button(text=n, command=lambda: add_num(n))


def add_end(n):
    return tk.Button(text=n, bd=5, font=('Comic sans', 11), command=calculate)


root = tk.Tk()
root.title('calculator')
root.config(bg='gray')
root.geometry(f'344x360+100+200')
zxc = tk.Entry(root, bd=10, justify=tk.RIGHT, font=('Comic sans', 11), width=20)
zxc.grid(row=0, column=0, columnspan=3)
add_but('1').grid(row=1, column=0, sticky='wens')
add_but('2').grid(row=1, column=1, sticky='wens')
add_but('3').grid(row=1, column=2, sticky='wens')
add_but('4').grid(row=2, column=0, sticky='wens')
add_but('5').grid(row=2, column=1, sticky='wens')
add_but('6').grid(row=2, column=2, sticky='wens')
add_but('7').grid(row=3, column=0, sticky='wens')
add_but('8').grid(row=3, column=1, sticky='wens')
add_but('9').grid(row=3, column=2, sticky='wens')
add_but('0').grid(row=4, column=3, sticky='wens')

add_end('=').grid(row=1, column=3, sticky='wens')

calc_b('/').grid(row=2, column=3, sticky='wens')

sus('C').grid(row=0, column=3, sticky='wens')
dell('del').grid(row=0, column=4, sticky='wens')

calc_b('*').grid(row=3, column=3, sticky='wens')
calc_b('+').grid(row=4, column=0, sticky='wens')
calc_b('-').grid(row=4, column=1, sticky='wens')
calc_b('.').grid(row=4, column=2, sticky='wens')

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)
root.mainloop()
# 14.08.2022
