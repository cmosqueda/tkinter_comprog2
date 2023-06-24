from tkinter import *

def on_select(event):
    selected_item = listbox.get(listbox.curselection())
    print('Selected item', selected_item)


def run():
    root = Toplevel()

    listbox. Listbox(root)
    listbox.pack()

    listbox.insert(END, 'Item 1')
    listbox.insert(END, 'Item 2')
    listbox.insert(END, 'Item 3')
    listbox.insert(END, 'Item 4')

    listbox.bind('<<ListboxSelect>>', on_select)

    root.mainloop()