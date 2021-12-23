file1 = open('inputs\day16p2parsing.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
counter = 0
from collections import deque
operator_count = 0
end_count = 0
for row in rows:
    if "operator" in row:
        operator_count += 1
    elif "end" in row:
        end_count += 1
print(f"Operators: {operator_count}, ends: {end_count}")
operator_stack = deque()
numbers_stack = deque()
# numbers_stack.append([])
# 0: "sum",
# 1: "product",
# 2: "minimum",
# 3: "maximum",
# 5: "greater_than",
# 6: "less_than",
# 7: "equals"
for row in rows:
    if "operator" in row:
        operator_stack.append(row[len("operator: "):])
        numbers_stack.append([])
    elif "literal: " in row:
        lis1 = numbers_stack.pop()
        lis1.append(int(row.lstrip("literal: ")))
        numbers_stack.append(lis1)
    elif "end subpackets" in row:
        operator = operator_stack.pop()
        latest_list = numbers_stack.pop()
        new_value = 0
        if operator == "sum":
            for item in latest_list:
                new_value += item
        elif operator == "product":
            new_value = 1
            for item in latest_list:
                new_value *= item
        elif operator =="minimum":
            new_value = min(latest_list)
        elif operator == "maximum":
            new_value = max(latest_list)
        elif operator == "greater_than":
            assert len(latest_list) == 2 ,f"len is {len(latest_list)}"
            if latest_list[0] > latest_list[1]:
                new_value = 1
            else:
                new_value = 0
        elif operator == "less_than":
            assert len(latest_list) == 2, f"len is {len(latest_list)}"
            if latest_list[0] < latest_list[1]:
                new_value = 1
            else:
                new_value = 0
        elif operator == "equals":
            assert len(latest_list) == 2, f"len is {len(latest_list)}"
            if latest_list[0] == latest_list[1]:
                new_value = 1
            else:
                new_value = 0

        try:
            next_list = numbers_stack.pop()
        except:
            pass
        next_list.append(new_value)
        numbers_stack.append(next_list)
        if len(list(numbers_stack)) == 1:
            print(numbers_stack)

print(numbers_stack)