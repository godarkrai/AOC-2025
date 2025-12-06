from collections import defaultdict

with open( 'Day6Input.txt' ) as f:
    lines = f.read().splitlines()

operations = lines[-1].split()
operations_dict = defaultdict(str)
numbers = []
numbers_part2 = []

for line in lines[:-1]:
    numbers.append(line.split())
rows = len(numbers)
cols = len(numbers[0])

def part1():

    result = defaultdict(int)
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if operations[j] == '*':
                if i == 0: 
                    result[j] = 1
                result[j] *= int(numbers[i][j])
            else:
                result[j] += int(numbers[i][j])
    return sum(result.values())

def part2():
    # Step 1: Put same column numbers in their own array
    for i, operator in enumerate(lines[-1]):
        operations_dict[i] = operator

    for line in lines[:-1]:
        for i, digit in enumerate(line):
            line = list(line)
            #print(i, digit, operations_dict[i])
            if line[i] == ' ':
                if i + 1 < len(line): # if its in the bounds
                    if operations_dict[i+1] not in ['*', '+']:
                        line[i] = '0'
        line = ''.join(line)
        numbers_part2.append(line.split())

    numbers_2 = defaultdict(list)
    for j in range(cols):
        for i in range(rows):
            numbers_2[j].append(numbers_part2[i][j])

    full_total = 0
    for key, value in numbers_2.items():
        new_value = defaultdict(list)
        for i in range(len(value)):
            for digit in range(len(value[i])-1,-1,-1):
                new_value[digit].append(value[i][digit])

        total = 1 if operations[key] == '*' else 0
        for _, digits in new_value.items():
            new_num = ''
            for d in digits:
                new_num += d if d != '0' else ''
            new_num = int(new_num)
            if operations[key] == '*':
                total *= new_num
            else:
                total += new_num
        full_total += total
    return full_total

print( "Part 1:", part1()) # Part 1: 4805473544166
print( "Part 2:", part2()) # Part 2: 8907730960817