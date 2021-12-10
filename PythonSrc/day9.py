file1 = open('inputs\day9.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
width = len(rows[0])-1
height = len(rows) -1
risk = 0
for row_index, row in enumerate(rows):
    for col_index, num in enumerate(row):
        low_point=True
        if col_index != 0:
            if num >= row[col_index-1]:
                continue

        if col_index != width:
            if num >= row[col_index+1]:
                continue

        if row_index != 0 :
            if num>= rows[row_index-1][col_index]:
                continue

        if row_index != height:
            if num >= rows[row_index+1][col_index]:
                continue
        risk += int(num) + 1


print(risk)
#516
