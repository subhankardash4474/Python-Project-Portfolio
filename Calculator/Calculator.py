from tkinter import *
import ast

root = Tk()
memory = 0
i = 0

def get_number(num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def clear_all():
    display.delete(0, END)

def is_valid_expression(expression):
    try:
        ast.parse(expression, mode='eval')
        return True
    except:
        return False

def calculate():
    entire_string = display.get()
    if is_valid_expression(entire_string):
        try:
            node = ast.parse(entire_string, mode="eval")
            result = eval(compile(node, '<string>', 'eval'))
            clear_all()
            display.insert(0, result)
        except Exception :
            clear_all()
            display.insert(0, "Error")
    else:
        clear_all()
        display.insert(0, "Invalid Input")

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")

def memory_add():
    global memory
    try:
        memory += float(display.get())
    except ValueError:
        pass

def memory_clear():
    global memory
    memory = 0

def memory_recall():
    clear_all()
    display.insert(0, memory)

def square_root():
    try:
        value = float(display.get())
        clear_all()
        display.insert(0, value ** 0.5)
    except ValueError:
        clear_all()
        display.insert(0, "Error")

def key_press(event):
    key = event.char
    if key.isdigit():
        get_number(key)
    elif key in ['+', '-', '*', '/', '%', '(', ')']:
        get_operation(key)
    elif key == '=' or key == '\r':  # Enter key
        calculate()
    elif key == '\x08':  # Backspace key
        undo()

root.bind("<Key>", key_press)

button_style = {
    'width': 5,
    'height': 2,
    'font': ('Helvetica', 14)
}

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, command=lambda text=button_text: get_number(text), **button_style)
        button.grid(row=x + 2, column=y)
        counter += 1

button = Button(root, text="0", command=lambda: get_number(0), **button_style)
button.grid(row=5, column=1)

Button(root, text="AC", command=lambda: clear_all(), **button_style).grid(row=5, column=0)
Button(root, text="=", command=lambda: calculate(), **button_style).grid(row=5, column=2)

Button(root, text="<-", command=lambda: undo(), **button_style).grid(row=5, column=4)

operations = ['+', '-', '*', '/', '%', '(', ')']
count = 0
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count], command=lambda text=operations[count]: get_operation(text), **button_style)
            count += 1
            button.grid(row=x + 2, column=y + 3)

Button(root, text="M+", command=memory_add, **button_style).grid(row=6, column=0)
Button(root, text="MC", command=memory_clear, **button_style).grid(row=6, column=1)
Button(root, text="MR", command=memory_recall, **button_style).grid(row=6, column=2)
Button(root, text="√", command=square_root, **button_style).grid(row=6, column=3)

root.mainloop()