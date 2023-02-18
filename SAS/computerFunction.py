def pad_left(l, x):
    if len(x) < l:
        return ('0' * (l - len(x))) + x
    return x


def computer_function(a, b):
    # convert both to binary
    # add them together, but do not carry
    # i.e. 1 + 1 goes to 0, not 10
    bin_a, bin_b = str(bin(a))[2:], str(bin(b))[2:]
    # pad string so that they are same length
    l = max(len(bin_a), len(bin_b))

    bin_a = pad_left(l, bin_a)
    bin_b = pad_left(l, bin_b)

    res = ''
    for i in range(len(bin_a)):
        if bin_a[i] == bin_b[i]:
            # if they are the same, result is 0 regardless
            res += '0'
        else:
            res += '1'

    print(bin_a, bin_b)
    print(res)

    return int(res, 2)


x1 = computer_function(10, 20)
x2 = computer_function(17, 35)
x3 = computer_function(61, 233)

print(f'''
COMPUTERFUNCTION(10, 20) => {x1}
COMPUTERFUNCTION(17, 35) => {x2}
COMPUTERFUNCTION(61, 233) => {x3}
''')