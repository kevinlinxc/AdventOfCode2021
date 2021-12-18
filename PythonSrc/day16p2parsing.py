file1 = open('inputs\day16p2parsing.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
counter = 0
from collections import deque

operator_stack = deque()
operator_count  = 0
end_count = 0
for row in rows:
    if "operator" in row:
        operator_count += 1
    elif "end" in row:
        end_count += 1

print(operator_count)
print(end_count)