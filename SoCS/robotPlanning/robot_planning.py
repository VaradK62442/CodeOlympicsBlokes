# robot simulation

class Robot:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos


def create_grid(N):
    grid = [['0' for i in range(N)] for j in range(N)]
    grid[0][0] = '1'
    grid[N-1][N-1] = '2'
    
    return grid


def print_grid(grid):
    for x in grid:
        for y in x:
            print(y, end = ' ')
        print()


def move_r1(r1, r2):    
    # strat 1:
    # move away from r2
    # r1 is to the left of r2
    if r1.x < r2.x:
        # move left
        return (r1.x + 1, r1.y)

    # r1 is to the right of r2
    elif r1.x > r2.x:
        # move right
        return (r1.x - 1, r1.y)

    else:
        # check if above or below

        # r1 is above r2
        if r1.y > r2.y:
            # move left
            return (r1.x, r1.y - 1)

        # r1 is below r2
        elif r1.y < r2.y:
            # move right
            return (r1.x, r1.y + 1)

        else:
            # there is a crash!
            return (-1, -1)



def move_r2(r1, r2):
    # move toward r1
    # returns new position

    # r1 is to the left of r2
    if r1.x < r2.x:
        # move left
        return (r2.x - 1, r2.y)

    # r1 is to the right of r2
    elif r1.x > r2.x:
        # move right
        return (r2.x + 1, r2.y)

    else:
        # check if above or below

        # r1 is above r2
        if r1.y > r2.y:
            # move left
            return (r2.x, r2.y + 1)

        # r1 is below r2
        elif r1.y < r2.y:
            # move right
            return (r2.x, r2.y - 1)

        else:
            # there is a crash!
            return (-1, -1)


def simulate(grid, r1, r2):
    # r1 = pos of robot 1
    # goal is to reach (N-1, N-1)

    # r2 = pos of robot 2
    # goal is to kill robot 1

    r1_new = move_r1(r1, r2)
    r2_new = move_r2(r1, r2)

    # remove previous positions from grid
    grid[r1.x][r1.y] = '0'
    grid[r2.x][r2.y] = '0'

    # update objects
    r1.x, r1.y = r1_new
    r2.x, r2.y = r2_new

    # update grid
    grid[r1.x][r1.y] = '1'
    grid[r2.x][r2.y] = '2'

    print_grid(grid)

    return grid, r1, r2


def main():
    N = 5
    grid = create_grid(N)
    r1 = Robot(0, 0)
    r2 = Robot(N-1, N-1)

    for _ in range(10):
        grid, r1, r2 = simulate(grid, r1, r2)
        print()


main()