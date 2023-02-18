# take in a 2x2 array
# the nth array represents stage n, up to 5
# the first items in the nth array represent available buttons
# the fifth item in the nth array represents prompt

def stage1(l, res):
    if l[-1] == 1 or l[-1] == 2:
        return l[1], 1 # second position
    return l[l[-1]-1], l[-1]-1 # else, xth position


def stage2(l, res, prev_id):
    if l[-1] == 1:
        return 4, l.index(4) # press button labelled 4
    elif l[-1] == 3:
        return l[0], 0 # first position
    return l[prev_id], prev_id # else, same position as stage 1


def stage3(l, res):
    if l[-1] == 1:
        # same label as stage 2
        return res[0], l.index(int(res[0]))
    elif l[-1] == 2:
        # same label as stage 1
        return res[1], l.index(int(res[1]))
    elif l[-1] == 3:
        return l[2], 2 # third position
    else:
        return 4, l.index(4) # button labelled '4'


def stage4(l, res, s1_id, s2_id):
    if l[-1] == 1:
        return l[s1_id], s1_id # same pos as stage 1
    elif l[-1] == 2:
        return l[0], 0 # first position
    return l[s2_id], s2_id # else, same position as stage 2


def stage5(l, ids):
    return l[ids[l[-1]-1]] # same position as pressed in stage n


def main(stages):
    res = ''

    s1, s1_id = stage1(stages[0], res)
    res += str(s1)

    s2, s2_id = stage2(stages[1], res, s1_id)
    res += str(s2)

    s3, s3_id = stage3(stages[2], res)
    res += str(s3)

    s4, s4_id = stage4(stages[3], res, s1_id, s2_id)
    res += str(s4)
    
    res += str(stage5(stages[4], [s1_id, s2_id, s3_id, s4_id]))

    return int(res)


sequence = [[1,3,2,4,1],
            [3,1,2,4,3],
            [2,3,4,1,2],
            [2,1,4,3,1],
            [4,1,2,3,4]]

print(main(sequence))