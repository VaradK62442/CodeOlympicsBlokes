maze = [['+', '-', '+', '-', '+', '-', '-', '+'],
        ['|', ' ', ' ', ' ', ' ', '|', ' ', '|'],
        ['+', ' ', '+', '-', ' ', ' ', ' ', '+'],
        ['|', ' ', ' ', 'F', '|', ' ', ' ', '|'],
        ['+', '-', '+', '-', '+', ' ', ' ', '+'],
        ['+', '-', '+', '-', '+', '-', ' ', '+'],
        ['|', '$', ' ', ' ', ' ', ' ', ' ', '|'],
        ['+', '-', '+', '-', '+', '-', '-', '+']]

height = len(maze)
width = len(maze[0])
graph = {}

def checkAdjacent(x,y):
    adjacent = []
    if maze[x -1][y]==' ' or maze[x -1][y]=='F':
        adjacent.append((x-1,y))
    if maze[x][y+1]==' ' or maze[x][y+1]=='F':
        adjacent.append((x,y+1))
    if maze[x +1][y]==' ' or maze[x +1][y]=='F':
        adjacent.append((x+1,y))
    if maze[x][y-1]==' ' or maze[x][y-1]=='F':
        adjacent.append((x,y-1))
    return adjacent

for x in range(width):
    for y in range(height):
        if maze[x][y] == '$':
            jake = (x,y)
            graph[(x,y)] = checkAdjacent(x,y)
        elif maze[x][y] == 'F':
            food = (x,y)
            graph[(x,y)] = checkAdjacent(x,y)
        elif maze[x][y] == ' ':
            graph[(x,y)] = checkAdjacent(x,y)

foundFood = False
path = []
pathToFood = []

def dfs(visited, graph, node):  #function for dfs 
    global path
    global pathToFood
    global foundFood
    if node not in visited:
        #print(node)
        #print(path)
        visited.append(node)
        if node == food:
            foundFood = True
            pathToFood = path.copy()
            return
        for neighbour in graph[node]:
            path.append(neighbour)
            dfs(visited, graph, neighbour)
            if not foundFood:
                path.pop()
visited = []
dfs(visited, graph, jake)

print("food at", food)
print("jake at", jake)
#print(pathToFood)

def getDirection(here, there):
    if here[0]<there[0]:
        return "down"
    elif here[0]>there[0]:
        return "up"
    elif here[1]<there[1]:
        return "right"
    elif here[1]>there[1]:
        return "left"

wordPath = []
for i in range(len(pathToFood)):
    if i==0:
        wordPath.append(getDirection(jake, pathToFood[0]))
    else:
        wordPath.append(getDirection(pathToFood[i-1], pathToFood[i]))

print(wordPath)
        
            