import re
import itertools

class RTF(object):

    match_gen = re.compile(r'\w+(?= generator)')
    match_chip = re.compile(r'\w+(?=-compatible)')

    def __init__(self):
        self.elevator = 1
        self.floors = {}
        for i in range(1, 5):
            self.floors[i] = self.Floor()

    def copy(self):
        result = self.__class__()
        result.elevator = self.elevator
        for k, v in self.floors.iteritems():
            result.floors[k] = v.copy()
        return result

    def parse_instructions(self, instructions):
        for idx, instruction in enumerate(instructions):
            for m in re.finditer(RTF.match_gen, instruction):
                self.floors[idx + 1].add_generator(m.group(0))
            for m in re.finditer(RTF.match_chip, instruction):
                self.floors[idx + 1].add_chip(m.group(0))

    def is_legal(self):
        for floor in self.floors.itervalues():
            print floor
            print floor.is_legal()

    class Floor(object):

        def __init__(self):
            self.generators = []
            self.chips = []

        def __str__(self):
            return 'Generators: ' + self.generators.__str__() + '\nChips: ' + self.chips.__str__()

        def get_possible_pickups(self):
            s = self.generators
            s.extend(self.chips)
            print s

        def copy(self):
            result = self.__class__()
            result.generators = list(self.generators)
            result.chips = list(self.chips)
            return result

        def add_chip(self, chip):
            self.chips.append(chip)

        def add_generator(self, generator):
            self.generators.append(generator)

        def is_legal(self):
            if len(self.generators) > 0:
                for chip in self.chips:
                    if chip not in self.generators:
                        return False

            return True

rtf = RTF()

with open('input.txt', 'r') as f:
    rtf.parse_instructions(line.strip() for line in f)

rtf.floors[1].get_possible_pickups()