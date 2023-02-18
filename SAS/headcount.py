# 1. identify all groups
# 2. identify group sizes
# 3. get total participants
# 4. return

# class Group 
# attributes:
#     - top left coord
#     - bottom right coord
# add instances of Group class to list

# loop through event list
# if there is not a 1 to the left or above, it is a top left
# if there is not a 1 to right or below, it is a bottom right
# get list of top left elts and bottom right elts

# pair top left and bottom rights
# for each top left do
#     left coords will be <= right coords
#     find right coords with the smallest difference with left coords
#     that is also more than left coords
#     group has been identified
#     put in master list


from math import sqrt


class Group:
    def __init__(self, top_left, bottom_right):
        self.tl = top_left
        self.br = bottom_right
        self.size = (self.br[0] - self.tl[0] + 1) * (self.br[1] - self.tl[1] + 1)


def is_valid_pos(i, j, m, n):
    # i: x coord of elt
    # j: y coord of elt
    # m: x dimension of array
    # n: y dimension of array
    if (i < 0 or j < 0 or i > m - 1 or j > n - 1):
        return 0
    return 1


def is_top_left(arr, i, j):
    n = len(arr)
    m = len(arr[0])

    # check left
    if not (is_valid_pos(i - 1, j, m, n)) or arr[j][i - 1] == 0:
        # check above
        if not (is_valid_pos(i, j - 1, m, n)) or arr[j - 1][i] == 0:
            # current elt is in top left
            return True
    return False


def is_bot_right(arr, i, j):
    n = len(arr)
    m = len(arr[0])

    # check right
    if not (is_valid_pos(i + 1, j, m, n)) or arr[j][i + 1] == 0:
        # check down
        if not (is_valid_pos(i, j + 1, m, n)) or arr[j + 1][i] == 0:
            # current elt is in top left
            return True
    return False


def find_groups(arr):
    groups = []

    top_left = []
    bottom_right = []

    # find top lefts and bottom rights
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            if arr[j][i] == 1:
                if is_top_left(arr, i, j):
                    top_left.append([i, j])
                elif is_bot_right(arr, i, j):
                    bottom_right.append([i, j])

    # pair together top left and bottom rights
    # for each top left coord
    for tl in top_left:
        dists = {}
        # for each bottom right coord
        for br in bottom_right:    
            if br[0] >= tl[0] and br[1] >= tl[1]:
                dists[(sqrt((br[0]-tl[0])**2 + (br[1] - tl[1])))] = (br[0], br[1])

        # will fail if there is a bottom right point equal distance from a top left
        # as the actual top left point
        closest_br_dist = min(list(dists.keys()))
        closest_br = dists[closest_br_dist]

        groups.append(Group(tl, list(closest_br)))

    return groups


def display_results(group):
    team_num = len(group)

    team_sizes = []
    for g in group:
        team_sizes.append(g.size)

    team_sizes = sorted(team_sizes, reverse=True)
    total_pariticipants = sum(team_sizes)

    print(f"{team_num} teams of {team_sizes} totalling {total_pariticipants}.")


def main(event):
    groups = find_groups(event)
    display_results(groups)


event = [[1,1,0,0,0,0,1,1],
         [1,1,0,1,1,0,1,1],
         [0,0,0,1,1,0,0,0],
         [1,1,0,1,1,0,1,1],
         [1,1,0,0,0,0,1,1]]

main(event)