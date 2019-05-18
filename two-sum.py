"""
LeetCode : Two Sum (Easy)
Python 3
"""


class Solution:
    def twoSum(self, nums, target):
        for index, number in enumerate(nums):
            expected = target - number
            if expected in nums:
                expected_index = nums.index(expected)
                if expected_index == index:
                    continue
                return sorted([index, expected_index])
        return []
