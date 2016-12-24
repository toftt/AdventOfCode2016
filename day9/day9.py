def decompress(data, version=2):
    count = 0
    idx = 0
    while idx < len(data):
        if data[idx] == '(':
            idx += 1
            marker = ''
            while data[idx] != ')':
                marker += data[idx]
                idx += 1

            no_of_chars, times = map(int, marker.split('x'))
            idx += 1

            if version == 2:
                count += decompress(data[idx:idx + no_of_chars], version) * times
            elif version == 1:
                count += no_of_chars * times

            idx += no_of_chars
        else:
            count += 1
            idx += 1
    return count

with open('input.txt', 'r') as f:
    line = f.readline()
    f.close()

print "Decompressed (version 1) length of input:", decompress(line, 1)
print "Decompressed (version 2) length of input:", decompress(line, 2)
