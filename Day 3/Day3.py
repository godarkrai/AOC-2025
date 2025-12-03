with open( 'Day3Input.txt' ) as f:
    input = f.read().splitlines()

def jumping_window_max( nums, window_size, k ):
    left = 0
    n = len(nums)
    result = ''
    while left < n and len(result) < k:
        # window size should be minimum 1
        window_size = max(1, window_size)
        # end should be maximum at the len of the num string
        end = min(left+window_size,n)
        window = nums[left:end]
        max_ = max(window)
        result += max_
        max_index = window.index(max_)
        # the new window size should be shrinked because all the numbers
        # before this index is smaller and we don't need them but
        # should not be less than 1
        window_size = max(1, window_size - max_index)
        # the left index should now point to the max_index + 1
        # 2 3 5 3 4 if we need the max 2 cells -> 53 in this case
        # k = 2, window size = 5 - ( 2 - 1 ) = 5 - 1 = 4
        # window = 2 3 5 3 -> max = 5, new_window = 3 4
        # window = 3 4 -> max = 4 => max cell = 54
        left = left + max_index + 1

    return result

part = 1
for k in [2,12]:
    ans = 0
    for line in input:
        window_size = len(line) - ( k - 1 )
        ans += int( jumping_window_max(line, window_size, k) )
    print( "Part", part, ":", ans )
    part += 1
