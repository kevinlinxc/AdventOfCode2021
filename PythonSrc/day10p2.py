file1 = open('inputs\day10.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
from collections import deque
points = { ")": 1,
           "]": 2,
           "}": 3,
           ">": 4
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
scores = []

for row in rows:
    whatever = deque()
    error_score = 0
    bad_line = False
    for bracket in row:
        if bracket in start_brackets:
            whatever.append(bracket)
        else:
            next_to_pop = whatever.pop()
            expected = matching_bracket(next_to_pop)
            if bracket != expected:
                bad_line=True
                break
    if not bad_line:
        while len(whatever) > 0:
            error_score = error_score * 5 + points[matching_bracket(whatever.pop())]
        scores.append(error_score)

sort_scores = sorted(scores)
print(sort_scores)
print(sort_scores[len(sort_scores)//2])
#2192104158