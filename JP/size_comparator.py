measurement = input("Enter measurement in the format [number][units].\ne.g. 6ft:\n")

letters = list(measurement)
numbers = int(''.join([letter for letter in letters if letter.isnumeric()]))
units = ''.join([letter for letter in letters if letter.isalpha()])

# convert to metres
if units == 'ft':
    pass
elif units == 'in':
    pass
elif units == 'cm':
    pass
elif units == 'km':
    pass