# Rotate an array right by k — reversal trick
# Rotate [1,2,3,4,5] right by 2 → [4,5,1,2,3] .


def rotate(nums, k):
    """Rotates by k and returns the list."""
    length = len(nums)
    k = k % length
    reverse(nums, 0, length - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, length - 1)

    return nums


def reverse(nums, i, j):
    """Reverses sub array using the starting and ending indices alone"""

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


nums = [1, 2, 3, 4, 5]
k = 4

print(rotate(nums, k))
