from tkinter import *

root = Tk()

photo = PhotoImage(file='imgs/bg.png')
theLabel = Label(root,
                 text='學習 Pytho 真好玩',
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=('標楷體', 20),
                 fg='blue')
theLabel.pack()

mainloop()
