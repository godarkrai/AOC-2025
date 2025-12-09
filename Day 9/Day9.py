with open('Day9Input.txt') as f:
    input = f.read().splitlines()

points = []
for i in input:
    points.append(list(map(int, i.split(',')))[::-1])
sorted(points)
# BRUTE FORCE!
max_area = 0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        height = abs(x1-x2) + 1
        length = abs(y1-y2) + 1
        max_area = max(max_area, height*length)
print(max_area) # Part 1: 4781377701

# Ray casting algo
# 1st condition the row for the point to check must be between any of the corner points
# 2nd the column crossing should be greater than the current points column
# if both of them satisfies, change the inside to not inside and do it for all corner points.
def is_point_inside_polygon(point, corners):
    row, col = point
    n = len(corners)
    inside = False
    for i in range(n):
        r1, c1 = corners[i]
        r2, c2 = corners[(i + 1) % n]
        if (r1 <= row < r2) or (r2 <= row < r1):
            if r1 != r2:
                cross_col = c1 + (row - r1) * (c2 - c1) / (r2 - r1)
                if col < cross_col:
                    inside = not inside
    
    return inside

def is_on_boundary(point, corners):
    row, col = point
    n = len(corners)
    for i in range(n):
        r1, c1 = corners[i]
        r2, c2 = corners[(i + 1) % n]
        if r1 == r2 == row:  # Horizontal edge
            if min(c1, c2) <= col <= max(c1, c2):
                return True
        elif c1 == c2 == col:  # Vertical edge
            if min(r1, r2) <= row <= max(r1, r2):
                return True
    
    return False

def are_edge_points_inside_or_boundary(four_corners, polygon_corners):
    for i in range(4):
        start = four_corners[i]
        end = four_corners[(i + 1) % 4] 
        edge_points = get_edge_points(start, end)
        for point in edge_points:
            if not is_on_boundary( point, polygon_corners) and not is_point_inside_polygon(point, polygon_corners):
                return False
    return True


def get_edge_points(start, end):
    r1, c1 = start
    r2, c2 = end
    
    points = set()
    if r1 == r2:
        if c1 <= c2: # left to right
            for c in range(c1, c2 + 1):
                points.add((r1, c))
        else: # right to left
            for c in range(c1, c2 - 1, -1):
                points.add((r1, c))
    elif c1 == c2:
        if r1 <= r2: # top to bottom
            for r in range(r1, r2 + 1):
                points.add((r, c1))
        else: # bottom to top
            for r in range(r1, r2 - 1, -1):
                points.add((r, c1))
    
    return points

# why is it failing we must check all the points on the edge
max_area = 0
for i in range(len(points)):
    row, col = points[i]
    for j in range(i+1, len(points)):
        row2, col2 = points[j]
        row3, col3 = row, col2
        if not is_on_boundary( (row3, col3), points ) and not is_point_inside_polygon( (row3, col3 ), points ):
            continue
        row4, col4 = row2, col
        if not is_on_boundary( (row4, col4), points ) and not is_point_inside_polygon( (row4, col4 ), points ):
            continue
        if not are_edge_points_inside_or_boundary( [(row,col), (row2, col2), (row3,col3), (row4,col4)], points):
            continue
        height = abs(row-row2) + 1
        length = abs(col-col2) + 1
        max_area = max(max_area, height*length)
print(max_area) # Part 2: 1470616992 Takes too long xd