# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.


# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or not intervals[0]:
            return []

        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output


print(Solution().merge([[1, 4], [4, 5], [5, 8], [6, 8], [7, 11], [10, 12], [11, 13]]))
print(Solution().merge([[1, 4], [5, 6], [5, 8], [6, 8], [7, 11], [10, 12], [15, 20]]))
print(Solution().merge([[15, 20], [1, 4], [5, 6], [5, 8], [6, 8], [7, 11], [10, 12]]))
print(Solution().merge([]))
