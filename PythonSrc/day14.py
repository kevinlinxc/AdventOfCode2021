# tags: hard, insert, exponential
file1 = open('inputs\day14.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
insert_rules = {}
start = rows[0]
for i in range(2, len(rows)):
    line = rows[i]
    split = line.split(" -> ")
    sides, insert = split[0], split[1]
    print(f"Sides {sides}, insert {insert}")
    insert_rules[sides] = insert


def build(current):
    next = []
    for i in range(0, len(current)-1):
        left = current[i]
        right = current[i+1]
        combined = left+right
        next.append(left+insert_rules.get(combined, ""))
    next.append(current[-1])
    return "".join(next)

epochs = 10
for i in range(epochs):
    print(f"After step {i+1}: {start}, {i}")
    start = build(start)
    print(f"Length at step {i+1}: {len(start)}")

counter = list(start)
ms_freq = max(counter, key=counter.count)
print(f"{ms_freq} is most frequent")
ls_freq = min(counter, key=counter.count)
print(f"{ls_freq} is least frequent")
max1 = counter.count(ms_freq)
print(f"{ms_freq} occurs {max1} times")
min1 = counter.count(ls_freq)
print(f"{ls_freq} occurs {min1} times")
print(max1 - min1)
#3284
