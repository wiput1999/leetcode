"""
LeetCode : String to Integer (atoi) (Medium)
Python 3
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        num = ''
        # remove left spaces
        str = str.lstrip(' ')

        # check empty string
        if (not str):
            return 0

        # check minus/plus signs
        if (str[0] == '-' or str[0] == '+'):
            num = str[0]
            str = str[1:]

        # check digits
        for ch in str:
            if (ch.isdigit()):
                num += ch
            else:
                break

        try:
            value = int(num)
            # check overflow
            if (value.bit_length() >= 32):
                return (2**31-1) if value > 0 else -2**31
            return value
        except ValueError:
            return 0
