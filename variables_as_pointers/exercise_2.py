# Without running this code, what will it print? Why?
set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)


# The code will print, in no particular order, the following list:
{42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}
# set1 and set2 reference the same set. Assigning a variable to another
# variable does not create any new objects, it just provides another pointer to
# the same object.