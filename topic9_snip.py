from tkinter import *

def file_new():
    print('New File')

def file_open():
    print('Open File')

def file_save():
    print('File save')

def file_exit():
    root.quit()


def run():
    root = Toplevel()

    menubar = Menu(root)

    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label='New', command=file_new)
    file_menu.add_command(label='Open', command=file_open)
    file_menu.add_command(label='Save', command=file_save)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=file_exit)

    menubar.add_cascade(label='File', menu=file_menu)

    root.config(menu=menubar)

    root.mainloop()