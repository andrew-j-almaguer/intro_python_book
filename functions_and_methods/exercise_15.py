# Using the code below, classify the identifiers as global, local, or built-in.
# For our purposes, you may assume this code is the entire program.
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Identifier        Class
# multiply          Global
# left              Local
# right             Local
# get_num           Global
# prompt            Local
# float             Built-in
# input             Built-in
# first_number      Global
# second_number     Global
# product           Global
# print             Built-in