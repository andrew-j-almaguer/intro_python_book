# Use the REPL and the arithmetic operators to extract the individual digits
# of 4936:

number = 4936
print(f'For number {number}')
ones = number % 10
print(f'One place is {ones}')               # 6

number = number // 10
tens = number % 10
print(f'Tens place is {tens}')              # 3

number = number // 10
hundreds = number % 10
print(f'Hundreds place is {hundreds}')      # 9

thousands = number // 10
print(f'Thousands place is {thousands}')    # 4