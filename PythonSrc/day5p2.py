file1 = open('inputs\day5.txt', 'r')
Lines = file1.readlines()
print(Lines)
stripped = [(line.strip("\n")) for line in Lines]

max_x = 0
max_y = 0
commands = []
for line in stripped:
    print(line)
    leftright = line.split(" -> ")
    left = leftright[0]
    right = leftright[1]
    x1, y1 = int(left.split(",")[0]), int(left.split(",")[1])
    x2, y2 = int(right.split(",")[0]), int(right.split(",")[1])
    max_x = max(x1, x2, max_x)
    max_y = max(y1, y2, max_y)
    commands.append([x1, y1, x2, y2])
print(f"max_x: {max_x}, max_y: {max_y}")

arr = [[0 for j in range(max_y+1)] for i in range(max_x+1)]
import math
sign = lambda x: math.copysign(1, x)
for command in commands:
    print(command)
    if command[0] == command[2]: # x stays
        first = min(command[1], command[3])
        second = max(command[1], command[3])
        for i in range(first, second + 1):
            print(f"Doing {command[0]}, {i}")
            arr[command[0]][i] += 1
    elif command[1] == command[3]: # y stays same
        first = min(command[0], command[2])
        second = max(command[0], command[2])
        for i in range(first, second + 1):
            print(f"Doing {i}, {command[1]}")
            arr[i][command[1]] += 1
    elif sign((command[3]-command[1])*(command[2]-command[0])) == 1.0: # normal diagonal
        difference = command[3] - command[1]
        plus1 = sign(difference)
        difference = abs(difference)
        start = min(command[0], command [2])
        end = min(command[1], command[3])
        for i in range(difference + 1):
            print(f"Doing {start + i}, {end + i}")
            arr[start + i][end+ i] += 1
    else: # secondary diagonal
        difference = command[2] - command[0]
        plus1 = sign(difference)
        difference = abs(difference)
        start = min(command[0], command [2])
        end = max(command[1], command[3])
        for i in range(difference + 1):
            print(f"Doing {start + i }, {end - i}")
            arr[start + i][end - i] += 1



counter = 0
for i in arr:
    for j in i:
        if j >= 2:
            counter += 1

print(f"Final answer: {counter}")
#20012
