class KeyPad(object):

    dirs = {
        'U': [-1, 0],
        'D': [1, 0],
        'L': [0, -1],
        'R': [0, 1]
    }

    def __init__(self, layout, start_pos):
        self.layout = layout
        self.set_layout()
        self.code = ""
        self.cur_pos = [start_pos[0] + 1, start_pos[1] + 1]
        self.start_pos = list(self.cur_pos)

    def set_layout(self):
        self.layout.insert(0, [None for _ in range(len(self.layout[0]))])
        self.layout.append([None for _ in range(len(self.layout[0]))])
        for row in self.layout:
            row.insert(0, None)
            row.append(None)

    def is_legal(self, pos):
        return self.layout[pos[0]][pos[1]] is not None

    def move(self, direction):
        new_pos = [x + y for x, y in zip(self.cur_pos, KeyPad.dirs[direction])]
        if self.is_legal(new_pos):
            self.cur_pos = new_pos

    def get_current(self):
        current = self.layout[self.cur_pos[0]][self.cur_pos[1]]
        self.cur_pos = self.start_pos
        self.code += current

imagined_keypad = KeyPad(
    [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ],
    [1, 1]
)

bathroom_keypad = KeyPad(
    [
        [None, None, '1', None, None],
        [None, '2', '3', '4', None],
        ['5', '6', '7', '8', '9'],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None]
    ],
    [2, 0]
)

with open('input.txt', 'r') as f:
    for line in f:
        for c in line.strip():
            imagined_keypad.move(c)
            bathroom_keypad.move(c)
        imagined_keypad.get_current()
        bathroom_keypad.get_current()

print imagined_keypad.code
print bathroom_keypad.code
