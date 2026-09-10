"""
Input: Vishnu
Output: Vowels:2, Consonants:4
"""

name_input = "Vishnu"


# Approach 1: Loop
def count_vowels_consonants(s):
    s = s.lower()

    vowels = 0
    consonants = 0

    for char in s:
        if char in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1
    return vowels, consonants


v, c = count_vowels_consonants(input)
print(f"Vowels:{v} Consonants:{c}")


# Approach 2: Comprehension
def count_vowels_consonants_2(s):

    vowels = [char for char in s.lower() if char in "aeiou"]
    consonants = [char for char in s.lower() if char not in "aeiou" and char.isalpha()]

    return vowels, consonants


v, c = count_vowels_consonants_2(input)
print(f"Vowels:{len(v)} Consonants:{len(c)}")
