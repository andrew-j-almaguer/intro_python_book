# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# This code will print:
# 42
# 3.141592
# 2

# We have passed foo two arguments instead of three. Since the third parameter
# has a default value, Python uses it.