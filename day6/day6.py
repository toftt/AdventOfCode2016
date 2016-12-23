columns = [[] for _ in range(8)]
with open('input.txt', 'r') as f:
    for line in f:
        for idx, char in enumerate(line.strip()):
            columns[idx].append(char)

# Part one
result = ''
for col in columns:
    most_common = max(set(col), key=col.count)
    result += most_common

print result

# Part two
result = ''
for col in columns:
    most_common = min(set(col), key=col.count)
    result += most_common

print result