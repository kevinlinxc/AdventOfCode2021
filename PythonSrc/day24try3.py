# In this attempt I try to loop from 1-9 so I can avoid the 0s. This was harder to start at a new number with.
file1 = open('inputs\day24.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]

w = 0
x = 0
y = 0
z = 0


def check_model_number(input):
    inputs = list(input)
    global w
    w = 0
    global x
    x = 0
    global y
    y = 0
    global z
    z = 0
    input_counter = 0

    for row in rows:
        if "inp" in row:
            w = inputs[input_counter]
            input_counter += 1
        elif "add" in row:
            vars = row[4:]
            left, right = vars.split(" ")
            if right.lstrip("-").isnumeric():
                globals()[left] += int(right)
            else:
                globals()[left] += int(globals()[right])
        elif "mul" in row:
            vars = row[4:]
            left, right = vars.split(" ")
            if right.lstrip("-").isnumeric():
                globals()[left] *= int(right)
            else:
                globals()[left] *= int(globals()[right])
        elif "div" in row:
            vars = row[4:]
            left, right = vars.split(" ")
            if right.lstrip("-").isnumeric():
                globals()[left] //= int(right)
            else:
                globals()[left] //= int(globals()[right])
        elif "mod" in row:
            vars = row[4:]
            left, right = vars.split(" ")
            if right.lstrip("-").isnumeric():
                globals()[left] %= int(right)
            else:
                globals()[left] %= int(globals()[right])
        elif "eql" in row:
            vars = row[4:]
            left, right = vars.split(" ")
            if right.lstrip("-").isnumeric():
                globals()[left] = 1 if globals()[left] == int(right) else 0
            else:
                globals()[left] = 1 if globals()[left] == int(globals()[right]) else 0

    if z == 0:
        print(f"{input} is a valid model number!")
        return True
    else:
        print(f"{input} is NOT a valid model number")
        return False

file = open("inputs\day24output.txt", "a")

valid_nums = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
for a in valid_nums:
    for b in valid_nums:
        for c in valid_nums:
            for d in valid_nums:
                for e in valid_nums:
                    for f in valid_nums:
                        for g in valid_nums:
                            for h in valid_nums:
                                for i in valid_nums:
                                    for j in valid_nums:
                                        for k in valid_nums:
                                            for l in valid_nums:
                                                for m in valid_nums:
                                                    for n in valid_nums:
                                                        string = a+b+c+d+e+f+g+h+i+j+k+l+m+n
                                                        if check_model_number(string):
                                                            print(i)
                                                            file.write(str(i))
                                                            exit(0)
# 11111143577935
