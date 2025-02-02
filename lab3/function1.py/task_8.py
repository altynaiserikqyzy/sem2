def spy_game(nums):
    zero = 0
    seven = 0
    for i in range(len(nums) - 1):
        if nums[i] == 0:
            zero += 1
        if nums[i] == 7:
            seven += 1
    if zero >= 2 and seven >= 1:
        return True
    return False

