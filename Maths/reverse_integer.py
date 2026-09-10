"""
Problem: Reverse Integer
LeetCode #: 7 | Difficulty: Medium
Link: https://leetcode.com/problems/reverse-integer/

Approach:
Store the sign separately and work with the absolute value of x.
Build the reversed number digit by digit (reverse = reverse * 10 + digit).
Reapply the sign, then check the result fits in a signed 32-bit integer
range [-2^31, 2^31 - 1]; if it overflows, return 0.

Time Complexity: O(d), where d = number of digits in x
Space Complexity: O(1)
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        reverse = 0
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        reverse = reverse * sign

        if -2**31 <= reverse < 2**31 - 1:
            return reverse
        return 0