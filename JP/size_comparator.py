measurement = input("Enter measurement in the format [number][units].\ne.g. 6ft:\n")

letters = list(measurement)
numbers = int(''.join([letter for letter in letters if letter.isnumeric()]))
units = ''.join([letter for letter in letters if letter.isalpha()])

# convert to metres
if units == 'ft':
    conv_units = numbers / 3.281
elif units == 'in':
    conv_units = (numbers / 12) / 3.281
elif units == 'cm':
    conv_units = numbers / 100
elif units == 'km':
    conv_units = numbers * 1000
else:
    conv_units = numbers


# all in metres
COMPARISONS = {
    'Gilbert Scott Building': 84.7344,
    'Titanic': 269,
    'average height of UK males': 1.759,
    'height of a brown bear': 1.5,
    'caterpillar': 0.14,
    'Universe': 8.8 * 10**26
}

for k in COMPARISONS:
    print(f"Given measurement is approximately {round(conv_units / COMPARISONS[k], 4)} times as long as the {k}")