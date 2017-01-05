moves = {
    'r': lambda x, y: (x + 1, y),
    'l': lambda x, y: (x - 1, y),
    'd': lambda x, y: (x, y + 1),
    'u': lambda x, y: (x, y - 1)
}

with open('input.txt', 'r') as f:
    fav_number = int(f.read())

is_wall = lambda x, y: ('{0:b}'.format(x * x + 3 * x + 2 * x * y + y + y * y + fav_number).count('1')) % 2
length = 100

is_open = [[not is_wall(i, j) for j in range(length)] for i in range(length)]
distance = [[-1 for i in range(length)] for j in range(length)]
marked = [[False for i in range(length)] for j in range(length)]

queue = [(1, 1)]
distance[1][1] = 0
while queue:
    x, y = queue[0]
    marked[x][y] = True

    for move in moves.itervalues():
        new_x, new_y = move(x, y)

        if (min(new_x, new_y) >= 0 and max(new_x, new_y) < length and
                not marked[new_x][new_y] and is_open[new_x][new_y]):
            distance[new_x][new_y] = distance[x][y] + 1
            queue.append((new_x, new_y))
    del queue[0]

number_reachable = sum(1 if 0 <= item <= 50 else 0 for sublist in distance for item in sublist)

print 'Distance to (31, 39):', distance[31][39]
print 'Number of locations reachable in 50 steps:', number_reachable
