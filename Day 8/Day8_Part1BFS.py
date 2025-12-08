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

from collections import defaultdict, deque
graph = defaultdict(list)
dist_sorted = dict(sorted(distances.items(), key=lambda x: x[1]))
i = 0
for point, distance in dist_sorted.items():
    x,y = point
    if y not in graph[x]:
        graph[x].append(y)
    if x not in graph[y]:
        graph[y].append(x)
    i += 1
    if i == 1000:
        break
def bfs( node ):
    queue = deque([node])
    total = 0
    while queue:
        n = queue.popleft()
        for conn in graph[n]:
            if conn not in visited:
                visited.add(conn)
                queue.append(conn)
        total += 1
    return total
visited = set()
connected_components = []
for i in range(len(points)):
    if i not in visited:
        visited.add(i)
        total = 1
        ret = bfs(i)
        if ret > 0:
            total = ret
        connected_components.append(total)
connected_components.sort()
print( connected_components[-1] * connected_components[-2] * connected_components[-3]) # Part 1: 122430