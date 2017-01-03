import re
import copy
import itertools

def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 == 1


def is_equal(st1, st2):
    if st1[0]['elevator'] != st2[0]['elevator']:
        return False


def get_possible_floors(floor1, floor2):
    result = []
    combinations = itertools.combinations(floor1, 2)
    p = [list(c) for c in combinations]
    for t in floor1:
        p.append(t)

    for pos in p:
        if type(pos) is int:
            floor2.append(pos)
            floor1.remove(pos)
            if is_legal(floor2) and is_legal(floor1):
                result.append((copy.copy(floor1), copy.copy(floor2)))
            floor2.remove(pos)
            floor1.append(pos)
        else:
            for i in pos:
                floor2.append(i)
                floor1.remove(i)
            if is_legal(floor2) and is_legal(floor1):
                result.append((copy.copy(floor1), copy.copy(floor2)))
            for i in pos:
                floor2.remove(i)
                floor1.append(i)
    return result


def finished(state):
    for idx in range(3):
        if state[1][idx]:
            return False
    return True


def get_possible_moves(state):
    tmp_state = copy.deepcopy(state[1])
    result_states = []
    el = state[0]['elevator']
    if el < 3:
        for pf in get_possible_floors(tmp_state[el], tmp_state[el + 1]):
            new_state = copy.deepcopy(state)
            new_state[1][el] = pf[0]
            new_state[1][el + 1] = pf[1]
            new_state[0]['elevator'] = el + 1
            new_state[0]['steps'] += 1
            result_states.append(new_state)
    if el > 0:
        for pf in get_possible_floors(tmp_state[el], tmp_state[el - 1]):
            new_state = copy.deepcopy(state)
            new_state[1][el] = pf[0]
            new_state[1][el - 1] = pf[1]
            new_state[0]['elevator'] = el - 1
            new_state[0]['steps'] += 1
            result_states.append(new_state)
    return result_states


def is_legal(floor):
    if len(filter(is_odd, floor)) > 0:
        for chip in filter(is_even, floor):
            if chip + 1 not in floor:
                return False

    return True

match_gen = re.compile(r'\w+(?= generator)')
match_chip = re.compile(r'\w+(?=-compatible)')
elements = {}
floors = [[] for _ in range(4)]
elevator = 0
count = 0

with open('input.txt', 'r') as f:
    for i, line in enumerate(f):

        for m in re.finditer(match_chip, line):
            if not elements.has_key(m.group(0)):
                elements[m.group(0)] = count * 2
                count += 1
            floors[i].append(elements[m.group(0)])

        for m in re.finditer(match_gen, line):
            if not elements.has_key(m.group(0)):
                elements[m.group(0)] = count * 2
                count += 1
            floors[i].append(elements[m.group(0)] + 1)

st = [{'elevator': 0, 'steps': 0}, floors]
queue = [st]
visited = []

while queue:
    print queue[0], len(queue), len(visited)

    if finished(queue[0]):
        print queue[0]
        break

    if queue[0][1] not in visited:
        for s in get_possible_moves(queue[0]):
            if s[1] not in visited:
                queue.append(s)
                #queue.insert(0, s)

    visited.append(queue[0][1])
    del queue[0]
