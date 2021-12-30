file1 = open('inputs\day16p1parsing.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
counter = 0
for item in rows:
    counter += int(item)

print(counter)
# 886
