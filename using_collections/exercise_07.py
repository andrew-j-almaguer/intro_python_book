# Write Python code to replace all the : characters in the string below with +.
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
# Try this problem using the methods you've learned about in this chapter. Once
# you have that working, use the Python documentation for the str type to find
# an alternative solution.

new_info = info.split(':')
new_info = '+'.join(new_info)
print(new_info)                     # xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh

alt_info = info.replace(':','+')
print(alt_info)                     # xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh