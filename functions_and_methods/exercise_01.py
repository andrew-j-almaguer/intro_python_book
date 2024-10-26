# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# This code returns an error: NameError: name 'foo' is not defined.
# This is because 'foo' is assigned inside the function set_foo() and,
# therefore, is not in scope when executing code outside of that function.