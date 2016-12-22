count = 0

with open('input.txt', 'r') as f:
    for line in f:
        triangle = line.strip().split()
        triangle = [int(side) for side in triangle]
        triangle.sort()

        if triangle[0] + triangle[1] > triangle[2]:
            count += 1

print "by rows:", count
count = 0
triangles = []
with open('input.txt', 'r') as f:
    for idx, line in enumerate(f):
        triangles.append(line.strip().split())
        if idx % 3 == 2:
            triangles = zip(*triangles)
            for triangle in triangles:
                triangle = [int(side) for side in triangle]
                triangle.sort()
                if triangle[0] + triangle[1] > triangle[2]:
                    count += 1
            triangles = []

print "by cols:", count