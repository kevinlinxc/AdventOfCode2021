file1 = open('inputs\day15.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
width = len(rows[0]) - 1
height = len(rows) - 1


# functions to make new grid
def next_number(number):
    if number == "9":
        return "1"
    return str(int(number) + 1)


def increment_row(row: str):
    output = ""
    for char in row:
        output += next_number(char)
    return output


def increment_multi(row, times):
    for i in range(times):
        row = increment_row(row)
    return row


# expand rows to the right first
new_rows = []
for row in rows:
    row_copy = row
    for i in range(1, 5):
        new_row = increment_multi(row_copy, i)
        row = row + new_row
    new_rows.append(row)

# expand rows downward
while len(new_rows) < 5 * (height + 1):
    current_lst = len(new_rows) - 1
    reference = new_rows[current_lst - height]
    new_row = increment_row(reference)
    new_rows.append(new_row)

rows = new_rows
width = len(rows[0]) - 1
height = len(rows) - 1
print(rows)
from dijkstar import Graph, find_path

graph = Graph()


def get_legal_moves(position: tuple):
    x = position[0]
    y = position[1]
    deltas = []
    if x > 0:
        new_position = (x - 1, y)
        deltas.append(new_position)
    if x < width:
        new_position = (x + 1, y)
        deltas.append(new_position)
    if y > 0:
        new_position = (x, y - 1)
        deltas.append(new_position)
    if y < height:
        new_position = (x, y + 1)
        deltas.append(new_position)
    return deltas


edge_count = 0
for y, row in enumerate(rows):
    for x, letter in enumerate(row):
        position = (x, y)
        moves = get_legal_moves((x, y))
        for move in moves:
            new_x, new_y = move[0], move[1]
            edge_value = int(rows[new_y][new_x])
            edge_count += 1
            graph.add_edge(position, move, edge_value)

start = (0, 0)
end = (width, height)
path = find_path(graph, start, end)
print(path)
print(f"Number of edges: {edge_count}")
# 2993
