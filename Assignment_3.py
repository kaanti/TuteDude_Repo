# Task 1

def factorial(num):

    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input('Enter a number:'))
print(f"The factorial of {num} is {factorial(num)}")

Task 2

import math

num = int(input('Enter a number:'))

print('Square root:', math.sqrt(num))
print('Logarithm:', math.log(num))
print('Sine:', math.sin(num))