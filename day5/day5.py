import hashlib

input = 'ojvtpuvg'


def part_one(input):

    idx = 0
    password = ''
    while len(password) < 8:
        hash = hashlib.md5(input + str(idx)).hexdigest()
        if hash[:5] == '00000':
            password += hash[5]
            print password
        idx += 1


def part_two(input):
    idx = 0
    found = 0
    password = '________'
    while found < 8:
        hash = hashlib.md5(input + str(idx)).hexdigest()
        if hash[:5] == "00000" and ord(hash[5]) < 56 and password[int(hash[5])] == '_':
            pos = int(hash[5])
            password = password[:pos] + hash[6] + password[pos + 1:]
            found += 1
            print password
        idx += 1

part_one(input)
part_two(input)
