# tried a lot of brute force variations until day24try4 and day24try5 together got me across the line with some pen and paper
file1 = open('inputs\day24.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]

w = 0
x = 0
y = 0
z = 0
counter = 0

def check_model_number(input, thread_name):
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
    global counter
    counter += 1
    if z == 0:

        print(f"{thread_name}: {input} is a valid model number!")
        return True
    else:
        if counter % 100000 == 0:
            print(f"{thread_name} {input} is NOT a valid model number, z = {z}")
        return False

f = open("inputs\day24outputreal.txt", "a")

max_model_num = 0
def run_from(ceiling, thread_name):
    for i in range(ceiling, 11111311662335, -1):
        string_num = str(i)
        if "0" not in string_num:
            if check_model_number(string_num, thread_name):
                print(i)
                f.write(str(i))
                exit(0)

from multiprocessing import Process

#past progress:
#9999998457476
#9999986895698
#9999985427378
#9999963749661
#9999962628649
#9999952983773
#9999946745883
#9999938614332
def main():
    threads = []
    for x in range(9):
        start = int(str(x) + "9999938614332 ")
        t = Process(target=run_from, args=(start, f"thread-{x}"))
        t.start()
        threads.append(t)

    import time
    try:
        while 1:
            time.sleep(.1)
    except KeyboardInterrupt:
        for t in threads:
            t.join()
        print("threads successfully closed")

if __name__ == '__main__':
    main()



print(f"Hi {max_model_num}")
