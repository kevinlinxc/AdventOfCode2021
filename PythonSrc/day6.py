# lanternfish exponentially breeding. Trick: just keep track of numbers of fish, not individual fish. Part 2 is more
# days. See part 2 for this optimized code.

file1 = open('inputs\day6.txt', 'r')
Lines = file1.readlines()
print(Lines)
stripped = [(line.strip("\n")) for line in Lines]
fishages = stripped[0].split(",")
fishages = [int(age) for age in fishages]

for _ in range(80):
    day_counter = 0
    for index, age in enumerate(fishages):
        if age == 0:
            day_counter += 1
            fishages[index] = 6
        else:
            fishages[index] = age - 1
    for j in range(day_counter):
        fishages.append(8)
    print(f"{day_counter} fish were born on day {_ + 1}, current population: {len(fishages)}")
print(len(fishages))

# 386536
