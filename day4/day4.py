def decypher(string, shifts):
    result = ""
    for char in string:
        if char == "-":
            result += " "
        else:
            result += chr(97 + ((ord(char) % 97) + shifts) % 26)
    return result

sector_sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        checksum = line[len(line) - 6:len(line) - 1]
        sector_id = line[len(line) - 10:len(line) - 7]

        d = {}
        for char in line[:len(line) - 10]:
            if char == '-':
                continue
            if char not in d:
                d[char] = 0
            else:
                d[char] += 1
        result = [(k, v) for k, v in d.iteritems()]
        result = sorted(result, key=lambda x: (-int(x[1]), x[0]))
        if ''.join([x[0] for x in result][:5]) == checksum:
            sector_sum += int(sector_id)
            real_name = decypher(line[:len(line) - 11], int(sector_id))
            print real_name, sector_id
print sector_sum
