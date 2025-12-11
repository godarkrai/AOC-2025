with open( 'Day11Input.txt' ) as f:
    lines = f.read().splitlines()

from collections import defaultdict
graph = defaultdict(list)
for line in lines:
    line = line.split(': ')
    graph[line[0]] = line[1:][0].split()

def solve( node, end ):
    memo = {}
    def dfs(node):
        if node == end:
            return 1
        if node in memo:
            return memo[node]
        ans = 0
        for nei in graph[node]:
            ans += dfs(nei)
        memo[node] = ans
        return memo[node]
    return dfs(node)

ans = solve('you', 'out')
print("Part 1:", ans) # Part 1: 764

# for part 2 create 3 separate dfs
# svr->fft fft->dac dac->out
# svr->dac dac->fft fft->out
total = solve( 'svr', 'fft' )
total *= solve( 'fft', 'dac' )
total *= solve( 'dac', 'out' )

total2 = solve( 'svr', 'dac' )
total2 *= solve( 'dac', 'fft' )
total2 *= solve( 'fft', 'out' )

print( "Part 2:", total + total2 ) # Part 2: 462444153119850