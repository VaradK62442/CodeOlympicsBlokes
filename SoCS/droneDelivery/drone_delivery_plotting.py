from matplotlib import pyplot as plt

def read_in_file(fname):
    data = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            line = list(map(int, line.strip().split()))
            data.append(line)

    return data


def plot(num):
    cust = read_in_file(f"./SoCS/droneDelivery/p{num}.txt")
    dept = read_in_file(f"./SoCS/droneDelivery/depotP{num}.txt")

    m = cust[0]
    cust = cust[1:]
    n = dept[0]
    dept = dept[1:]

    x = [elt[0] for elt in cust]
    y = [elt[1] for elt in cust]

    plt.scatter(x, y)

    x = [elt[0] for elt in dept]
    y = [elt[1] for elt in dept]

    plt.scatter(x, y)

plot('22')
plot('317')
plt.show()