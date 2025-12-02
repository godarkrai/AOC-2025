with open( 'Day2Input.txt' ) as f:
    input = f.read().splitlines()

ranges = []
for i in input:
    for range_ in i.split(','):
        if range_ != '':
            ranges.append(range_)

def part1():
    ans = 0
    for range_ in ranges:
        start, end = range_.split('-')
        for num in range(int(start), int(end)+1):
            num = str(num)
            if len(num)%2 != 0:
                continue
            half_point = len(num)//2
            if num[:half_point] == num[half_point:]:
                ans += int(num)
    return ans

def part2():
    ans = 0
    for range_ in ranges:
        start, end = range_.split('-')
        for num in range(int(start), int(end)+1):
            num = str(num)
            n = len(num)
            for i in range(1, n // 2 + 1):
                # start from index 1, if you cant divide the string into "i" parts then no need to continue
                if n % i != 0:
                    continue 
                # get the num string upto that index
                pattern = num[:i]
                # number of repeats you have to do to get the num
                repeats = n // i

                if pattern * repeats == num:
                    ans += int(num)
                    # There is only one invalid number, if ts 222222 doesnt matter if its 2 6 times or 22 3 times.
                    break
                
    return ans
print( "Part 1:", part1()) # 31000881061

print( "Part 2:", part2()) # 46769308485