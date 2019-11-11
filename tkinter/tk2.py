import tkinter as tk

class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
#        frame.pack()
        frame.pack(side=tk.LEFT, padx=10, pady=10)

#        self.hi_there = tk.Button(frame, text='打招呼', fg='blue', command=self.say_hi)
        self.hi_there = tk.Button(frame, text='打招呼', bg='black', fg='white', command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print('Hello Button')


root = tk.Tk()
app = APP(root)

root.mainloop()
