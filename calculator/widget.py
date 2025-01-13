import tkinter as tk
import re
from functools import partial
import math



def add( x, y):
    try: 
        x = int(x)
        y = int(y)
        z = x + y 
        return z
    except ValueError as a:
        return f"Error: Invalid input.{a}."
def subtract(x, y):
    try:
        x = int(x)
        y = int(y)
        z = x - y
        return z
    except ValueError as a:
        return f"Error : {a}"
def multiply(x , y):
    try:
        x = int(x)
        y = int(y)
        return x * y
    except ValueError as z :
        return f"Error: {z}."
    
def divide( x, y):
    try:
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError as z:
        return f"Error: {z}"
    
def power(x, y):
    try: 
        if x == 0:
            return 0
        elif y == 0:
            return 1
        else:
            return math.pow(x,y)
        
    except ValueError as z:
        return f"Error: {z}"
        

# Function to solve mathematical expressions with custom operators
def solve(expression, operator):
    num1, num2 = map(int, expression.split(operator))
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    elif operator == '^':
        return power(num1, num2)

def process_operation(expression, op_regex, operator):
    match = re.search(op_regex, expression)
    while match:
        full_match = match.group(0)
        result = solve(full_match, operator)
        expression = expression.replace(full_match, str(result), 1)
        match = re.search(op_regex, expression)
    return expression

def custom_calculate(expression_var):
    expression = expression_var.get()
    expression = re.sub(r'\s+', '', expression)  # Remove any whitespace

    operations = {
        '^': r'(\d+)\^(\d+)',
        '*': r'(\d+)\*(\d+)',
        '/': r'(\d+)/(\d+)',
        '+': r'(\d+)\+(\d+)',
        '-': r'(\d+)-(\d+)',
    }

    try:
         
        while any(op in expression for op in '^*/+-'):
            for operator in '^*/+-':
                if operator in expression:
                    expression = process_operation(expression, operations[operator], operator)
                    expression_var.set(expression)
    except:
        expression_var.set("Error")

def press_key(exp, key):
    exp.set(exp.get() + str(key))

def clear(exp):
    exp.set("")

# GUI Setup
root = tk.Tk()
root.title("Calculator")
exp = tk.StringVar()
entry = tk.Entry(root, textvariable=exp, font=('Arial', 20), bd=10, insertwidth=4, width=14, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button Layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('^', 5, 0),
]

for (text, row, col) in buttons:
    if text == '=':
        action = partial(custom_calculate, exp)
    elif text == 'C':
        action = partial(clear, exp)
    else:
        action = partial(press_key, exp, text)
    
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=action)
    button.grid(row=row, column=col)
    button.config(bg="lightblue")

root.mainloop()