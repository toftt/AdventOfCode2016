def cpy(x, y):
    registers[y] = registers[x] if x in registers else int(x)


def inc(x):
    registers[x] += 1


def dec(x):
    registers[x] -= 1


def jnz(x, y):
    global current
    x = registers[x] if x in registers else x
    if x != 0:
        current += int(y) - 1

part_two = True
current = 0
registers = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0
}

with open('input.txt', 'r') as f:
    instructions = f.read().split('\n')

if part_two:
    registers['c'] = 1

while 0 <= current < len(instructions):
    to_do = instructions[current]
    locals()[to_do.split(' ')[0]](*to_do.split(' ')[1:])
    current += 1

if not part_two:
    print 'Answer (part 1):', registers['a']
else:
    print 'Answer (part 2):', registers['a']
