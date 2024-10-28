# Refactor this statement to use a regular if statement instead.
return ('bar' if foo() else qux())

# Solution:
if foo():
    return 'bar'
else:
    return qux()