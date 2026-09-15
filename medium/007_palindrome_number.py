# Given an integer x, return true if x is a palindrome, and false otherwise.


# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


# Constraints:

# -231 <= x <= 231 - 1


# Follow up: Could you solve it without converting the integer to a string?


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        s = str(x)
        return s == s[::-1]

    def is_palindrome_without_string(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x is None:
            return None

        # Negative numbers and numbers ending in 0 (except 0 itself) cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_number = 0

        # Reversing only the second half of the number to prevent integer overflow
        while x > reversed_number:
            reversed_number = (reversed_number * 10) + (x % 10)
            x = x // 10

        # Check if the first half and reversed second half match
        # x == reversed_number handles even-digit numbers (e.g., 1221 -> x=12, reversed=12)
        # x == reversed_number // 10 handles odd-digit numbers (e.g., 12321 -> x=12, reversed=123)
        return x == reversed_number or x == reversed_number // 10


solution_instance = Solution()

print(solution_instance.is_palindrome_without_string(1221), 1221)
print(solution_instance.is_palindrome_without_string(121), 121)
print(solution_instance.is_palindrome_without_string(900), 900)
print(solution_instance.is_palindrome_without_string(-100), -100)
print(solution_instance.is_palindrome_without_string(100), 100)
print(solution_instance.is_palindrome_without_string(1), 1)
print(solution_instance.is_palindrome_without_string(0), 0)
print(solution_instance.is_palindrome_without_string(None), None)
