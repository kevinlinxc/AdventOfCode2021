# actually only changed n between part 1 and 2
file1 = open('inputs\day20.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
lookup = rows[0]
picture = rows[2:]
print(lookup)
print(picture)


def get_nine_digits(picture, rowindex, charindex, exterior):
    return_value = ""
    diffs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    for diff in diffs:
        new_row = rowindex + diff[0]
        new_column = charindex + diff[1]
        try:
            return_value += "1" if picture[new_row][new_column] == "#" else "0"
        except:
            return_value += "1" if exterior == "#" else "0"
    return return_value


def expand(picture, exterior):
    row_width = len(picture[0])
    new_row_width = row_width + 2
    new_pic = [exterior * new_row_width]
    new_pic.extend([exterior + row_to_expand + exterior for row_to_expand in picture])
    new_pic.append(exterior * new_row_width)
    return new_pic


def augment_picture(picture, i):
    if i % 2 == 0:
        exterior = "."
        next_exterior = "#"
    else:
        exterior = "#"
        next_exterior = "."
    picture = expand(picture, exterior)
    new_width = len(picture[0]) + 2
    output_picture = [next_exterior * new_width]

    for rowindex, row in enumerate(picture):
        new_row = next_exterior
        for charindex, char in enumerate(row):
            nine_digits = get_nine_digits(picture, rowindex, charindex, exterior)
            new_pixel_index = int(nine_digits, 2)
            new_pixel = lookup[new_pixel_index]
            new_row += new_pixel
        new_row += next_exterior
        output_picture.append(new_row)
    output_picture.append(next_exterior * new_width)
    return output_picture


times = 50

for i in range(times):
    picture = augment_picture(picture, i)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in picture]))

counter = 0
for row in picture:
    for char in row:
        if char == "#":
            counter += 1

print(counter)
# 14279
