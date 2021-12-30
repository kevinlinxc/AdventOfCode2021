file1 = open('inputs\day15ex.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
width = len(rows[0]) - 1
height = len(rows) - 1
graph = {}
import sys

sys.setrecursionlimit(3000)


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
        graph[(x, y)] = get_legal_moves((x, y))

visited = set()
counter = 0
score = 0


def printAllPathsUtil(start, dest, visited, path, score):
    # Mark the current node as visited and store in path
    path.append(start)
    visited[start] = True
    score_at_start = int(rows[start[1]][start[0]])
    score += score_at_start
    # If current vertex is same as destination, then print
    # current path[]
    if start == dest:
        print(score)
        print(path)
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for i in graph[start]:
            if visited[i] == False:
                printAllPathsUtil(i, dest, visited, path, score)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[start] = False
    score -= score_at_start


def printAllPaths(start, dest):
    # Mark all the vertices as not visited
    visited = {}
    for key in graph.keys():
        visited[key] = False

    # Create an array to store paths
    path = []

    # Call the recursive helper function to print all paths
    printAllPathsUtil(start, dest, visited, path, score)


printAllPaths((0, 0), (width, height))
