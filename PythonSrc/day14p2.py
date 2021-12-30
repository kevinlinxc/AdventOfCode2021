file1 = open('inputs\day14.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
insert_rules = {}
frequency = {}
start = rows[0]


def add_or_increment(dict, value, quantity=1):
    if value in dict:
        dict[value] += quantity
    else:
        dict[value] = quantity


for char in start:
    add_or_increment(frequency, char)

# collect the insertion rule pairs
for i in range(2, len(rows)):
    line = rows[i]
    split = line.split(" -> ")
    sides, insert = split[0], split[1]
    print(f"Sides {sides}, insert {insert}")
    insert_rules[sides] = insert

pairs = {}


def first_build(start):
    for i in range(0, len(start) - 1):
        left = start[i]
        right = start[i + 1]
        combined = left + right
        if combined in insert_rules:
            add_or_increment(pairs, combined)


def build(pairs, freq):
    pairs_copy = pairs.copy()
    for pair in pairs_copy:
        if pair in insert_rules:
            quantity = pairs_copy[pair]
            insert = insert_rules[pair]
            add_or_increment(freq, insert, quantity)
            first = pair[0]
            second = pair[1]
            pairs[pair] -= quantity
            add_or_increment(pairs, first + insert, quantity)
            add_or_increment(pairs, insert + second, quantity)


epochs = 40
first_build(start)
print(pairs)
print(frequency)
for i in range(epochs):
    build(pairs, frequency)
    print(f"Frequency at step {i + 1}: {frequency}")

print(frequency)
maximum = max(frequency.values())
minimum = min(frequency.values())
print(maximum)
print(minimum)
print(maximum - minimum)
# 4302675529689
