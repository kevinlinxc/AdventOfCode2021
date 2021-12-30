# tags: hard, dijkstra, graph, search, path, shortest path
file1 = open('inputs\day15ex.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
width = len(rows[0]) - 1
height = len(rows) - 1

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


for y, row in enumerate(rows):
    for x, letter in enumerate(row):
        position = (x, y)
        moves = get_legal_moves((x, y))
        for move in moves:
            new_x, new_y = move[0], move[1]
            edge_value = int(rows[new_y][new_x])
            graph.add_edge(position, move, edge_value)

start = (0, 0)
end = (width, height)
path = find_path(graph, start, end)
print(path)
# 717
