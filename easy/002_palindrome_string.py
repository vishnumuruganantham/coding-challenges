"""Check if a string is a palindrome"""


def palindrome_1(word):
    return word == word[::-1]


print(palindrome_1("dad"))
print(palindrome_1("mom"))
print(palindrome_1("daddy"))
print(palindrome_1("mommy"))


def palindrome_2(word):
    """two pointer method"""
    i = 0
    j = len(word) - 1

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


print(palindrome_2("dad"))
print(palindrome_2("mom"))
print(palindrome_2("daddy"))
print(palindrome_2("mommy"))
