# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)      # Good Morning, Victor
print('Good Afternoon, ' + NAME)    # Good Afternoon, Victor
print('Good Evening, ' + NAME)      # Good Evening, Victor

NAME = 'Nina'
print('Good Morning, ' + NAME)      # Good Morning, Nina
print('Good Afternoon, ' + NAME)    # Good Afternoon, Nina
print('Good Evening, ' + NAME)      # Good Evening, Nina

# The program greets Victor three times, then Nina three times. Unfortunately,
# Python does not support true constants, and in this case, NAME does not act
# as a constant because it is reassigned mid-program, so using snake_case to
# denote a variable would be more appropriate.