file1 = open('inputs\day7.txt', 'r')
Lines = file1.readlines()
print(Lines)
stripped = [(line.strip("\n")) for line in Lines]
stripped = stripped[0].split(",")
positions = [int(age) for age in stripped]


max_pos = max(positions)
print(max_pos)
min_fuel = float('inf')
best_position = -1
for i in range(1931):
    fuel = 0
    for position in positions:
        n = abs(position-i)
        fuel += n
    if fuel < min_fuel:
        min_fuel = fuel
        best_position = i

print(best_position)
print(f"Fuel used: {min_fuel}")

# 340056