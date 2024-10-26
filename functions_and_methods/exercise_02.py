# Take a look at this code snippet:
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
# What does this program print? Why?

# This program prints 'bar'. This is because 'foo' was assigned to 'bar' in
# line 2 of the code. The assignment of 'foo' on line 5 is local to the
# function set_foo(), and does not apply outside of executing that function.
# As such, this is not a reassignment, but a shadowing.