"""
Remove duplicate characters
Input: hackearth
Output: hackert
"""

input = "hackearth"
# Approach 1: Using dictionary


def remove_duplicates(s):
    seen = {}
    result = []

    for char in s:
        if char not in seen:
            seen[char] = True
            result.append(char)

    return "".join(result)


print("Approach 1:", remove_duplicates(input))


def remove_duplicates_2(s):
    print(set(s))
    print(dict.fromkeys(s))
    print(list(dict.fromkeys(s)))
    return "".join(list(dict.fromkeys(s)))


print("Approach 2:", remove_duplicates_2(input))
