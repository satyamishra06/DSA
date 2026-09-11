"""
Problem: Three Divisors
LeetCode #: 1952 | Difficulty: Easy
Link: https://leetcode.com/problems/three-divisors/

Approach:
Count how many numbers from 1 to n divide n evenly.
If exactly 3 such divisors exist, return True (this happens only when
n is the square of a prime number).

Time Complexity: O(n)
Space Complexity: O(1)

Note: Can be optimized to O(sqrt(n)) by checking divisors up to sqrt(n)
and counting each pair (i, n // i) instead of looping through all of n.
"""

class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        if count == 3:
            return True
        return False