# What does the following function do? Be sure to identify the output value.
def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))            # CHRIS

# The do_something function first obtains a list of the keys in a given dict,
# then sorts them, and returns an upper case version of the key at index [1].