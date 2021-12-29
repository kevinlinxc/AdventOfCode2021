# in this attempt I try to create a single formula for z that python could execute quickly, but it turns out it was really slow and needed more optimized
file1 = open('inputs\day24.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]

w = "0"
x = "0"
y = "0"
z = "0"
inputs = ["in1", "in2", "in3", "in4", "in5", "in6", "in7", "in8", "in9", "in10", "in11", "in12", "in13", "in14"]



def read_monad(inputs):
    global w
    global x
    global y
    global z

    input_counter = 0

    for row in rows:
        if "inp" in row:
            w = inputs[input_counter]
            input_counter += 1
        elif "add" in row:
            vars = row[4:]
            left, right = vars.split(" ")
            if right.lstrip("-").isnumeric():
                if int(right) == 0:
                    continue
                globals()[left] = "(" + f"{globals()[left]}) + " + right
            else:
                globals()[left] = "(" + f"{globals()[left]}) + " + f"{globals()[right]}"
        elif "mul" in row:
            vars = row[4:]
            left, right = vars.split(" ")
            if right.lstrip("-").isnumeric():
                if int(right) == 0:
                    globals()[left] = "0"
                    continue
                globals()[left] = "(" + f"{globals()[left]}) * " + right
            else:
                globals()[left] = "(" + f"{globals()[left]}) * " + f"{globals()[right]}"
        elif "div" in row:
            vars = row[4:]
            left, right = vars.split(" ")
            if right.lstrip("-").isnumeric():
                globals()[left] = "(" + f"{globals()[left]}) // " + right
            else:
                globals()[left] = "(" + f"{globals()[left]}) // " + f"{globals()[right]}"
        elif "mod" in row:
            vars = row[4:]
            left, right = vars.split(" ")
            if right.lstrip("-").isnumeric():
                globals()[left] = "(" + f"{globals()[left]}) % " + right
            else:
                globals()[left] = "(" + f"{globals()[left]}) % " + f"{globals()[right]}"
        elif "eql" in row:
            vars = row[4:]
            left, right = vars.split(" ")
            if right.lstrip("-").isnumeric():
                globals()[left] = "int((" + f"{globals()[left]}) == " + right + ")"
            else:
                globals()[left] = "int((" + f"{globals()[left]}) == " + f"{globals()[right]}" + ")"

    return w, x, y, z


wf, xf, yf, zf = read_monad(inputs)

#11111111111111
#11111111177632
# 11111169364264
# 11111311662335
# print(f"w: {wf}")
# print(f"x: {xf}")
# print(f"y: {yf}")
# print(f"z: {zf}")
f = open("inputs\day24output.txt", "w")
f.write(zf)

# this code just runs forever on just 1 input so probably not gonna work
# zf = "global ret; ret = " + zf
# num = 111111111111
# num_list = list(str(num))
# for i in range(len(inputs)):
#     zf.replace(inputs[i], num_list[i])
#     print("before")
#     exec(zf)
#     print("After")
#     global ret
#     print(ret)

