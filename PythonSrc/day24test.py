file1 = open('inputs\day24test.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]

w = 0
x = 0
y = 0
z = 0


def check_model_number(inputs):
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
            w = int(inputs[input_counter])
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

    return "".join([str(w), str(x), str(y), str(z)])


print(check_model_number([15]))
