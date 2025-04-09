"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    answer = a + b
    return answer
def sub(a, b):
    answer = a - b
    return answer
def mul(a, b):
    answer = a * b
    return answer
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a
def log(a, b):
    if b < 0:
        return ValueError
    return math.log(a, b)
def exp(a, b):
    answer = a ** b
    return answer

def square_root(a):
    if a < 0:
        return ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)







