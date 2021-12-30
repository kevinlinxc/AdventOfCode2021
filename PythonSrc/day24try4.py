# used this dashboard to manually enter values and note effects. Also used to compare the original input and my simplified input
file1 = open('inputs\day24.txt', 'r')
file2 = open('inputs\day24test.txt', 'r')
lines = file1.readlines()
lines2 = file2.readlines()
rows = [(line.strip()) for line in lines]
rows2 = [(line.strip()) for line in lines2]
import streamlit

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
    # cond6 = (int(inputs[1]) + int(inputs[3]) + int(inputs[5]) + int(inputs[7]) + int(inputs[11]) + 10) % 26 - 12 == int(inputs[12])
    cond6 = z12 % 26 - 12 == int(inputs[12])
    m6 = 1 if cond6 else 26
    z13 = z12 // 26 * m6 + offset_input(12, inputs) * int(not cond6)
    # cond7 = int(inputs[0]) + int(inputs[12]) - 13 == int(inputs[13])
    cond7 = z13 % 26 - 13 == int(inputs[13])
    m7 = 1 if cond7 else 26
    z14 = z13 // 26 * m7 + offset_input(13, inputs) * int(not cond7)
    zlist = [z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14]
    return z14, zlist


def check_model_number(input, rows):
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
    zlist = []
    for row in rows:
        if "inp" in row:
            if input_counter != 0:
                zlist.append(z)
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
    zlist.append(z)
    global counter
    counter += 1
    return z, zlist


f = open("inputs\day24outputreal.txt", "a")


def main():
    streamlit.set_page_config(layout="wide")
    min_score = float("inf")
    min_num = "99999999999999"
    if "min_score" not in streamlit.session_state:
        streamlit.session_state['min_score'] = min_score
    if "min_num" not in streamlit.session_state:
        streamlit.session_state['min_num'] = min_num
    cols = streamlit.columns(14)
    current_num = streamlit.empty()
    number = ["1"] * 14
    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(cols)):
        number[i] = cols[i].selectbox(f"Number {i + 1}", options=options, key=i)
    total_num = "".join(number)
    score, zlist = check_model_number(total_num, rows)
    score2 = check_model_number(total_num, rows2)
    score3, zlist3 = check_model_number_unparsed(total_num)
    if score == score3:
        streamlit.markdown("# two are equal for now")
    else:
        streamlit.markdown("# two are NOT equal")
    streamlit.write(zlist)
    streamlit.write(zlist3)
    current_num.markdown(f"# {total_num} has score {score}, {score3}")
    if score == 0:
        print(f"AHHHHHHHHHHHHHHHHHHHHHHHH {total_num}")
    if score < streamlit.session_state['min_score']:
        streamlit.session_state['min_score'] = score
        streamlit.session_state['min_num'] = total_num
    streamlit.write(f"Min score so far: {streamlit.session_state['min_score']}")
    streamlit.write(f"Min num so far: {streamlit.session_state['min_num']}")


if __name__ == '__main__':
    main()
# biggest: 99995969919326
# smallest: 48111514719111
