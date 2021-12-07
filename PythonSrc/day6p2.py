#lanternfish

file1 = open('inputs\day6.txt', 'r')
Lines = file1.readlines()
print(Lines)
stripped = [(line.strip("\n")) for line in Lines]
fishages = stripped[0].split(",")
fishages = [int(age) for age in fishages]


#severely optimized code from part 1
n = 256
days = [0] * n
for age in fishages:
    days[age] += 1

number_of_fish = len(fishages)
for i in range(n+3):
    gain = days[i]
    if i + 7 < n:
        days[i+7] += gain
    if i+9< n:
        days[i+9] += gain
    number_of_fish += gain
    print(f"{number_of_fish} fish on day {i+1}")
print(number_of_fish)

#1732821262171