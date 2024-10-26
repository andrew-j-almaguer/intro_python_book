# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# The code will raise an error. We have passed foo zero arguments instead of
# three. With neither an argument nor a default value to work with, the first
# parameter raises an error.