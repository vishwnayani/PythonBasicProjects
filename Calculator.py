from tkinter import *

def button_press(nums):
    global equation_text
    equation_text = equation_text + str(nums)
    equation_label.set(equation_text)
def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)
def equal():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("cant divide by zero")
    except SyntaxError:
        equation_label.set("Syntax Error")

window = Tk()
window.title('Calculator')
window.geometry('500x500')

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable = equation_label, font = ('Consolas', 20), width = 24, height=2, bg = 'white')
label.pack()

frame = Frame(window)
frame.pack()

b1 = Button(frame, text = '1', width = 6, height = 3, font = 35, command  = lambda: button_press(1))
b1.grid(row = 0, column = 0)
b2 = Button(frame, text = '2', width = 6, height = 3, font = 35, command  = lambda: button_press(2))
b2.grid(row = 0, column = 1)
b3 = Button(frame, text = '3', width = 6, height = 3, font = 35, command  = lambda: button_press(3))
b3.grid(row = 0, column = 2)
b4 = Button(frame, text = '4', width = 6, height = 3, font = 35, command  = lambda: button_press(4))
b4.grid(row = 1, column = 0)
b5 = Button(frame, text = '5', width = 6, height = 3, font = 35, command  = lambda: button_press(5))
b5.grid(row = 1, column = 1)
b6 = Button(frame, text = '6', width = 6, height = 3, font = 35, command  = lambda: button_press(6))
b6.grid(row = 1, column = 2)
b7 = Button(frame, text = '7', width = 6, height = 3, font = 35, command = lambda: button_press(7))
b7.grid(row = 2, column = 0)
b8 = Button(frame, text = '8', width = 6, height = 3, font = 35, command = lambda: button_press(8))
b8.grid(row = 2, column = 1)
b9 = Button(frame, text = '9', width = 6, height = 3, font = 35, command = lambda: button_press(9))
b9.grid(row = 2, column = 2)
b0 = Button(frame, text = '0',width = 6, height = 3, font = 35, command = lambda: button_press(0))
b0.grid(row = 3, column = 0)

plus = Button(frame, text = '+', width = 6, height = 3, font = 35, command = lambda: button_press('+'))
plus.grid(row = 0, column = 3)
minus = Button(frame, text = '-', width = 6, height = 3, font = 35, command = lambda: button_press('-'))
minus.grid(row = 1, column = 3)
divide = Button(frame, text = '/', width = 6, height = 3, font = 35, command = lambda: button_press('/'))
divide.grid(row = 2, column = 3)
multiply = Button(frame, text = '*', width = 6, height = 3, font = 35, command = lambda: button_press('*'))
multiply.grid(row = 3, column = 3)

decimal = Button(frame, text = '.', width = 6, height = 3, font = 35, command = lambda: button_press('.'))
decimal.grid(row = 3, column = 1)
equal = Button(frame, text = '=', width = 6, height = 3, font = 35, command = equal)
equal.grid(row = 3, column = 2)

clear = Button(window, text = 'clear', width = 9, height = 3, font = 35, command = clear)
clear.pack()

window.mainloop()
