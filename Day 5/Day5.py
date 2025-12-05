with open( 'Day5Input.txt' ) as f:
    input = f.read().splitlines()

ranges = []
ingredients = []
ingredients_started = False
for i in input:
    if i == '':
        ingredients_started = True
        continue
    if ingredients_started == False:
        left, right = i.split('-')
        ranges.append([int(left), int(right)])
    else:
        ingredients.append(int(i))

total_fresh = 0

# we can merge intervals and do binary search to get the range in which the ingredient might be present
# for now lets brute force

for ingredient in ingredients:
    for left, right in ranges:
        if left <= ingredient <= right:
            total_fresh += 1
            # if we find the ingredient in any range just break out
            break
print( "Part 1:", total_fresh ) # Part 1: 726

# Part 2 -> Just merge intervals after sorting.
ranges.sort( key = lambda x:x[0] )
res = [ranges[0]]
for i in range(1, len(ranges)):
    if ranges[i][0] <= res[-1][1]:
        res[-1][1] = max( res[-1][1], ranges[i][1])
    else:
        res.append(ranges[i])

total_fresh = 0
for left, right in res:
    fresh = right - left + 1
    total_fresh += fresh
print( "Part 2:", total_fresh ) # Part 2: 354226555270043