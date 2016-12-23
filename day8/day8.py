class LittleScreen(object):

    def __init__(self, rows, cols):
        self.grid = [['-'] * cols for _ in range(rows)]

    def __str__(self):
        result = ''
        for row in self.grid:
            result += row.__str__() + '\n'
        return result

    def lit_pixels(self):
        count = 0
        for row in self.grid:
            for col in row:
                if col == '#':
                    count += 1
        return count

    def rect(self, x, y):
        for i in range(y):
            for j in range(x):
                self.grid[i][j] = '#'

    def rotate_row(self, row, shift):
        self.grid[row] = self.grid[row][-shift:] + self.grid[row][:-shift]

    def rotate_column(self, col, shift):
        length = len(self.grid)
        new_col = [None for _ in range(length)]
        for idx, row in enumerate(self.grid):
            new_col[(idx + shift) % length] = row[col]

        for idx, row in enumerate(self.grid):
            row[col] = new_col[idx]

    def parse_instruction(self, instruction):
        if instruction[:4] == 'rect':
            self.rect(*[int(x) for x in instruction.split()[1].split('x')])

        else:
            args = [int(x) for x in instruction.split('=')[1].split(' by ')]
            method = getattr(self, 'rotate_' + instruction.split()[1])
            method(*args)

screen = LittleScreen(6, 50)

with open('input.txt', 'r') as f:
    for line in f:
        screen.parse_instruction(line.strip())

print screen.lit_pixels()
print screen
