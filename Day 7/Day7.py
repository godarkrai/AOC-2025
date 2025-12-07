with open( 'Day7Input.txt' ) as f:
    lines = f.read().splitlines()

from collections import deque

tachyon = []
for line in lines:
    tachyon.append(list(line))

splitter_locations = set()
first_splitter = None
for i, t in enumerate(tachyon):
    for j, cell in enumerate( t ):
        if cell == '^':
            splitter_locations.add((i,j))
            if first_splitter is None:
                first_splitter = (i,j)

total_splits = 0
splitted = set()
points = deque()
points.append(first_splitter)
while points:
    x, y = points.popleft()
    if ( x,y ) in splitter_locations:
        total_splits += 1
    # do two loops for rows for each +1, -1 column?
    for i in range(x+2, len(tachyon)): # traverse all the rows for +1 ,-1 column until first splitter
        if ( i, y-1 ) in splitter_locations:
            if (i,y-1) not in splitted:
                splitted.add((i,y-1))
                points.append((i,y-1))
                #print( "left splitter from (", x,",",y, ")found at (",i,",",y-1,")")
            break # break at first right splitter whether already splitted or not
    for i in range(x+2, len(tachyon)):
        if ( i, y+1 ) in splitter_locations:
            if (i,y+1) not in splitted:
                splitted.add((i,y+1))
                points.append((i,y+1))
                #print( "right splitter from (", x,",",y, ")found at (",i,",",y+1,")")
            break # break at first right splitter whether already splitted or not
print("Part 1:", total_splits) # Part 1 1667

# Part 2: Combinations
# DFS until end with +1 or -1 values
# basically traversing a tree!??
# root = first splitter

def find_next_splitter(x,y):
    for nx in range(x + 2, len(tachyon), 2):
        if (nx, y) in splitter_locations:
            return nx
    return None

memo = {}
def dfs(x, y):
    # If we've fallen off the bottom one successful timeline
    if x >= len(tachyon):
        return 1
    key = (x,y)
    if key in memo:
        return memo[key]
    # If current coordinate is a splitter branch left and right
    if key in splitter_locations:
        ans = dfs(x + 2, y - 1) + dfs(x + 2, y + 1)
    else:
    # Otherwise jump to next splitter in this column (if any)
        new_x = find_next_splitter(x, y)
        ans = 1 if new_x is None else dfs(new_x, y)
    memo[key] = ans
    return ans

timelines = dfs(first_splitter[0], first_splitter[1])
print("Part 2:", timelines) # Part 2: 62943905501815