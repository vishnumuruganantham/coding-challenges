# Given an integer array nums, move all 0's to the end of it while maintaining the relative order
# of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


def move_zeroes_to_end(nums):
    """Returns the list with zeroes moved to end"""
    k = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[k] = nums[i]
            k += 1
    while k < len(nums):
        nums[k] = 0
        k += 1
    return nums


nums = [0, 1, 0, 3, 12]
print(move_zeroes_to_end(nums))

nums = [0]
print(move_zeroes_to_end(nums))
