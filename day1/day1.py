input = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"
dir_arr = input.split(", ")

cor = 1 # 0=West 1=North 2=East 3=South
arr = [0, 0] # x and y
marked = set()

for i in dir_arr:
    if i[:1] == 'L':
        cor -= 1
    else:
        cor += 1
    cor %= 4

    if cor == 0:
        for j in range(0, int(i[1:])):
            arr[0] -= 1
            t = arr[0], arr[1]
            if t in marked:
                print t
            marked.add(t)
    if cor == 1:
        for j in range(0, int(i[1:])):
            arr[1] += 1
            t = arr[0], arr[1]
            if t in marked:
                print t
            marked.add(t)
    if cor == 2:
        for j in range(0, int(i[1:])):
            arr[0] += 1
            t = arr[0], arr[1]
            if t in marked:
                print t
            marked.add(t)
    if cor == 3:
        for j in range(0, int(i[1:])):
            arr[1] -= 1
            t = arr[0], arr[1]
            if t in marked:
                print t
            marked.add(t)
print sum(arr)