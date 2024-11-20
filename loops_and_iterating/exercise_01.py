# The following code causes an infinite loop (a loop that never stops
# iterating). Why?
counter = 0

while counter < 5:
    print(counter)

# The value of counter is never increased from 0, so the condition counter < 5
# forever remains truthy.