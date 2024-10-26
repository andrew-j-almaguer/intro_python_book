# Without running the following code, what do you think it will do?
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# This code will raise an error. We have passed foo one argument instead of
# three. The second parameter has a default value to use, but the third
# parameter does not. However, this code would raise an error with any number
# of arguments. Once a positional parameter has been assigned a default value,
# all subsequent parameters must have default values as well.