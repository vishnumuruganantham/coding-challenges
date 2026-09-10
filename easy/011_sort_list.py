"""Sort a list
Input: [5,3,8,1,9]
Output: [1,3,5,8,1,9]
"""

numbers = [5, 3, 8, 1, 9]


def sort(nums):
    nums.sort()  # list.sort(), sorts in place
    return nums


def sort_1(nums):
    output = sorted(nums)  # sorted(list) returns a new sorted array
    return output


def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(numbers)
print(sort(numbers))
print(sort_1(numbers))
print(bubble_sort(numbers))
