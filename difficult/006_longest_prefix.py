class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = [len(s) for s in strs]
        smallest = min(length)
        for i in range(smallest + 1):
            prefix = strs[0][0:i]
            for s in strs:
                if s.find(prefix) != 0:
                    return prefix[: len(prefix) - 1]

        return prefix

    def longestCommonPrefix_2(self, strs):
        if not strs:
            return ""

        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]

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
print(solution_instance.longestCommonPrefix(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix(["12", "flow", "floght"]))
print(solution_instance.longestCommonPrefix(["abc", "a", "ab"]))
print(solution_instance.longestCommonPrefix(["abcde", "abcde", "adbce"]))
print(solution_instance.longestCommonPrefix(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix(["", "flow", "floght"]))


print(solution_instance.longestCommonPrefix_2(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_2(["12", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_2(["abc", "a", "ab"]))
print(solution_instance.longestCommonPrefix_2(["abcde", "abcde", "adbce"]))
print(solution_instance.longestCommonPrefix_2(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_2(["", "flow", "floght"]))


print(solution_instance.longestCommonPrefix_3(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_3(["12", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_3(["abc", "a", "ab"]))
print(solution_instance.longestCommonPrefix_3(["abcde", "abcde", "adbce"]))
print(solution_instance.longestCommonPrefix_3(["flower", "flow", "floght"]))
print(solution_instance.longestCommonPrefix_3(["", "flow", "floght"]))
