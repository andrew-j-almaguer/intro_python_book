# Assume that obj already has a value of 42 when the code below starts running.
# Which of the subsequent statements reassign the variable? Which statements
# mutate the value of the object that obj references? Which statements do
# neither? If necessary, you can read the documentation.

obj = 'ABcd'            # Reassigns
obj.upper()             # Neither
obj = obj.lower()       # Reassigns
print(len(obj))         # Neither
obj = list(obj)         # Reassigns
obj.pop()               # Mutates
obj[2] = 'X'            # Mutates
obj.sort()              # Mutates
set(obj)                # Neither
obj = tuple(obj)        # Reassigns