import inflect

string = input()


def main(s):
    p = inflect.engine()

    s = s.split(":")
    temp = s[-1][-2:]

    if len(s) == 2:
        s[0] = int(s[0])
        s[1] = int(s[1][:-2])
    else:
        s[0] = int(s[0][:-2])

    if temp == "PM" and s[0] != 12:
        s[0] += 12
    elif temp == "AM" and s[0] == 12:
        s[0] += 12
        s[0] = s[0] % 24

    if len(s) == 1:
        return p.number_to_words(s[0]).replace("-", " ")

    res = ""
    # Adding hours
    res += (("zero " if s[0] < 10 and s[1] != 0 else "") +
            p.number_to_words(s[0]).replace("-", " "))
    # Adding minutes
    res += " hundred hours" if s[1] == 0 else (" zero " if s[1] < 10 else " ") + \
            p.number_to_words(s[1]).replace("-", " ")
    return res


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
