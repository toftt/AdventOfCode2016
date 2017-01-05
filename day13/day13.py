def make_is_wall_function(fav_num):
    return lambda x, y: ('{0:b}'.format(x * x + 3 * x + 2 * x * y + y + y * y + fav_num).count('1')) % 2


with open('input.txt', 'r') as f:
    fav_number = int(f.read())

is_wall = make_is_wall_function(fav_number)
length = 50

maze = [[0 for i in range(length)] for j in range(length)]
for x in range(len(maze)):
    for y in range(len(maze[0])):
        maze[x][y] = is_wall(x, y)

distance = [[-1 for i in range(len(maze))] for j in range(len(maze[0]))]
marked = [[False for i in range(len(maze))] for j in range(len(maze[0]))]

queue = [(1, 1)]
distance[1][1] = 0
while queue:
    x, y = queue[0][0], queue[0][1]
    marked[x][y] = True

    if x - 1 >= 0 and not marked[x - 1][y] and not maze[x - 1][y]:
        distance[x - 1][y] = distance[x][y] + 1
        queue.append((x - 1, y))

    if y - 1 >= 0 and not marked[x][y - 1] and not maze[x][y - 1]:
        distance[x][y - 1] = distance[x][y] + 1
        queue.append((x, y - 1))

    if x + 1 < len(maze) and not marked[x + 1][y] and not maze[x + 1][y]:
        distance[x + 1][y] = distance[x][y] + 1
        queue.append((x + 1, y))

    if y + 1 < len(maze[0]) and not marked[x][y + 1] and not maze[x][y + 1]:
        distance[x][y + 1] = distance[x][y] + 1
        queue.append((x, y + 1))

    del queue[0]

s = 0
for i in distance:
    for j in i:
        if j != -1 and j <= 50:
            s += 1

print 'Distance to (31, 39):', distance[31][39]
print 'Number of locations reachable in 50 steps:', s
