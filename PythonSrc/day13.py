# tags: folding, matplotlib in part 2
# folding pages and seeing which dots line up. See what message appears at the end
import re
file1 = open('inputs\day13.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)

folds = []
dots = []
dots_set = set()
max_x = 0
max_y = 0


def fold_fun(dots, axis, location):
    new_dots = set()
    if axis == "y":
        for dot in dots:
            dotx, doty = dot[0], dot[1]
            if dot[1] > location:
                new_location = (dotx, location - (doty - location))
                if new_location[0] >= 0 and new_location[1] >= 0:
                    new_dots.add(new_location)
            else:
                new_dots.add(dot)
        return new_dots
    if axis == "x":
        for dot in dots:
            dotx, doty = dot[0], dot[1]
            if dot[0] > location:
                new_location = (location - (dotx - location), doty)
                if new_location[0] >= 0 and new_location[1] >= 0:
                    # print(f"Mirroring {dotx}, {doty} across y={location} to {new_location}")
                    new_dots.add(new_location)
            else:
                new_dots.add(dot)
    return new_dots


for row in rows:
    if "fold" in row:
        print(row)
        instruction = re.search(r"[a-z]=[0-9]*", row).group(0)
        # print(f"found fold {instruction}")
        direction, number = instruction.split("=")
        folds.append((direction, int(number)))
    elif "," in row:
        x, y = row.split(",")
        x = max(int(x), max_x)
        y = max(int(y), max_y)
        dots.append((x, y))

# fold = folds[0]
# board = fold_fun(dots,fold[0], fold[1])
for fold in folds:
    print(f"Doing fold: {fold}")
    board = fold_fun(dots, fold[0], fold[1])
    dots = board
    print(f"Board now: {board}")
    print(f"Board size: {len(board)}")
# print(dots)
# print(folds)
# 753
