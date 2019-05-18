"""
LeetCode : Reverse Integer (Easy)
Python 3
"""


class Solution:
    def reverse(self, x):
        # boolean if x < 0
        minus = x < 0

        # multiply -1 to negative
        if minus:
            x *= -1

        x = int(str(x)[::-1])

        # As problem spec result must in range otherwise return 0
        if x not in range(-2 ** 31, 2 ** 31):
            return 0

        return -x if minus else x
