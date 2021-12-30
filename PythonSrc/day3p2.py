file1 = open('inputs\day3.txt', 'r')
Lines = file1.readlines()
print(Lines)
stripped = [(line.strip()) for line in Lines]

print(stripped)
length = len(str(stripped[0]))

zero_count = [0] * length


def find_oxygen(stripped):
    for i in range(length + 1):
        if len(stripped) == 1:
            return stripped[0]
        one_count = 0
        zero_count = 0
        for item in stripped:
            if item[i] == "0":
                zero_count += 1
            else:
                one_count += 1
        newstripped = []
        if one_count >= zero_count:
            for item in stripped:
                if item[i] == "1":
                    newstripped.append(item)
        else:
            for item in stripped:
                if item[i] == "0":
                    newstripped.append(item)
        stripped = newstripped


def find_scrubber(stripped):
    for i in range(length + 1):
        if len(stripped) == 1:
            return stripped[0]
        one_count = 0
        zero_count = 0
        for item in stripped:
            if item[i] == "0":
                zero_count += 1
            else:
                one_count += 1
        newstripped = []
        if zero_count <= one_count:
            for item in stripped:
                if item[i] == "0":
                    newstripped.append(item)
        else:
            for item in stripped:
                if item[i] == "1":
                    newstripped.append(item)
        stripped = newstripped


print(f'oxygen {find_oxygen(stripped)}')

print(f'scrubber {find_scrubber(stripped)}')
print(int(find_oxygen(stripped), 2) * int(find_scrubber(stripped), 2))

# print(int(b"000100011001",2))
# print(int(b"111011100110",2))
# print(281*3814)

# 6124992
