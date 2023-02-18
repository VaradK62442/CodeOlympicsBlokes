users = {}

# Create a dictionary {user: [friend_1, friend_2, ...]}
with open("friends05.txt") as f:
    for line in f:
        user, friend = line.rstrip("\n").split(" ")
        if user in users:
            users[user].append(friend)
        else:
            users[user] = [friend]

groups = []
print(users)
# Test

for user in users:
    groups.append([user])
    for friend in users[user]:
        if friend not in users:
            continue
        if user not in users[friend]:
            continue
        if len(groups[-1]) >= 2:
            for friend_prev in groups[-1][1:]:
                if friend in users[friend_prev] and friend_prev in users[friend]:
                    continue
                break
            else:
                groups[-1].append(friend)
        else:
            groups[-1].append(friend)

for group in sorted(groups, key=lambda x: len(x)):
    print(group)