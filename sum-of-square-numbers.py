"""
LeetCode : Sum of Square Numbers (Easy)
Python 3
"""


class Solution:
    def judgeSquareSum(self, c):
        count = 0

        while count ** 2 <= c:
            # If I use given number - count ** 2 and then take root
            # If it not has decimal then it's sum of square
            if (c - count ** 2) ** 0.5 % 1 == 0:
                return True

            count += 1
        return False
