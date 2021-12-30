# Manually parsed the logic in the input commands into a function. Basically pen and paper -> code so that I could
# understand what the logic was doing. After I had a valid function, compared it to the actual function for validation
# and then used try4's UI to test numbers following the logic
file1 = open('inputs\day24.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]

w = 0
x = 0
y = 0
z = 0
counter = 0

input_offsets = [10, 5, 12, 12, 6, 4, 15, 3, 7, 11, 2, 12, 4, 11]


def offset_input(index, inputs):
    return int(inputs[index]) + input_offsets[index]


def check_model_number_unparsed(input):
    inputs = list(input)
    z1 = offset_input(0, inputs)
    z2 = z1 * 26 + offset_input(1, inputs)
    z3 = z2 * 26 + offset_input(2, inputs)
    cond1 = int(inputs[2]) == int(inputs[3])
    m1 = 1 if cond1 else 26
    z4 = z2 * m1 + offset_input(3, inputs) * int(not cond1)
    z5 = z4 * 26 + offset_input(4, inputs)
    cond2 = int(inputs[4]) + 4 == int(inputs[5])
    m2 = 1 if cond2 else 26
    z6 = z4 * m2 + offset_input(5, inputs) * int(not cond2)
    z7 = z6 * 26 + offset_input(6, inputs)
    cond3 = int(inputs[6]) + 3 == int(inputs[7])
    m3 = 1 if cond3 else 26
    z8 = z6 * m3 + offset_input(7, inputs) * int(not cond3)
    z9 = z8 * 26 + offset_input(8, inputs)
    z10 = z9 * 26 + offset_input(9, inputs)
    cond4 = int(inputs[9]) + 8 == int(inputs[10])
    m4 = 1 if cond4 else 26
    z11 = z9 * m4 + offset_input(10, inputs) * int(not cond4)
    # cond5 = int(inputs[3]) + int(inputs[10]) - 4 == int(inputs[11])
    cond5 = z11 % 26 - 13 == int(inputs[11])
    m5 = 1 if cond5 else 26
    z12 = z11 // 26 * m5 + offset_input(11, inputs) * int(not cond5)
    # cond6 = (int(inputs[1]) + int(inputs[3]) + int(inputs[5]) + int(inputs[7])+ int(inputs[11]) + 10) % 26 - 12 == int(inputs[12])
    cond6 = z12 % 26 - 12 == int(inputs[12])
    m6 = 1 if cond6 else 26
    z13 = z12 // 26 * m6 + offset_input(12, inputs) * int(not cond6)
    # cond7 = int(inputs[0]) + int(inputs[12]) - 13 == int(inputs[13])
    cond7 = z13 % 26 - 13 == int(inputs[13])
    m7 = 1 if cond7 else 26
    z14 = z13 // 26 * m7 + offset_input(13, inputs) * int(not cond7)
    return z14
