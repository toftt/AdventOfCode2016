class BotNetwork(object):

    node_list = {}
    chip_list = []

    def add_bot(self, name, low, high):
        self.node_list[name] = self.Bot(name, low, high)

    def add_output(self, name):
        self.node_list[name] = self.Output(name)

    def distribute_chips(self):
        for chip in self.chip_list:
            self.node_list[chip[0]].receive_chip(self, chip[1])

    def parse_instruction(self, instruction):
        instruction = instruction.split(' ')

        if instruction[0] == 'bot':
            name, low, high = map(' '.join, [instruction[0:2], instruction[5:7], instruction[10:12]])
            if low[0] == 'o':
                self.add_output(low)
            if high[0] == 'o':
                self.add_output(high)
            self.add_bot(name, low, high)

        elif instruction[0] == 'value':
            value = int(instruction[1])
            bot = ' '.join(instruction[4:6])
            self.chip_list.append([bot, value])

    class Bot(object):

        def __init__(self, name, low, high):
            self.name = name
            self.low = low
            self.high = high
            self.chips = []

        def receive_chip(self, bot_net, chip):
            self.chips.append(chip)
            if len(self.chips) == 2:
                if max(self.chips) == 61 and min(self.chips) == 17:
                    print 'Bot comparing value-61 microchips with value-17 microchips:', self.name
                # print self.name, 'gives', max(self.chips), 'to', self.high
                bot_net.node_list[self.high].receive_chip(bot_net, max(self.chips))
                # print self.name, 'gives', min(self.chips), 'to', self.low
                bot_net.node_list[self.low].receive_chip(bot_net, min(self.chips))

                self.chips = []

    class Output(object):

        def __init__(self, name):
            self.name = name
            self.chips = []

        def receive_chip(self, bot_net, chip):
            self.chips.append(chip)

bot_net = BotNetwork()

with open('input.txt', 'r') as f:
    for line in f:
        bot_net.parse_instruction(line.strip())

bot_net.distribute_chips()
mul = 1
for n in ['output ' + str(i) for i in range(3)]:
    mul *= bot_net.node_list[n].chips[0]
print 'Values of one chip in each of outputs 0, 1, and 2 multiplied:', mul
