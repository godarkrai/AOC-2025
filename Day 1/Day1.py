
with open( 'Day1.txt' ) as f:
    input = f.read().splitlines()

starting = 50
password = 0
crossed_zero = 0
for i in input:
    direction = i[:1]
    amount = int( i[1:] )
    if direction == 'L':
        x = starting - amount
    else:
        x = starting + amount
    if x > 0:
        crossed_zero += x // 100
    elif x == 0:
        crossed_zero += 1
    else:
        crossed_zero += ((100-starting) % 100 + abs(amount)) // 100
    new_pos = x % 100
    starting = new_pos
    if ( starting == 0 ):
        password += 1
print( "Part 1:", password ) # Part 1: 1031
print( "Part 2:", crossed_zero ) # Part 2: 5831