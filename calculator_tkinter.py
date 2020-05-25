from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width=60, borderwidth=1)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def button_click(num):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    elif math == 'substraction':
        e.insert(0, f_num - int(second_number))
    elif math == 'dividing':
        e.insert(0, f_num / int(second_number))
    elif math == 'multiplication':
        e.insert(0, f_num * int(second_number))

def button_dvd():
    first_number = e.get()
    global f_num
    global math
    math = 'dividing'
    f_num = int(first_number)
    e.delete(0, END)

def button_mltp():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)

def button_min():
    first_number = e.get()
    global f_num
    global math
    math = 'substraction'
    f_num = int(first_number)
    e.delete(0, END)


btn_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
btn_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
btn_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
btn_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
btn_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
btn_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
btn_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
btn_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
btn_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
btn_0 = Button(root, text='0', padx=135, pady=20, command=lambda: button_click(0))

btn_C = Button(root, text='C', padx=86.4, pady=20, command=lambda: button_clear())
btn_E = Button(root, text='=', padx=86, pady=20, command=lambda: button_equal())
btn_dvd = Button(root, text='/', padx=40, pady=20, command=lambda: button_dvd())
btn_mltp = Button(root, text='*', padx=40, pady=20, command=lambda: button_mltp())
btn_add = Button(root, text='+', padx=40, pady=20, command=lambda: button_add())
btn_min = Button(root, text='-', padx=40, pady=20, command=lambda: button_min())


btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_0.grid(row=5, column=0, columnspan=3)
btn_C.grid(row=1, column=0, columnspan=2)
btn_E.grid(row=1, column=2, columnspan=2)
btn_dvd.grid(row=2, column=3)
btn_mltp.grid(row=3, column=3)
btn_add.grid(row=4, column=3)
btn_min.grid(row=5, column=3)

root.mainloop()
