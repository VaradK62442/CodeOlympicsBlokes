def read_in_file(fname):
    users = {}
    # create a dictionary {user: [friend_1, friend_2, ...]}
    with open(fname) as f:
        for line in f:
            user, friend = line.rstrip("\n").split(" ")
            if user in users:
                users[user].append(friend)
            else:
                users[user] = [friend]

    return users


def find_groups(users):
    groups = []
    for user in users:
        added = False
        # check if user already in groups list
        for g in groups:
            if user in g:
                g.update(users[user])
                added = True

        # if not already in groups list, make a new group
        if not added:
            groups.append(set(user))
            groups[-1].update(set([person for person in users[user]]))

    # get lengths
    group_lengths = [len(g) for g in groups]
    max_length = max(group_lengths)     
    max_length_group_id = group_lengths.index(max_length)
    biggest_group = groups[max_length_group_id]

    return max_length, biggest_group    


def main():
    users05 = read_in_file("./SoCS/friends05.txt")
    max05, biggest05 = find_groups(users05)

    users10 = read_in_file("./SoCS/friends10.txt")
    max10, biggest10 = find_groups(users10)

    print(f'''
    max group size for friends05: {max05}
    max group size for friends10: {max10}
    ''')


if __name__ == "__main__":
    main()