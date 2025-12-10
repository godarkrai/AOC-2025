with open('Day10Input.txt') as f:
    input = f.read().splitlines()

from collections import defaultdict, deque
config = defaultdict(list)
for line in input:
    line = line.split( ' ' )
    config['pattern'].append(line[0].replace('[','').replace(']',''))
    switches = []
    for switch in line[1:len(line)-1]:
        switch = list(map(int, switch.replace('(','').replace(')','').split(',')))
        switches.append(switch)
    config['switches'].append(switches)
    joltages = list(map(int, line[-1].replace('{', '').replace('}', '').split(',')))
    config['joltage'].append(joltages)

# starting pattern = [....] (equal to the pattern length for each config)
# ending pattern = config['pattern'] -> [ .##. ]
# intuition: try every switch at each pattern point to try and reach the final pattern
# since we have to do it in minimal steps -> BFS

from ortools.linear_solver import pywraplp

def solve_machine(buttons, targets):
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return None
    
    # Create variables: how many times to press each button
    num_buttons = len(buttons)
    x = [solver.IntVar(0, solver.infinity(), f'x_{i}') for i in range(num_buttons)]
    
    # Constraints: each counter must reach its target
    num_counters = len(targets)
    for counter in range(num_counters):
        constraint = solver.Constraint(targets[counter], targets[counter])
        for button_idx, button in enumerate(buttons):
            if counter in button:
                constraint.SetCoefficient(x[button_idx], 1)
    
    # Objective: minimize total button presses
    objective = solver.Objective()
    for i in range(num_buttons):
        objective.SetCoefficient(x[i], 1)
    objective.SetMinimization()
    
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        return int(objective.Value())
    return None

def solve( part ):
    n = len(input)
    total = 0
    for i in range(n):
        switches = config['switches'][i]
        if part == 2: # ILP, no idea how to do it.
            target = config['joltage'][i]
            ret = solve_machine(switches, target)
            total += ret
        else: # BFS with step counter
            target = config['pattern'][i]
            starting = '.' * len(target)
            steps = 0
            q = deque()
            q.append((starting, steps))
            visited = set()
            while q:
                current, steps = q.popleft()
                if current == target:
                    break
                for switch in switches:
                    next = list(current)
                    for index in switch: # like (0,1) => turn current index to not index
                        next[index] = '.' if current[int(index)] == '#' else '#'
                    next = ''.join(next)
                    if next not in visited:
                        q.append((next, steps+1))
                        visited.add(next)
            total += steps
    return total
print("Part 1:", solve(1)) # Part 1: 375
print("Part 2:", solve(2)) # Part 2: 15377