"""
LeetCode : Valid Perfect Square (Easy)
Python 3
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num ** 0.5 % 1 == 0