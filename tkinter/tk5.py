from tkinter import *

def callback():
    var.set('吹吧你！我才不信呢！')


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('您所下載的影片含有未成人限制內容，請滿18周歲後再點擊觀看！')

textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='imgs/18-stop.png')
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text='我已滿 18 周歲', command=callback)

theButton.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()
