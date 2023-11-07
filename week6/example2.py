import tkinter as tk
from tkinter import Entry, Button, StringVar

class Example2:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('350x50')
        self.window.title('Example 2 in OOP')

        self.txt_input = Entry(self.window, width=10)
        self.txt_input.focus()
        self.txt_input.grid(row=0, column=0)

        self.btn_clickme = Button(self.window, text='Click Me', command=self.clicked)
        self.btn_clickme.grid(row=0, column=1)

        self.output = StringVar(self.window)
        txt_output = Entry(self.window, width=20, textvariable=self.output, state='readonly')
        txt_output.grid(row=0, column=2)

    def clicked(self):
        name = self.txt_input.get()
        self.output.set('Hello ' + name)

    def run(self):
        self.window.mainloop()

