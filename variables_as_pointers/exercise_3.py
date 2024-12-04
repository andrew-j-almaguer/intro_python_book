# Without running this code, what will it print? Why?
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# The code will print:
# The Life of Brian

# This is because dict1 and dict2 are not the same dict. By using the
# constructor call dict(dict1), we created a new dict with the same key/value
# pairs as dict1. While initially dict1 and dict2 had identical values, they
# did not reference the same object, and so could be altered independently.