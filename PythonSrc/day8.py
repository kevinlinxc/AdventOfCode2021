# 7 segment display fixing. Using pen and paper to deduce which input signals correspond to which segments
file1 = open('inputs\day8.txt', 'r')
Lines = file1.readlines()
print(Lines)
stripped = [(line.strip()) for line in Lines]
counter = 0
for line in stripped:
    right_digits = line.split(' | ')[1].split(" ")
    for digit in right_digits:
        if len(digit) in [2, 3, 4, 7]:
            counter += 1
print(counter)
# 530
