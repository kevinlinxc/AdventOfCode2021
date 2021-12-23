file1 = open('inputs\day19.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]
import itertools




def config(points, id):
    new_points = []
    for point in points:
        x, y , z = (int(i) for i in point)
        # no one look at this code thanks
        state = id//3
        if state % 8 == 0:
            pass
        elif state % 8 == 1:
            x, y, z = x, y, -z
        elif state % 8 == 2:
            x, y, z = x, -y, z
        elif state % 8 == 3:
            x, y, z = x, -y, -z
        elif state % 8 == 4:
            x, y, z = -x, y, z
        elif state % 8 == 5:
            x, y, z = -x, y, -z
        elif state % 8 == 6:
            x, y, z = -x, -y, z
        elif state % 8 == 7:
            x, y, z = -x, -y, -z

        rotation = id % 3
        if rotation == 1:
            x, y, z = y, z, x
        elif rotation == 2:
            x, y, z = z, x, y
        new_points.append((x, y, z))
    return new_points

class scanner:
    def __init__(self, id):
        self.id = id
        self.points = []


    def add_point(self, list):
        self.points.append((list[0], list[1], list[2]))

    def __repr__(self):
        return str(self.points)

    def permute(self, orientation):
        return config(self.points, orientation)

    def diffs(self, list_of_points):
        return_list = []
        for pair in itertools.permutations(list_of_points, 2):
            pair1, pair2 = pair[0], pair[1]
            xdiff = int(pair2[0]) - int(pair1[0])
            ydiff = int(pair2[1]) - int(pair1[1])
            zdiff = int(pair2[2]) - int(pair1[2])
            return_list.append((xdiff, ydiff, zdiff))
        return return_list




current = None
list_of_scanners = []
import re
for row in rows:
    if row:
        match = re.match("--- scanner ([0-9]*) ---", row)
        if match:
            current = scanner(match.group(1))
            list_of_scanners.append(current)
        else:
            current.add_point(row.split(","))


new_scanners = {}
figured_out_scanners = {0}
current_diffs = list_of_scanners[0].diffs(list_of_scanners[0].points)
while new_scanners != figured_out_scanners:
    new_scanners = figured_out_scanners
    for i in range(1, len(list_of_scanners)-1):
        if i in figured_out_scanners:
            continue
        scanner = list_of_scanners[i]
        for j in range(24):
            counter = 0
            diffs = scanner.diffs(scanner.permute(j))
            for diff in diffs:
                if diff in current_diffs:
                    print(f"Diff {diff} from scanner {i} matches existing if permute {j}")
                    counter += 1
                    if counter > 12:
                        current_diffs.extend(diffs)
                        print(f"Scanner {i} works with permutation {j}")
                        figured_out_scanners.add(i)
                        break


print(list_of_scanners)



