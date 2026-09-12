"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {"}": "{", ")": "(", "]": "["}
        stack = []
        if not s:
            return False

        for char in s:
            if char in brackets:
                if not stack or stack.pop() != brackets[char]:
                    return False
            elif char in "[{(":
                stack.append(char)

        return not stack


instance = Solution()

print(instance.isValid("[]"))
print(instance.isValid(None))
print(instance.isValid("[]]"))
print(instance.isValid("{{{)}}}"))
print(instance.isValid("[]{}(){}]"))
print(instance.isValid("{{{[](){}()}}}"))
print(instance.isValid("}"))
