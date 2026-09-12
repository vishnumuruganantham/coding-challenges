# Find the Index of the First Occurrence in a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in
# haystack, or -1 if needle is not part of haystack.


# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if not haystack or not needle:
        #     return -1

        return haystack.find(needle)


solution_instance = Solution()
print(solution_instance.strStr("sadbutsad", "sad"))  # Output: 0
print(solution_instance.strStr("butsad", "sad"))  # Output: 3
print(solution_instance.strStr("leetcode", "leeto"))  # Output: -1
print(solution_instance.strStr("", "leeto"))  # Output: -1
print(solution_instance.strStr("leetcode", ""))  # Output: 0
