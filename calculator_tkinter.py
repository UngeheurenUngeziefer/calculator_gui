from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Calculator')
root.iconbitmap(r'pics\icon.ico')

# button icons
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
img_dot = ImageTk.PhotoImage(Image.open('pics\dot.png'))
img_plus_minus = ImageTk.PhotoImage(Image.open('pics\plus_minus.png'))
img_1_x = ImageTk.PhotoImage(Image.open(r'pics\1_x.png'))
img_x_2 = ImageTk.PhotoImage(Image.open(r'pics\x_2.png'))
img_x_3 = ImageTk.PhotoImage(Image.open(r'pics\x_3.png'))
img_2root_x = ImageTk.PhotoImage(Image.open(r'pics\2root_x.png'))

# enter field
root.configure(background='black')

e = Entry(root, width=13, bg='black', fg='white', justify='right', \
		  font="Arial 40 bold", borderwidth=0, highlightthickness=0)
e.pack(pady=50)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
root.minsize(300, 400)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)


# buttons functions
def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


def button_clear():
    e.delete(0, END)


def operation_buttons(func_button):
    def wrapper():
        first_number = e.get()
        global f_num
        func_button()
        f_num = first_number
        e.delete(0, END)
    return wrapper


@operation_buttons
def button_add():
    global math
    math = 'addition'


@operation_buttons
def button_dvd():
    global math
    math = 'dividing'


@operation_buttons
def button_mltp():
    global math
    math = 'multiplication'


@operation_buttons
def button_min():
    global math
    math = 'substraction'


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addition':
        if '.' in f_num or '.' in second_number:
            e.insert(0, float(f_num) + float(second_number))
        else:
            e.insert(0, int(f_num) + int(second_number))
    elif math == 'substraction':
        if '.' in f_num or '.' in second_number:
            e.insert(0, float(f_num) - float(second_number))
        else:
            e.insert(0, int(f_num) - int(second_number))
    elif math == 'dividing':
        if float(second_number) == 0:
            e.insert(0, str('Cannot divide by zero‬'))
        else:
            if '.' in f_num or '.' in second_number:
                e.insert(0, float(f_num) / float(second_number))
            else:
                e.insert(0, int(f_num) / int(second_number))
    elif math == 'multiplication':
        if '.' in f_num or '.' in second_number:
            e.insert(0, float(f_num) * float(second_number))
        else:
            e.insert(0, int(f_num) * int(second_number))


def plus_min():
    current = e.get()
    e.delete(0, END)
    if current[0] == '-':
        e.insert(0, str(current)[1:])
    else:
        e.insert(0, str('-') + str(current))


def one_dvd_x():
    current = e.get()
    e.delete(0, END)
    result = 1 / float(current)
    if result == int(result):
        e.insert(0, int(result))
    else:
        e.insert(0, result)


def x_2():
    current = e.get()
    e.delete(0, END)
    result = float(current)**2
    if result == int(result):
        e.insert(0, int(result))
    else:
        e.insert(0, result)


def x_3():
    current = e.get()
    e.delete(0, END)
    result = float(current)**3
    if result == int(result):
        e.insert(0, int(result))
    else:
        e.insert(0, result)


def sq_root():
    current = e.get()
    e.delete(0, END)
    if float(current) < 0:
        e.insert(0, str('Invalid input'))
    else:
        result = float(current) ** 0.5
        if result == int(result):
            e.insert(0, int(result))
        else:
            e.insert(0, result)


def key(event=None):
    button_click(event.char)
    try:
        button_name = 'btn_' + str(event.char)
        if button_name == 'btn_.':
            button_name = 'btn_dot'
        button_name = eval(button_name)
        button_name.config(bg='white')
        root.after(100, lambda: button_name.config(bg='black'))
    except NameError:
        pass


def backspace(event=None):
    btn_C.config(bg='white')
    root.after(100, lambda: btn_C.config(bg='salmon'))
    button_clear()


def equal(event=None):
    btn_E.config(bg='white')
    root.after(100, lambda: btn_E.config(bg='khaki'))
    button_equal()


def addition(event=None):
    btn_add.config(bg='white')
    root.after(100, lambda: btn_add.config(bg='gray'))
    button_add()


def minus(event=None):
    btn_min.config(bg='white')
    root.after(100, lambda: btn_min.config(bg='gray'))
    button_min()


def divide(event=None):
    btn_dvd.config(bg='white')
    root.after(100, lambda: btn_dvd.config(bg='gray'))
    button_dvd()


def multiple(event=None):
    btn_mltp.config(bg='white')
    root.after(100, lambda: btn_mltp.config(bg='gray'))
    button_mltp()

root.bind("<Key>", key)
root.bind("<BackSpace>", backspace)
root.bind("<plus>", addition)
root.bind("<minus>", minus)
root.bind("</>", divide)
root.bind("<*>", multiple)
root.bind("<=>", equal)
root.bind("<Return>", equal)

# buttons
btn_1 = Button(root, image=img_one, bg='black', command=lambda: button_click(1))
btn_2 = Button(root, image=img_two, bg='black', command=lambda: button_click(2))
btn_3 = Button(root, image=img_three, bg='black', command=lambda: button_click(3))
btn_4 = Button(root, image=img_four, bg='black', command=lambda: button_click(4))
btn_5 = Button(root, image=img_five, bg='black', command=lambda: button_click(5))
btn_6 = Button(root, image=img_six, bg='black', command=lambda: button_click(6))
btn_7 = Button(root, image=img_seven, bg='black', command=lambda: button_click(7))
btn_8 = Button(root, image=img_eight, bg='black', command=lambda: button_click(8))
btn_9 = Button(root, image=img_nine, bg='black', command=lambda: button_click(9))
btn_0 = Button(root, image=img_zero, bg='black', command=lambda: button_click(0))
btn_C = Button(root, image=img_c, bg='salmon', command=lambda: button_clear())
btn_E = Button(root, image=img_equal, bg='khaki', command=lambda: button_equal())
btn_dvd = Button(root, image=img_dvd, bg='gray', command=lambda: button_dvd())
btn_mltp = Button(root, image=img_mltp, bg='gray', command=lambda: button_mltp())
btn_add = Button(root, image=img_add, bg='gray', command=lambda: button_add())
btn_min = Button(root, image=img_min, bg='gray', command=lambda: button_min())
btn_dot = Button(root, image=img_dot, bg='black', command=lambda: button_click('.'))
btn_plus_min = Button(root, image=img_plus_minus, bg='black', command=lambda: plus_min())
btn_one_dvd_x = Button(root, image=img_1_x, bg='cornflowerblue', command=lambda: one_dvd_x())
btn_sq_root = Button(root, image=img_2root_x, bg='cornflowerblue', command=lambda: sq_root())
btn_x_2 = Button(root, image=img_x_2, bg='cornflowerblue', command=lambda: x_2())
btn_x_3 = Button(root, image=img_x_3, bg='cornflowerblue', command=lambda: x_3())


# grid location
btn_C.grid(row=1, column=0, columnspan=2, sticky="nsew")
btn_E.grid(row=1, column=2, columnspan=2, sticky="nsew")

btn_one_dvd_x.grid(row=2, column=0, sticky="nsew")
btn_x_2.grid(row=2, column=1, sticky="nsew")
btn_x_3.grid(row=2, column=2, sticky="nsew")
btn_sq_root.grid(row=2, column=3, sticky="nsew")

btn_7.grid(row=3, column=0, sticky="nsew")
btn_8.grid(row=3, column=1, sticky="nsew")
btn_9.grid(row=3, column=2, sticky="nsew")
btn_dvd.grid(row=3, column=3, sticky="nsew")

btn_4.grid(row=4, column=0, sticky="nsew")
btn_5.grid(row=4, column=1, sticky="nsew")
btn_6.grid(row=4, column=2, sticky="nsew")
btn_mltp.grid(row=4, column=3, sticky="nsew")

btn_1.grid(row=5, column=0, sticky="nsew")
btn_2.grid(row=5, column=1, sticky="nsew")
btn_3.grid(row=5, column=2, sticky="nsew")
btn_add.grid(row=5, column=3, sticky="nsew")

btn_plus_min.grid(row=6, column=0, sticky="nsew")
btn_0.grid(row=6, column=1, sticky="nsew")
btn_dot.grid(row=6, column=2, sticky="nsew")
btn_min.grid(row=6, column=3, sticky="nsew")

root.mainloop()
