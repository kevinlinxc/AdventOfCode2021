file1 = open('inputs\day10.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
from collections import deque
points = { ")": 3,
           "]": 57,
           "}": 1197,
           ">": 25137
        }

def matching_bracket(bracket):
    if bracket == "{":
        return "}"
    elif bracket == "(":
        return ")"
    elif bracket == "[":
        return "]"
    elif bracket == "<":
        return ">"
    else:
        return "alsjdlkfajsdf"

start_brackets = {"(", "[", "{", "<"}
whatever = deque()

error_score = 0
for row in rows:
    for bracket in row:
        if bracket in start_brackets:
            whatever.append(bracket)
        else:
            next_to_pop = whatever.pop()
            expected = matching_bracket(next_to_pop)
            if bracket != expected:
                error_score+= points[bracket]
                print(f"Adding {points[bracket]} for illegal")
                break



print(error_score)
#392367