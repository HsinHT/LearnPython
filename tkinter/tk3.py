from tkinter import *

root = Tk()

textLabel = Label(root,
                  text='您所下載的影片含有未成人限制內容，請滿18周歲後再點擊觀看！',
                  justify=LEFT,
                  padx=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='imgs/18-stop.png')
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)

mainloop()
