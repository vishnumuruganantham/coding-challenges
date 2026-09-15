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

print("----")


# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower().replace(" ", "")
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    def isPalindrome_2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("0P"))


print(Solution().isPalindrome_2("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome_2("0P"))
