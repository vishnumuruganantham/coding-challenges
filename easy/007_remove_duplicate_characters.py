"""
Remove duplicate characters
Input: hackearth
Output: hackert
"""

word_input = "hackearth"
# Approach 1: Using dictionary


def remove_duplicates(s):
    seen = {}
    result = []

    for char in s:
        if char not in seen:
            seen[char] = True
            result.append(char)

    return "".join(result)


print("Approach 1:", remove_duplicates(word_input))


# Approach 2: using dict.fromkeys which preserves order
def remove_duplicates_2(s):
    return "".join(list(dict.fromkeys(s)))


print("Approach 2:", remove_duplicates_2(word_input))
