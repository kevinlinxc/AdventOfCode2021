file1 = open('inputs\day25.txt', 'r')
lines = file1.readlines()
rows = [(list(line.strip())) for line in lines]

print(rows)
height = len(rows) -1
width = len(rows[0])-1

from copy import deepcopy

def move_right(rows):
    items_moved = 0
    rowscopy = deepcopy(rows)
    for rowindex, row in enumerate(rows):
        for colindex, item in enumerate(row):
            if item == ">":
                rightindex = 0 if colindex == width else colindex+1
                if row[rightindex] == ".":
                    items_moved += 1
                    rowscopy[rowindex][rightindex] = ">"
                    rowscopy[rowindex][colindex] = "."
    return items_moved, rowscopy

def move_down(rows):
    items_moved = 0
    rowscopy = deepcopy(rows)
    for rowindex, row in enumerate(rows):
        for colindex, item in enumerate(row):
            if item == "v":
                downindex = 0 if rowindex == height else rowindex+1
                if rows[downindex][colindex] == ".":
                    items_moved += 1
                    rowscopy[downindex][colindex] = "v"
                    rowscopy[rowindex][colindex] = "."
    return items_moved, rowscopy


def cycle(rows):
    print("Start")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in rows]))
    items_moved = 0
    # print("After moving right")
    right_moves, rowsright = move_right(rows)
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in rowsright]))
    down_moves, rowsdown = move_down(rowsright)
    # print("After moving down")
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in rowsdown]))
    items_moved += right_moves + down_moves
    return items_moved, rowsdown

items_moved, rows = cycle(rows)
counter = 1
while items_moved != 0:
    items_moved, rows = cycle(rows)
    counter += 1
print(counter)
#334
