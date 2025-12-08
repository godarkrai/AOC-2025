with open('Day8Input.txt') as f:
    input = f.read().splitlines()

points = []
for i in input:
    points.append(list(map(int, i.split(','))))

from math import sqrt
distances = {}
for i in range(len(points)):
    for j in range(i+1, len(points)):
        x1 = points[i][0]
        y1 = points[i][1]
        z1 = points[i][2]
        x2 = points[j][0]
        y2 = points[j][1]
        z2 = points[j][2]
        distances[(i,j)] = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
edge_dict = dict(sorted(distances.items(), key=lambda x: x[1]))

class DSU:

    # n is the length of our total points/coordinates
    def __init__(self, n):
        self.parent = list(range(n)) # in the starting every component is a parent of itself
        self.size = [1] * n # size of each component
        self.components = n # total components = total points
    
    # union is always done with the root, so if the current element is not its root find its root
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a,b):
        # 1. find roots of both elements
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False #Already connected

        # ensure ra is always bigger
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.size[rb] = 0
        self.components -= 1
        return True

def solve( part, k ):
    n = len(points)
    dsu = DSU(n)
    i = 0
    for (a,b), _ in edge_dict.items():
        dsu.union(a,b)
        if part == 1:
            i += 1
            if i == k:
                component_sizes = [dsu.size[dsu.find(i)] for i in range(n) if dsu.parent[i] == i]
                component_sizes.sort()
                return component_sizes[-1] * component_sizes[-2] * component_sizes[-3]
        if dsu.components == 1:
            return (points[a][0] * points[b][0])
print("Part 1:", solve(1, 1000)) # Part 1: 122430
print("Part 2:", solve(2, None)) # Part 2: 8135565324