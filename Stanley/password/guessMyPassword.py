# keylog.txt
# guess shortest possible password by analysing text file
from bisect import bisect


def read_in_file(fname):
    keylog = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            keylog.append(line.strip())

    return keylog


def remove_elt(appears_after, elt_to_remove):
    # propagate guess, remove digits that are confirmed from dict
    for k in appears_after:
        if elt_to_remove in appears_after[k]:
            appears_after[k].remove(elt_to_remove)

    return appears_after


def decode(keylog):
    # for each elt in keylog
    # we know which position numbers must be relative to each other
    # e.g. 317 => 3 is before 1 is before 7
    guess = ''

    # get list of every number that appears after x
    appears_after = {}
    for elt in keylog:
        for i, n in enumerate(elt):
            if i != 0:
                if n not in appears_after:
                    appears_after[n] = set([elt[i-1]])
                else:
                    appears_after[n].add(elt[i-1])

    # debugging comments
    # [print(elt) for elt in keylog]
    # [print(f'{k}: {v}') for k, v in appears_after.items()]

    # find smallest set and propagate down
    # by removing numbers that are accounted for in the guess

    # to find first digit, find number that is in keylog
    # but not in dict
    # since if a digit does not appear after any number,
    # that digit is first
    for i in range(9):
        in_keylog = False
        for elt in keylog:
            if str(i) in elt:
                in_keylog = True
        
        if in_keylog and str(i) not in list(appears_after.keys()):
            guess += str(i)

    # repeat until all sets are empty
    all_empty = False
    while not all_empty:
        all_empty = True

        # next digit is digit that appears only after previous, and nothing else
        for k in appears_after:
            if len(appears_after[k]) == 1 and appears_after[k] == {guess[-1]}:
                guess += k

        appears_after = remove_elt(appears_after, guess[-2])
        
        for k in appears_after:
            if len(appears_after[k]) != 0:
                all_empty = False

    return guess



def main():
    keylog = read_in_file("./Stanley/keylog.txt")
    guess = decode(keylog)
    print(guess)


if __name__ == "__main__":
    main()