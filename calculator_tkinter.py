from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Calculator')
root.iconbitmap('pics\icon.ico')

img_equal = ImageTk.PhotoImage(Image.open('pics\equal.png'))
img_c = ImageTk.PhotoImage(Image.open('pics\c.png'))
img_zero = ImageTk.PhotoImage(Image.open('pics\zero.png'))
img_dvd = ImageTk.PhotoImage(Image.open('pics\dvd.png'))
img_mltp = ImageTk.PhotoImage(Image.open('pics\mltp.png'))
img_add = ImageTk.PhotoImage(Image.open(r'pics\add.png'))
img_min = ImageTk.PhotoImage(Image.open('pics\min.png'))

img_one = ImageTk.PhotoImage(Image.open('pics\one.png'))
img_two = ImageTk.PhotoImage(Image.open(r'pics\two.png'))
img_three = ImageTk.PhotoImage(Image.open(r'pics\three.png'))
img_four = ImageTk.PhotoImage(Image.open(r'pics\four.png'))
img_five = ImageTk.PhotoImage(Image.open(r'pics\five.png'))
img_six = ImageTk.PhotoImage(Image.open('pics\six.png'))
img_seven = ImageTk.PhotoImage(Image.open('pics\seven.png'))
img_eight = ImageTk.PhotoImage(Image.open('pics\eight.png'))
img_nine = ImageTk.PhotoImage(Image.open(r'pics\nine.png'))


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

def button_dot(num):
    after_dot = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


btn_1 = Button(root, image=img_one, bg='black', command=lambda: button_click(1))
btn_2 = Button(root, image=img_two, bg='black', command=lambda: button_click(2))
btn_3 = Button(root, image=img_three, bg='black', command=lambda: button_click(3))
btn_4 = Button(root, image=img_four, bg='black', command=lambda: button_click(4))
btn_5 = Button(root, image=img_five, bg='black', command=lambda: button_click(5))
btn_6 = Button(root, image=img_six, bg='black', command=lambda: button_click(6))
btn_7 = Button(root, image=img_seven, bg='black', command=lambda: button_click(7))
btn_8 = Button(root, image=img_eight, bg='black', command=lambda: button_click(8))
btn_9 = Button(root, image=img_nine, bg='black', command=lambda: button_click(9))

btn_0 = Button(root, image=img_zero, bg='rosybrown', command=lambda: button_click(0))

btn_C = Button(root, image=img_c, bg='rosybrown', command=lambda: button_clear())
btn_E = Button(root, image=img_equal, bg='khaki', command=lambda: button_equal())

btn_dvd = Button(root, image=img_dvd, bg='rosybrown', command=lambda: button_dvd())
btn_mltp = Button(root, image=img_mltp, bg='rosybrown', command=lambda: button_mltp())
btn_add = Button(root, image=img_add, bg='rosybrown', command=lambda: button_add())
btn_min = Button(root, image=img_min, bg='rosybrown', command=lambda: button_min())

btn_dot = Button(root, text='.', command=lambda: button_dot())

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
#btn_dot.grid(row=6, column=0)

root.mainloop()
