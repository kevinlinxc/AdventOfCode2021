file1 = open('inputs\day16.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
packet = rows[0]
first_len= len(rows[0])
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
    packets_read = 0

    while index < len(binary):
        if debug: print(binary[index:])
        if binary[index:] == len(binary[index:]) * "0":
            if number_of_subpackets or target_length:
                print("end subpackets")
                return index
        three_letters = binary[index:index+3]
        version = int(three_letters, 2)

        if debug: print(f"version {version}")
        index += 3
        if debug: print(binary[index:])
        three_letters = binary[index:index+3]
        id = int(three_letters, 2)
        if debug: print(f"id: {id}")
        if id != 4:
            mode_string = binary[index+3]
            if debug: print(f"mode: {mode_string}")
            index += 4
            if debug: print(binary[index:])
            print(f"operator: {operators[id]}")
            if mode_string == "0":
                next_15_bits = binary[index:index+15]
                total_length = int(next_15_bits, 2)
                if debug: print(f"Reading subpacket with length {total_length} from {next_15_bits}")
                index += 15
                if debug: print(binary[index:])
                index_increment = read_packet(binary[index:],
                                                            target_length=total_length)
                index += index_increment
                if debug: print(binary[index:])
            else:
                next_11_bits = binary[index: index+11]
                number_of_subpackets = int(next_11_bits, 2)
                if debug: print(f"Reading subpacket with quantity {number_of_subpackets} from {next_11_bits}")
                index += 11
                if debug: print(binary[index:])

                index_increment = read_packet(binary[index:], number_of_subpackets=number_of_subpackets)
                index += index_increment
                if debug: print(binary[index:])
        else:
            index += 3
            if debug: print(binary[index:])
            bcd = ""
            while True:
                continues_or_not = int(binary[index])
                index += 1
                next_4_bits = binary[index: index+4]
                bcd = bcd + next_4_bits
                index += 4
                if debug: print(binary[index:])
                if not continues_or_not:
                    break
            print(f"literal: {int(bcd, 2)} from {bcd}")
        packets_read += 1
        if target_length:
            if index == target_length:
                print("end subpackets")
                return index
        if number_of_subpackets:
            if packets_read == number_of_subpackets:
                print("end subpackets")
                return index


read_packet(binary)
print(total_version)
# use day16p2parsing.py to parse output of this run
