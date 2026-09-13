# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return None

        new = [str(d) for d in digits]
        num = int("".join(new))
        num += 1

        result = list(str(num))
        result = [int(d) for d in result]
        return result

    def plusOne_2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return None

        number = 0
        for num in digits:
            number = number * 10 + num

        number = number + 1
        result = []
        while number != 0:
            digit = number % 10
            number = number // 10
            result.append(digit)

        return result[::-1]


print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne(None))
print(Solution().plusOne([9]))
print(Solution().plusOne([1, 1, 9]))

print("---")

print(Solution().plusOne_2([1, 2, 3]))
print(Solution().plusOne_2(None))
print(Solution().plusOne_2([9]))
print(Solution().plusOne_2([1, 1, 9]))
