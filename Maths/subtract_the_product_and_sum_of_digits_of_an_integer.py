"""
Problem: Subtract the Product and Sum of Digits of an Integer
LeetCode #: 1281 | Difficulty: Easy
Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

Approach:
Extract each digit of the number one by one (using % 10 and // 10).
Keep a running product and running sum of the digits.
Return product - sum after all digits are processed.

Time Complexity: O(d), where d = number of digits in n
Space Complexity: O(1)
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0

        while n > 0:
            digit = n % 10
            product = product * digit
            total = total + digit
            n = n // 10

        return product - total