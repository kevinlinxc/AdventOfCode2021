# tags: bfs, graph, search
# search through path through nodes. Capitals can be visited multiple times, but start and end only once.
# in part two, what if one small cave could be visited more than once?
file1 = open('inputs\day12.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
graph = {}
for row in rows:
    split = row.split("-")
    start, end = split[0], split[1]
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]
    if end in graph:
        graph[end].append(start)
    else:
        graph[end] = [start]

print(graph)

# visited = set()
counter = 0


def printAllPathsUtil(start, dest, visited, path):
    # Mark the current node as visited and store in path
    global counter
    # checking for upper cuz the question allows upper places to be visited multiple times
    if not start.isupper():
        visited[start] = True
    path.append(start)

    # If current vertex is same as destination, then print
    # current path[]
    if start == dest:
        print(path)
        counter += 1
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for i in graph[start]:
            if not visited[i]:
                printAllPathsUtil(i, dest, visited, path)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[start] = False


# just replaced this setup function with a defaultdict and empty path initialization
# def printAllPaths(start, dest):
#     # Mark all the vertices as not visited
#     visited = {}
#     for key in graph.keys():
#         visited[key] = False
#
#     # Create an array to store paths
#     path = []
#
#     # Call the recursive helper function to print all paths
#     printAllPathsUtil(start, dest, visited, path)

from collections import defaultdict

visited = defaultdict(lambda: False)
printAllPathsUtil("start", "end", visited, path=[])
print(counter)
# 3713
