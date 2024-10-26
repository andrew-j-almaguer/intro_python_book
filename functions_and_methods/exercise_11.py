# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# The code will print:
# 42
# 3
# 2

# We have passed foo only one argument instead of three. Since the second and
# third parameters have default values, Python uses them.