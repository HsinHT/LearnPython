from tkinter import *

master = Tk()

''' Test Code Part 1 '''
#v = StringVar()

#def test1():
#    if v.get() == '小甲魚':
#        print('正確！')
#        return True
#    else:
#        print('錯誤！')
#        return False

#def test2():
#    print('我被調用了...')
#    return True


#e1 = Entry(master, textvariable=v, validate='focusout', \
#           validatecommand=test1, invalidcommand=test2)
#e2 = Entry(master)

#e1.pack(padx=10, pady=10)
#e2.pack(padx=10, pady=10)

''' Test Code Part 2 '''
v = StringVar()

def test(content, reason, name):
    if content == '小甲魚':
        print('正確！')
        print(content, reason, name)
        return True
    else:
        print('錯誤！')
        print(content, reason, name)
        return False

testCMD = master.register(test)
e1 = Entry(master, textvariable=v, validate='focusout', \
           validatecommand=(testCMD, '%P', '%v', '%W'))
e2 = Entry(master)

e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)

mainloop()
