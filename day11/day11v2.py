import re
import copy
import itertools
from heapq import *


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
            floor2.add(pos)
            floor1.remove(pos)
            if is_legal(floor2) and is_legal(floor1):
                result.append((copy.copy(floor1), copy.copy(floor2)))
            floor2.remove(pos)
            floor1.add(pos)
        else:
            for i in pos:
                floor2.add(i)
                floor1.remove(i)
            if is_legal(floor2) and is_legal(floor1):
                result.append((copy.copy(floor1), copy.copy(floor2)))
            for i in pos:
                floor2.remove(i)
                floor1.add(i)
    return result


def finished(state):
    pass


def evaluate_state(state):
    result = 0
    for idx, floor in enumerate(state['floors']):
        result += (idx ** 2) * len(floor)

    result -= state['steps'] * 2
    return -result


def get_possible_moves(state):
    tmp_state = copy.deepcopy(state['floors'])
    result_states = []
    el = state['elevator']
    if el < 3:
        for pf in get_possible_floors(tmp_state[el], tmp_state[el + 1]):
            new_state = copy.deepcopy(state)
            new_state['floors'][el] = pf[0]
            new_state['floors'][el + 1] = pf[1]
            new_state['elevator'] = el + 1
            new_state['steps'] += 1
            result_states.append(new_state)
    if el > 0:
        for pf in get_possible_floors(tmp_state[el], tmp_state[el - 1]):
            new_state = copy.deepcopy(state)
            new_state['floors'][el] = pf[0]
            new_state['floors'][el - 1] = pf[1]
            new_state['elevator'] = el - 1
            new_state['steps'] += 1
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
floors = [set() for _ in range(4)]
elevator = 0
count = 0

with open('input.txt', 'r') as f:
#with open('input_part2.txt', 'r') as f:
    for i, line in enumerate(f):

        for m in re.finditer(match_chip, line):
            if not elements.has_key(m.group(0)):
                elements[m.group(0)] = count * 2
                count += 1
            floors[i].add(elements[m.group(0)])

        for m in re.finditer(match_gen, line):
            if not elements.has_key(m.group(0)):
                elements[m.group(0)] = count * 2
                count += 1
            floors[i].add(elements[m.group(0)] + 1)

st = {'elevator': 0, 'steps': 0, 'floors': floors}
queue = [st]
# heappush(queue, (evaluate_state(st), st))
visited = set()

while queue:
    # pop = heappop(queue)
    # cur = pop[1]

    cur = queue[0]

    print cur, len(queue), len(visited)  # , 'eval: ', -pop[0]
    if len(cur['floors'][3]) == 10:
        print '\n', cur
        raw_input('Press enter to continue')

    if finished(cur):
        print cur
        break

    floors = [frozenset(f) for f in cur['floors']]
    if (cur['elevator'], tuple(floors)) not in visited:
        for pos_state in get_possible_moves(cur):
            p_floors = [frozenset(f) for f in pos_state['floors']]
            if (pos_state['elevator'], tuple(p_floors)) not in visited:
                # heappush(queue, (evaluate_state(pos_state), pos_state))
                queue.append(pos_state)

    visited.add((cur['elevator'], tuple(floors)))
    del queue[0]