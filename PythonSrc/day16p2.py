file1 = open('inputs\day16.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
packet = rows[0]
first_len = len(rows[0])
# binary = bin(int(rows[0], 16))[2:] # doesn't work for some reason
binary = ""
debug = False
for char in rows[0]:
    new_char = bin(int(char, 16))[2:]
    padded = new_char.zfill(4)
    binary += padded
# binary = binary.rstrip("0")
print(packet)
print(f"Start: Binary is {binary}")
# lazy enum
versioning = "V"
iding = "I"
reading_subpackets = "R"

total_version = 0
operators = {
    0: "sum",
    1: "product",
    2: "minimum",
    3: "maximum",
    5: "greater_than",
    6: "less_than",
    7: "equals"
}


def literal(binary, index, values):
    bcd = ""
    while True:
        continues_or_not = int(binary[index])
        index += 1
        next_4_bits = binary[index: index + 4]
        bcd = bcd + next_4_bits
        index += 4
        if debug: print(binary[index:])
        if not continues_or_not:
            break
    literal = int(bcd, 2)
    print(f"literal: {literal}")
    values.append(literal)
    return index


from collections import deque

operator_stack = deque()


def operate(operator, latest_list):
    new_value = 0
    if operator == "sum":
        for item in latest_list:
            new_value += item
    elif operator == "product":
        new_value = 1
        for item in latest_list:
            new_value *= item
    elif operator == "minimum":
        new_value = min(latest_list)
    elif operator == "maximum":
        new_value = max(latest_list)
    elif operator == "greater_than":
        assert len(latest_list) == 2, f"len is {len(latest_list)}"
        if latest_list[0] > latest_list[1]:
            new_value = 1
        else:
            new_value = 0
    elif operator == "less_than":
        assert len(latest_list) == 2, f"len is {len(latest_list)}"
        if latest_list[0] < latest_list[1]:
            new_value = 1
        else:
            new_value = 0
    elif operator == "equals":
        assert len(latest_list) == 2, f"len is {len(latest_list)}"
        if latest_list[0] == latest_list[1]:
            new_value = 1
        else:
            new_value = 0
    return new_value


def read_packet(binary, number_of_subpackets=None, target_length=None):
    index = 0
    packets_read = 0
    values = []
    while index < len(binary):
        if debug:
            print(binary[index:])
        if binary[index:] == len(binary[index:]) * "0":
            return values
        version_letters = binary[index:index + 3]
        version = int(version_letters, 2)

        if debug:
            print(f"version {version}")
        index += 3
        if debug:
            print(binary[index:])
        id_letters = binary[index:index + 3]
        id = int(id_letters, 2)
        if debug:
            print(f"id: {id}")
        if id == 4:
            index += 3
            if debug:
                print(binary[index:])
            index = literal(binary, index, values)
        else:
            mode_string = binary[index + 3]
            if debug:
                print(f"mode: {mode_string}")
            index += 4
            if debug:
                print(binary[index:])
            print(f"operator: {operators[id]}")
            operator_stack.append(operators[id])
            if mode_string == "0":
                next_15_bits = binary[index:index + 15]
                total_length = int(next_15_bits, 2)
                if debug:
                    print(f"Reading subpacket with length {total_length} from {next_15_bits}")
                index += 15
                if debug:
                    print(binary[index:])
                index_increment, value = read_packet(binary[index:],
                                                     target_length=total_length)

                index += index_increment
                values.append(value)
                if debug:
                    print(binary[index:])
            else:
                next_11_bits = binary[index: index + 11]
                number_of_subpackets_next = int(next_11_bits, 2)
                if debug:
                    print(f"Reading subpacket with quantity {number_of_subpackets_next} from {next_11_bits}")
                index += 11
                if debug:
                    print(binary[index:])

                index_increment, value = read_packet(binary[index:], number_of_subpackets=number_of_subpackets_next)
                index += index_increment
                values.append(value)
                if debug:
                    print(binary[index:])
        if target_length:
            if index == target_length:
                operator = operator_stack.pop()
                value = operate(operator, values)
                print("end subpackets")
                return index, value
        if number_of_subpackets:
            packets_read += 1
            if packets_read == number_of_subpackets:
                operator = operator_stack.pop()
                value = operate(operator, values)
                print("end subpackets")
                return index, value


print(read_packet(binary))
# 184487454837
# day162parsing was supposed to parse output but I just ended up putting everything in here
