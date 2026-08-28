# Problem 1: Two Sum
# Input: [2, 7, 11, 15], target = 9  |  Output: indices [0, 1] (2 + 7 = 9)
# Very common interview problem. The dict approach is expected.


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in seen:
            return [seen[compliment], i]
        seen[num] = i
    return None


print(two_sum([2, 7, 11, 15], 9))
