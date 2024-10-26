# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# This code will print:

# 42
# 3.141592
# 2.718

# We have defined foo with three parameters, including two default ones. In
# this case, we have passed foo three arguments, so the defult values are
# ignored.