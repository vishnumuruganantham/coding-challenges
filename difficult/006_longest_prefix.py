# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


class Solution(object):

    # Vertical Scanning
    def longestCommonPrefix_1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Loop through the characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Check this character against all other strings
            for s in strs:
                # If the string is shorter than index i, or character doesn't match
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]

    # Sorting elimination
    def longestCommonPrefix_2(self, strs):
        if not strs:
            return ""

        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]

    # Horizontal Scanning
    def longestCommonPrefix_3(self, strs):
        if not strs:
            return ""

        # Start by assuming the first string is the prefix
        prefix = strs[0]

        # Compare this prefix with every other string one by one
        for s in strs[1:]:
            # Truncate prefix until it matches the start of string s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


solution_instance = Solution()
print(solution_instance.longestCommonPrefix_1(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_1(["12", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_1(["abc", "a", "ab"]))
print(solution_instance.longestCommonPrefix_1(["abcde", "abcde", "adbce"]))
print(solution_instance.longestCommonPrefix_1(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_1(["", "flow", "floght"]))
print("---")
print(solution_instance.longestCommonPrefix_2(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_2(["12", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_2(["abc", "a", "ab"]))
print(solution_instance.longestCommonPrefix_2(["abcde", "abcde", "adbce"]))
print(solution_instance.longestCommonPrefix_2(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_2(["", "flow", "floght"]))
print("---")
print(solution_instance.longestCommonPrefix_3(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_3(["12", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_3(["abc", "a", "ab"]))
print(solution_instance.longestCommonPrefix_3(["abcde", "abcde", "adbce"]))
print(solution_instance.longestCommonPrefix_3(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_3(["", "flow", "floght"]))
print("---")
