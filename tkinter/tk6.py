from tkinter import *

root = Tk()

''' Test Code Part 1 '''
#v = IntVar()

#c = Checkbutton(root, text='測試一下', variable=v)
#c.pack()

#l = Label(root, textvariable=v)
#l.pack()

''' Test Code Part 2 '''
#GIRLS = ['西施', '貂蟬', '王昭君', '楊玉環']

#v = []

#for girl in GIRLS:
#    v.append(IntVar())
#    b = Checkbutton(root, text=girl, variable=v[-1])
#    b.pack(anchor=W)

''' Test Code Part 3 '''
#v = IntVar()

#Radiobutton(root, text='One', variable=v, value=1).pack(anchor=W)
#Radiobutton(root, text='Two', variable=v, value=2).pack(anchor=W)
#Radiobutton(root, text='Three', variable=v, value=3).pack(anchor=W)

''' Test Code Part 4 '''
#LANGS = [
#    ('Python', 1),
#    ('Perl', 2),
#    ('Ruby', 3),
#    ('Lua', 4)
#]

#v = IntVar()
#v.set(1)

#for lang, num in LANGS:
##    b = Radiobutton(root, text=lang, variable=v, value=num)
##    b.pack(anchor=W)
#
#    b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)
#    b.pack(fill=X)

''' Test Code Part 5 '''
group = LabelFrame(root, text='最好的腳本語言是？', padx=5, pady=5)
group.pack(padx=10, pady=10)

LANGS = [
    ('Python', 1),
    ('Perl', 2),
    ('Ruby', 3),
    ('Lua', 4)
]

v = IntVar()

for lang, num in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=num)
    b.pack(anchor=W)

mainloop()
