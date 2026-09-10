"""
Group words by first letter
Input: ['apple','ant', ball','banana','cat']
Output: a=['apple','ant'], b=['ball','banana'], c=['cat]
"""

words = ["apple", "ant", "ball", "banana", "cat"]


def group_by_letter(words):
    group = {}

    for word in words:
        if word:  # Safety check to avoid IndexError on empty strings
            letter = word[0]

            if letter not in group:
                group[letter] = []

            group[letter].append(word)
    return group


print(group_by_letter(words))


# Approach using defaultdict
from collections import defaultdict


def group_by_letter_2(words):
    group = defaultdict(list)  # By default all keys will have empty list to start with

    for word in words:
        if word:  # Safety check to avoid IndexError on empty strings
            letter = word[0]
            group[letter].append(word)  # No need to check existence
    return dict(group)


print(group_by_letter_2(words))
