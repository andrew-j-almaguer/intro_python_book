# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])               # Empty

# This code returns 'Not Empty' if a list is truthy, or else 'Empty' if a list
# is falsy. Since empty lists are falsy, the else block runs, returning
# 'Empty'.