"""
Input: Vishnu
Output: unhsiV
"""

input = "Vishnu"


# Approach 1: Slicing
def string_reversal(s):
    return s[::-1]


# Approach 2: Loop
def string_reversal_2(s):
    result = []
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    return "".join(result)


print(string_reversal(input))
print(string_reversal_2(input))
