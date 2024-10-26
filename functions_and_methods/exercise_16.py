# In the code shown below, identify all of the function names and parameters
# present in the code. Include the line numbers for each item identified.
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Functions:
# multiply: defined on line 3, used on line 11
# get_num: defined on line 6, used on lines 9 and 10
# float: built-in, used on line 7
# input: built-in, used on line 7
# print: built-in, used on line 12

# Parameters:
# left: defined on line 3, used on line 4
# right: defined on line 3, used on line 4
# prompt: defined on line 6, used on line 7