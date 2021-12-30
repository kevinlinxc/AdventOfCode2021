# Find the most common values in certain binary positions
file1 = open('inputs\day3.txt', 'r')
Lines = file1.readlines()
print(Lines)
stripped = [(line.strip()) for line in Lines]

print(stripped)
length = len(str(stripped[0]))
one_count = [0] * length
zero_count = [0] * length

for item in stripped:
    for i in range(0, len(str(item))):
        if int(item[i]) == 0:
            zero_count[i] += 1
        else:
            one_count[i] += 1
print(one_count)
print(zero_count)
# scrappy finish
print(int(b"000100011001", 2))
print(int(b"111011100110", 2))
print(281 * 3814)
# 1071734
