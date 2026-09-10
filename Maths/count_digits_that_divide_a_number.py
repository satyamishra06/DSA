"""
Problem: Count the Digits That Divide a Number
LeetCode #: 2520 | Difficulty: Easy
Link: https://leetcode.com/problems/count-the-digits-that-divide-a-number/
 
Approach:
Extract each digit of the number one by one (using % 10 and // 10).
For every non-zero digit, check if it divides the original number evenly.
Count how many digits satisfy this condition.
 
Time Complexity: O(d), where d = number of digits in num
Space Complexity: O(1)
"""
 
class Solution:
    def countDigits(self, num: int) -> int:
        original = num
        count = 0
 
        while num > 0:
            digit = num % 10
            if digit != 0 and original % digit == 0:
                count += 1
            num = num // 10
        return count