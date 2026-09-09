"""Check if two strings are anagrams.

Input: "listen", "silent"
Output: True

Input: "Astronomer", "moon starer"
Output: True

Input: "hello", "helloo"
Output: False
"""


def is_anagram(s1, s2):

    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if not count.get(char):
            return False
        count[char] -= 1

    for value in count.values():
        if value != 0:
            return False

    return True


print(is_anagram("listen", "silent"))
print(is_anagram("Astronomer", "Moon starer"))  # Returns True (Normalized match)
print(is_anagram("apple", "paxle"))  # Returns False (Fails early on 'x')
print(is_anagram("hello", "hellooo"))  # Returns False (Fails length check)
