file1 = open('inputs\day11.txt', 'r')
lines = file1.readlines()
rows = []
for line in lines:
    rows.append(list(map(int, line.strip())))
print(rows)
width = len(rows[0])-1
height = len(rows) -1
deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def flash(row_index, col_index, rows, already_flashed):
    for delta in deltas:
        new_row = row_index + delta[0]
        new_col = col_index + delta [1]
        if 0 <= new_row <= height and 0 <= new_col <=width:
            if rows[new_row][new_col] != 0:
                rows[new_row][new_col] += 1
    rows[row_index][col_index] = 0

counter = 0
for i in range(100):
    for row_index, row in enumerate(rows):
        for col_index, number in enumerate(row):
            row[col_index] +=1
    already_flashed = []
    while any([value > 9 for value in [item for sublist in rows for item in sublist]]):
        for row_index, row in enumerate(rows):
            for col_index, num in enumerate(row):
                if num > 9:
                    flash(row_index, col_index, rows, already_flashed)
                    counter += 1
                    already_flashed.append((row_index, col_index))
    print(f"Rows at step {i}: {rows}")
print(counter)
#1686
