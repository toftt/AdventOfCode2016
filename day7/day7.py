import re

# Part 1

# Matches sequence inside []
pat1 = re.compile(r"\[\w*(.)(?!\1)(.)\2\1\w*\]")
# Matches square brackets
pat2 = re.compile(r"\[\w*\]")
# Matches sequence
pat3 = re.compile(r"\w*(.)(?!\1)(.)\2\1\w*")

count = 0
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()

        if re.search(pat1, line) is not None:
            continue

        parts = re.split(pat2, line)
        for p in parts:
            if re.search(pat3, p) is not None:
                count += 1
                break
print count

# Part 2

pat4 = re.compile(r"\w*((\w)(?!\2)(\w)\2)(?!\w*\]).*(\[\w*\3\2\3\w*\])")
pat5 = re.compile(r"\[\w*(\w)(?!\1)(\w)\1\w*\].*\2\1\2(?!\w*\])")

count = 0
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()

        if re.search(pat4, line) is not None:
            count += 1
            continue

        if re.search(pat5, line) is not None:
            count += 1
            continue

print count