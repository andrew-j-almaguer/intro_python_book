# Without running this code, what will it print? Why?
dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# This code will print:
# [1, 42, 3]
# By using the constructor call dict(dict1), we have created a new dict and
# assigned it to dict2. However, this is only a shallow copy, which means that
# nested objects are not duplicated, but still reference the nested objects
# from the original dict. Thus, mutating the values in the nested object of one
# dict will still affect the other.