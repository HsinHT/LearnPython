from tkinter import *

master = Tk()

theLB = Listbox(master)
theLB.pack()

items = ['雞蛋', '鴨蛋', '鵝蛋', '李狗蛋']

for item in items:
    theLB.insert(END, item)

theButton = Button(master, text='刪除', \
                   command=lambda x=theLB:x.delete(ACTIVE))
theButton.pack()

mainloop()
