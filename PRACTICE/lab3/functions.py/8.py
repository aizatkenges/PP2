def find_first_zero(nums):
    for i, num in enumerate(nums):
        if num == 0:
            return i
    return None

def find_first_seven(nums, start_index):
    for i in range(start_index, len(nums)):
        if nums[i] == 7:
            return i
    return None

def spy_game(nums):
    pos_0 = find_first_zero(nums)
    if pos_0 is None:
        return False
    pos_7 = find_first_seven(nums, pos_0)
    if pos_7 is None:
        return False
    return find_first_zero(nums[pos_7:]) is not None

# Test cases
print(spy_game([1,2,4,0,0,7,5])) # True
print(spy_game([1,0,2,4,0,5,7])) # True
print(spy_game([1,7,2,0,4,5,0])) # False
