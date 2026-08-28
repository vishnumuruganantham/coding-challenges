# Remove Duplicates from List
# Input: [1, 2, 2, 3, 3, 4]  |  Output: [1, 2, 3, 4]

# If order does NOT matter
nums = [1, 2, 2, 3, 3, 4]
unique = list(set(nums))  # [1, 2, 3, 4]

# If order MUST be preserved (Pythonic)
unique = list(dict.fromkeys(nums))  # [1, 2, 3, 4]


# Manual version preserving order
def remove_duplicates(nums):
    seen = set()  # Membership check is very fast in set
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
