file1 = open('inputs\day16.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
packet = rows[0]
first_len= len(rows[0])
# binary = bin(int(rows[0], 16))[2:] # doesn't work for some reason
binary = ""
for char in rows[0]:
    new_char = bin(int(char, 16))[2:]
    padded = new_char.zfill(4)
    binary += padded
# binary = binary.rstrip("0")
print(f"Start: Binary is {binary}")
# lazy enum
versioning = "V"
iding = "I"
literal = "L"
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


def read_packet(binary, number_of_subpackets=None, target_length=None):
    index = 0
    current = versioning
    global total_version
    version = 0
    id = 0
    operator = False
    total_length = 0
    packets_read = 0

    while index < len(binary):
        if binary[index:] == len(binary[index:]) * "0":
            if number_of_subpackets or target_length:
                print("end subpackets")
                return index, total_version
            return total_version
        if current == versioning:
            start = index
            three_letters = binary[index:index+3]
            version = int(three_letters, 2)

            total_version += version
            current = iding
            index += 3
        elif current == iding:
            three_letters = binary[index:index+3]
            id = int(three_letters, 2)
            if id != 4:
                mode_string = binary[index+3]
                index += 4
                print(f"operator: {operators[id]}")
                if mode_string == "0":
                    next_15_bits = binary[index:index+15]
                    total_length = int(next_15_bits, 2)
                    index += 15
                    index_increment, version_bump = read_packet(binary[index:],
                                                                target_length=total_length)
                    index += index_increment
                    total_version += version_bump
                else:
                    next_11_bits = binary[index: index+11]
                    index += 11
                    number_of_subpackets = int(next_11_bits, 2)
                    index_increment, version_bump = read_packet(binary[index:], number_of_subpackets=number_of_subpackets)
                    index += index_increment
                    total_version += version_bump
            else:
                index += 3
                bcd = ""
                while True:
                    continues_or_not = int(binary[index])
                    index += 1
                    next_4_bits = binary[index: index+4]
                    bcd = bcd + next_4_bits
                    index += 4
                    if not continues_or_not:
                        break
                print(f"literal: {int(bcd, 2)}")
                packets_read += 1
            if target_length:
                if index == target_length:
                    print("end subpackets")
                    return index, total_version
            if number_of_subpackets:
                if packets_read == number_of_subpackets:
                    print("end subpackets")
                    return index, total_version
            current = versioning


read_packet(binary)
print(total_version)
# use day16p2parsing.py to parse output of this run
