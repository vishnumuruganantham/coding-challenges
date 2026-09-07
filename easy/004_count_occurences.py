# Frequency Counting: Write a script to find the exact count of occurrences of each letter/character in a string or unique strings in an array.

# Method 1: Using Counter
from collections import Counter

s = "StringgGs"


def count_frequency_1(s):
    count = Counter(s.lower())

    print(count)
    return count


count_frequency_1(s)


# Method 2: Manual using dictionary
def count_frequency_2(s):

    count = {}
    for char in s.lower():
        count[char] = count.get(char, 0) + 1
    print(count)
    return count


count_frequency_2(s)

# Method 3: Using comprehension
count = {char: s.lower().count(char) for char in s.lower()}
print(count)
