# idea of adding all points that will be turned on to a list and then applying transformations to every point
# ideally faster, but still way too slow with O(n^3)
file1 = open('inputs\day22.txt', 'r')
lines = file1.readlines()
rows = [(line.strip()) for line in lines]


class transformation:
    def __init__(self, row):
        self.on = True if row.split(" ")[0] == "on" else False
        rest = row.split(" ")[1]
        xstring, ystring, zstring = rest.split(",")
        xstring, ystring, zstring = xstring[2:], ystring[2:], zstring[2:]
        self.xmin, self.xmax = int(xstring.split("..")[0]), int(xstring.split("..")[1])
        self.ymin, self.ymax = int(ystring.split("..")[0]), int(ystring.split("..")[1])
        self.zmin, self.zmax = int(zstring.split("..")[0]), int(zstring.split("..")[1])

    def __repr__(self):
        return str(self.on) + ", " + str(self.xmin) + " to " + str(self.xmax) + ", " + str(self.ymin) + " to " + \
               str(self.ymax) + ", " + str(self.zmin) + " to " + str(self.zmax)

xmin = 0
xmax = 0
ymin = 0
ymax = 0
zmin =0
zmax = 0
transformations = []
for row in rows:
    t=transformation(row)
    if t.on:
        xmin = min(xmin, t.xmin)
        xmax = max(xmax, t.xmax)
        ymin = min(ymin, t.ymin)
        ymax = max(ymax, t.ymax)
        zmin = min(zmin, t.zmin)
        zmax = max(zmax, t.zmax)
    transformations.append(transformation(row))

print(f"Found bounds {xmin}, {xmax}, {ymin}, {ymax}, {zmin}, {zmax}")
# for transformation in transformations:
#     print(transformation)


class reactor_cube:
    def __init__(self, x, y, z):
        self.on = False
        self.x = x
        self.y = y
        self.z = z

import sys
def progress(purpose,currentcount, maxcount):
    sys.stdout.write('\r')
    sys.stdout.write("{}: {:.1f}%, {} of {}".format(purpose,(100/(maxcount-1)*currentcount), currentcount, maxcount))
    sys.stdout.flush()


points = []
n = (xmax-xmin) * (ymax-ymin) * (zmax-zmin)
counter = 0
for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        for z in range(zmin, zmax+1):
            counter += 1
            progress("Adding point: ", counter, n)
            # print(f"Adding point {x}, {y}, {z}")
            points.append(reactor_cube(x, y, z))

for index, transformation in enumerate(transformations):
    print(f"Doing transformation {index}: {transformation}")
    for point in points:
        if transformation.xmin <= point.x <= transformation.xmax and \
                transformation.ymin <= point.y <= transformation.ymax and \
                transformation.zmin <= point.z <= transformation.zmax:
            point.on = transformation.on

counter = 0
for point in points:
    if point.on:
        counter+=1

print(counter)
#644257
