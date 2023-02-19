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
import numpy as np


class Group:
    def __init__(self, top_left, bottom_right):
        self.tl = top_left
        self.br = bottom_right
        self.size = (self.br[0] - self.tl[0] + 1) * (self.br[1] - self.tl[1] + 1)


def is_valid_pos(i, j, m, n): # O(1)
    # i: x coord of elt
    # j: y coord of elt
    # m: x dimension of array
    # n: y dimension of array
    if (i < 0 or j < 0 or i > m - 1 or j > n - 1):
        return 0
    return 1


def is_top_left(arr, i, j): # O(1)
    n, m = arr.shape

    # check left
    if not (is_valid_pos(i - 1, j, m, n)) or arr[j][i - 1] == 0:
        # check above
        if not (is_valid_pos(i, j - 1, m, n)) or arr[j - 1][i] == 0:
            # current elt is in top left
            # since there is nothing above or left
            return True
    return False


def is_bot_right(arr, i, j): # O(1)
    n, m = arr.shape

    # check right
    if not (is_valid_pos(i + 1, j, m, n)) or arr[j][i + 1] == 0:
        # check down
        if not (is_valid_pos(i, j + 1, m, n)) or arr[j + 1][i] == 0:
            # current elt is in bottom right
            # since there is nothing below or right
            return True
    return False


def check_valid(arr, tl, br): # O(1)
    # get slice of array from tl to br
    # check if all 1s

    # get correct slice
    arr = np.array(arr)
    sub_array = arr[tl[1]:br[1]+1, tl[0]:br[0]+1]

    dim = np.size(sub_array)
    total_sum = np.sum(sub_array)

    if total_sum == dim:
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

        # will fail if there is a bottom right point equal distance from a top left
        # as the actual top left point, and it is checked first
        # e.g.
        #     [1, 1, 0, 1, 1]
        #     [1, 1, 0, 1, 1]
        #     [1, 1, 0, 0, 0]
        #     [1, 1, 0, 0, 0]
        #     [1, 1, 0, 0, 0]

        # to get around this, could check if path from chosen top_left 
        # to chosen bottom_right is all 1s
        # if it is, it is a valid group

        is_valid = False
        invalid_brs = []

        while not is_valid:
            # keep repeating until valid br is chosen
            # for each bottom right coord    
            for br in bottom_right:    
                # find a br that is located to the right of and below tl
                # and is not in invalid list
                if (br[0] >= tl[0] and br[1] >= tl[1]) and br not in invalid_brs:
                    dists[(sqrt((br[0]-tl[0])**2 + (br[1] - tl[1])))] = (br[0], br[1])

            closest_br_dist = min(list(dists.keys()))
            closest_br = dists[closest_br_dist]

            # if chosen coord is not in invalid list, check if it is valid
            is_valid = check_valid(arr, tl, closest_br)
            if not is_valid:
                invalid_brs.append(closest_br)

        groups.append(Group(tl, closest_br))

    return groups


def display_results(groups):
    team_num = len(groups)

    team_sizes = []
    for g in groups:
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

# event = [
#     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#     [0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
#     [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
#     [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
#     [1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
#     [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
#     [0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
# ]


if __name__ == "__main__":
    main(np.array(event))