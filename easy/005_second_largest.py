"""Find the second-largest value in one pass."""


def find_second_largest(nums):
    """Return the second largest number from the list"""

    largest = float("-inf")
    second_largest = float("-inf")

    for num in nums:

        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num

    print(second_largest)


find_second_largest([1, 2, 50, 4, 5, 6])
