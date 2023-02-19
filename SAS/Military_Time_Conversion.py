import inflect

string = input()


def main(s):
    p = inflect.engine()

    s = s.split(":")
    half = s[-1][-2:] # Saves "AM" or "PM"

    # Converting strings to integers and removing AM/PM
    if len(s) == 2:
        s[0] = int(s[0])
        s[1] = int(s[1][:-2])
    else:
        s[0] = int(s[0][:-2])

    if half == "PM" and s[0] != 12:
        s[0] += 12
    elif half == "AM" and s[0] == 12:
        s[0] += 12
        s[0] = s[0] % 24

    # If format is "[number]AM/PM" return 1 word
    if len(s) == 1:
        return p.number_to_words(s[0]).replace("-", " ")

    # Adding hours
    # "zero" before number is omitted when exactly on the hour
    res = (("zero " if s[0] < 10 and s[1] != 0 else "") +
           p.number_to_words(s[0]).replace("-", " "))
    # Adding either "hundred hours" or minutes
    if s[1] == 0:
        return res + " hundred hours"
    return res + (" zero " if s[1] < 10 else " ") + \
        p.number_to_words(s[1]).replace("-", " ")


print(main(string))

assert main("12AM") == "zero"
assert main("7AM") == "seven"
assert main("1PM") == "thirteen"
assert main("11PM") == "twenty three"
assert main("4:00PM") == "sixteen hundred hours"
assert main("11:00AM") == "eleven hundred hours"
assert main("11:23AM") == "eleven twenty three"
assert main("6:45PM") == "eighteen forty five"
assert main("7:45AM") == "zero seven forty five"
assert main("5:05PM") == "seventeen zero five"
assert main("4:09AM") == "zero four zero nine"
