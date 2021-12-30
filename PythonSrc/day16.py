# one giant string packet that has multiple subpacketse, headers, operations, and rules. Took me a long time.
# Part 1 is counting packet values, part 2 is calculating the final value of the packet after simplifying
file1 = open('inputs\day16.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
packet = rows[0]
first_len = len(rows[0])
# binary = bin(int(rows[0], 16))[2:] # doesn't work for some reason
binary = ""
for char in rows[0]:
    new_char = bin(int(char, 16))[2:]
    padded = new_char.zfill(4)
    binary += padded
# binary = binary.rstrip("0")
print(f"Start: Binary is {binary}")
print(f"Length: {len(binary)}")
# lazy enum
versioning = "V"
iding = "I"
literal = "L"
reading_subpackets = "R"

total_version = 0
outfile = "inputs\day16p1parsing.txt"
file = open(outfile, "a")


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
        print(f"Binary at start of loop: {binary[index:]}")
        if binary[index:] == len(binary[index:]) * "0":
            print("Only zeros remain, good bye")
            if number_of_subpackets:
                return index, total_version
            return total_version
        if current == versioning:
            start = index
            three_letters = binary[index:index + 3]
            version = int(three_letters, 2)
            print(f"packet version: {three_letters} aka {version}")
            file.write(f"{version}\n")
            total_version += version
            current = iding
            index += 3
            print(binary[index:])
        elif current == iding:
            three_letters = binary[index:index + 3]
            id = int(three_letters, 2)
            print(f"packet type id: {three_letters} aka {id}")
            if id != 4:
                mode_string = binary[index + 3]
                print(f"length type id is {mode_string}")
                index += 4
                print(binary[index:])
                if mode_string == "0":
                    next_15_bits = binary[index:index + 15]
                    print(f"Reading {next_15_bits} for total_length")
                    total_length = int(next_15_bits, 2)
                    index += 15
                    print(f"Subpackets mode with length {total_length}")
                    index_increment, version_bump = read_packet(binary[index:],
                                                                target_length=total_length)
                    index += index_increment
                    total_version += version_bump
                else:
                    next_11_bits = binary[index: index + 11]
                    print(f"Reading {next_11_bits} for total_length")
                    index += 11
                    number_of_subpackets = int(next_11_bits, 2)
                    print(f"Subpackets mode with num subpackets {number_of_subpackets}")
                    index_increment, version_bump = read_packet(binary[index:],
                                                                number_of_subpackets=number_of_subpackets)
                    index += index_increment
                    total_version += version_bump
            else:
                print("Literal-type")
                index += 3
                print(binary[index:])
                bcd = ""
                while True:
                    continues_or_not = int(binary[index])
                    index += 1
                    print(binary[index:])
                    next_4_bits = binary[index: index + 4]
                    bcd = bcd + next_4_bits
                    index += 4
                    if not continues_or_not:
                        break
                print(f"Found digit {int(bcd, 2)} from literal {bcd}")
                packets_read += 1
            if target_length:
                if index == target_length:
                    return index, total_version
            if number_of_subpackets:
                if packets_read == number_of_subpackets:
                    return index, total_version
            current = versioning


read_packet(binary)
print(total_version)
# use day16p1parsing.py to parse output of this to get the answer
