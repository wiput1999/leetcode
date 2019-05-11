"""
LeetCode : Palindrome Number (Easy)
Python 3
"""

class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            return False

        # A bit tricky in python lol
        if str(x) == str(x)[::-1]:
            return True
        return False