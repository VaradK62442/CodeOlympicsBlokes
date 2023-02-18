def read_in_file(fname):
    users = {}
    # Create a dictionary {user: [friend_1, friend_2, ...]}
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

        if not added:
            groups.append(set(user))
            groups[-1].update(set([person for person in users[user]]))

    group_lengths = [len(g) for g in groups]
    print(max(group_lengths))            


def main():
    users05 = read_in_file("./SoCS/friends05.txt")
    find_groups(users05)

    users10 = read_in_file("./SoCS/friends10.txt")
    find_groups(users10)


if __name__ == "__main__":
    main()