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


transformations = []
for row in rows:
    transformations.append(transformation(row))


# for transformation in transformations:
#     print(transformation)


class reactor_cube:
    def __init__(self, x, y, z):
        self.on = False
        self.x = x
        self.y = y
        self.z = z


points = []
for x in range(-50, 51):
    for y in range(-50, 51):
        for z in range(-50, 51):
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
