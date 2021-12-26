# approach of adding and subtracting volumes. Wrong because iterating over cuboids adds too much volume
# and too hard because calculating resulting cuboids is difficult
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
on_trans = []
for row in rows:
    t = transformation(row)
    transformations.append(t)

from dataclasses import dataclass

@dataclass()
class cuboid:
    xmin: int
    xmax: int
    ymin: int
    ymax: int
    zmin: int
    zmax: int

    def subtract_other_cuboid(self, cuboid):
        return []

    def volume(self):
        return (self.xmax - self.xmin) * (self.ymax - self.ymin) * (self.zmax - self.zmin)



on_cuboids = [] # none of the cuboids in this list shall be overlapping
volume = 0
for t in transformations:
    new_cuboid = cuboid(t.xmin, t.xmax, t.ymin, t.ymax, t.zmin, t.zmax)
    cuboids_c = on_cuboids.copy()
    if t.on:
        # check for intersection with existing ons, find t-existing volume, add volume. Somehow find only non intersecting part of old cubes and keep them,
        # removing old complete cuboids

        for cuboid in cuboids_c:
            # if cuboid intersects, subtract other cuboid, remove cuboid, add those other cuboids
            replace_cuboids = cuboid.subtract_other_cuboid(t)
            on_cuboids.extend(replace_cuboids)
        on_cuboids.append(new_cuboid)
        volume += new_cuboid.volume()



    else:
        # check for intersection with existing ons, find difference, subtract volume. Find non intersecting part of old cubes and keep them, removing
        # old complete cuboids
        for cuboid in cuboids_c:
            pass

