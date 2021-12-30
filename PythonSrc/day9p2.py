file1 = open('inputs\day9.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
width = len(rows[0]) - 1
height = len(rows) - 1
all_low_points = {}
low_points = []
for row_index, row in enumerate(rows):
    for col_index, num in enumerate(row):
        if col_index != 0:
            if num >= row[col_index - 1]:
                continue

        if col_index != width:
            if num >= row[col_index + 1]:
                continue

        if row_index != 0:
            if num >= rows[row_index - 1][col_index]:
                continue

        if row_index != height:
            if num >= rows[row_index + 1][col_index]:
                continue
        # it's a low point!
        low_points.append((row_index, col_index))

basin_sizes = []


def search(basin):
    new_basin = basin.copy()
    for spot in basin:
        row_index = spot[0]
        col_index = spot[1]
        # check up
        if row_index != 0:
            if rows[row_index - 1][col_index] != '9' and (row_index - 1, col_index) not in basin:
                new_basin.add((row_index - 1, col_index))
        # check down
        if row_index != height:
            if rows[row_index + 1][col_index] != '9' and (row_index + 1, col_index) not in basin:
                new_basin.add((row_index + 1, col_index))
        # check left
        if col_index != 0:
            if rows[row_index][col_index - 1] != '9' and (row_index, col_index - 1) not in basin:
                new_basin.add((row_index, col_index - 1))
        # check_right
        if col_index != width:
            if rows[row_index][col_index + 1] != '9' and (row_index, col_index + 1) not in basin:
                new_basin.add((row_index, col_index + 1))

    return new_basin


for low_point in low_points:
    basin = {low_point}
    while True:
        old_basin = basin
        new_basin = search(basin)
        if new_basin == old_basin:
            break
        basin = new_basin
    basin_size = len(new_basin)
    basin_sizes.append(basin_size)
    print(f"low_point {low_point} has basin_size {basin_size}")

print(basin_sizes)
answer = 1
for i in range(3):
    largest = max(basin_sizes)
    answer *= largest
    basin_sizes.pop(basin_sizes.index(largest))
    print(largest)

print(answer)
# 1023660
