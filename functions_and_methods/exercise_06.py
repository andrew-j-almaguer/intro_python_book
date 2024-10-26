# What does the following code print?
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# The code prints nothing. The return on line 4 terminates the function and any
# subsequent code is disregarded.