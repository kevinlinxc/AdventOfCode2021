# risk level maze. Find shortest path. Part 2 involves copying the map five times with rules for new risk.
file1 = open('inputs\day15.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
width = len(rows[0]) - 1
height = len(rows) - 1

start_risk = rows[0][0]
end_risk = rows[height][width]


def get_legal_moves(position: tuple, visited):
    x = position[0]
    y = position[1]
    deltas = []
    if x > 0:
        new_position = (x - 1, y)
        if new_position not in visited:
            deltas.append(new_position)
    if x < width:
        new_position = (x + 1, y)
        if new_position not in visited:
            deltas.append(new_position)
    if y > 0:
        new_position = (x, y - 1)
        if new_position not in visited:
            deltas.append((x, y - 1))
    if y < height:
        new_position = (x, y + 1)
        if new_position not in visited:
            deltas.append((x, y + 1))
    return deltas


history = set()

lowest_risk = float("inf")


def recurse(position: tuple, risk: int):
    history.add(position)
    new_positions = get_legal_moves(position, history)
    for new_position in new_positions:
        if new_position == (width, height):
            return risk + int(end_risk)
        else:
            risk_at_new_position = risk + int(rows[new_position[1]][new_position[0]])

            return risk + recurse(new_position, risk_at_new_position)


print(recurse((0, 0), int(start_risk)))
