# how many rolls it would take to visit every square on a monopoly board
from random import randint
from matplotlib import pyplot as plt

def monopoly():
    # create representation of board
    # False means square is not landed on
    # start on first square, so first square is True
    board = [True] + [False] * 39
    cur_pos = 0
    circuits = 0
    total = 0

    while sum([1 for space in board if space]) != 40:
        roll = randint(1,6) + randint(1,6)
        # if current position is more than 39, 
        # reset back within range
        cur_pos += roll
        total += roll

        if cur_pos > 39:
            circuits += 1
            cur_pos = cur_pos % 40

        board[cur_pos] = True

    # print(f"It took {circuits} circuits to hit every square on the board.")
    # print(f"A total of {total} spaces were moved.")

    return circuits, total


def main():
    circuit_lengths, totals = [], []
    reps = 100000
    for _ in range(reps):
        c, t = monopoly()
        circuit_lengths.append(c)
        totals.append(t)

    print(f'''
    Average circuit length: {sum(circuit_lengths) / reps}
    Highest circuit length: {max(circuit_lengths)}
    Lowest circuit length: {min(circuit_lengths)}

    Average spaces moved: {sum(totals) / reps}
    Highest spaces moved: {max(totals)}
    Lowest spaces moved: {min(totals)}
    ''')

    plt.scatter(range(reps), circuit_lengths, label = "Circuit lengths")
    plt.legend()
    plt.show()


main()