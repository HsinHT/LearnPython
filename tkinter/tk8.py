from tkinter import *

root = Tk()

Label(root, text='帳號：').grid(row=0, column=0)
Label(root, text='密碼：').grid(row=1, column=0)

v1 = StringVar()
v2 = StringVar()
is_checked = BooleanVar()

def update_e2():
    global is_checked

    if is_checked.get():
        e2 = Entry(root, textvariable=v2)
    else:
        e2 = Entry(root, textvariable=v2, show='*')

    e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    print('帳號：%s' % e1.get())
    print('密碼：%s' % e2.get())

e1 = Entry(root, textvariable=v1)
e2 = Entry(root, textvariable=v2, show='*')
c1 = Checkbutton(root, text='顯示', variable=is_checked, command=update_e2)

e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
c1.grid(row=1, column=2, padx=10, pady=5)

Button(root, text='芝麻開門', width=10, command=show)\
             .grid(row=3, column=0, sticky=W, padx=10, pady=5)

Button(root, text='退出', width=10, command=root.quit)\
             .grid(row=3, column=2, sticky=E, padx=10, pady=5)

mainloop()
