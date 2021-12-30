file1 = open('inputs\day12.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
print(rows)
graph = {}
import sys

sys.setrecursionlimit(3500)
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

counter = 0
good_paths = set()


def list_of_strings_hashcode(list_of_strings):
    prime = 31
    result = 1
    for string in list_of_strings:
        result = result * prime + hash(string)
    return result


def printAllPathsUtil(start, dest, visited, path, can_visit_twice):
    # Mark the current node as visited and store in path
    global counter
    if not start.isupper():
        if start == can_visit_twice:
            visited[start] = visited[start] + 1
        else:
            visited[start] = 2
    path.append(start)

    # If current vertex is same as destination, then print
    # current path[]
    if start == dest:
        hashcode = list_of_strings_hashcode(path)
        if hashcode not in good_paths:
            counter += 1
            print(f"New path found: {path}")
            good_paths.add(hashcode)
        else:
            pass
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for i in graph[start]:
            if visited[i] < 2:
                printAllPathsUtil(i, dest, visited, path, can_visit_twice)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    if start == can_visit_twice:
        visited[start] = visited[start] - 1
    else:
        visited[start] = 0


def printAllPaths(start, dest, can_visit_twice):
    # Mark all the vertices as not visited
    visited = {}
    for key in graph.keys():
        visited[key] = 0

    # Create an array to store paths
    path = []

    # Call the recursive helper function to print all paths
    printAllPathsUtil(start, dest, visited, path, can_visit_twice)


small_caves = [key for key in graph.keys() if key.islower() and key not in ["start", "end"]]
for small_cave in small_caves:
    printAllPaths("start", "end", small_cave)
print(counter)
