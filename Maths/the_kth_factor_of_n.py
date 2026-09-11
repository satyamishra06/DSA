"""
Problem: The kth Factor of n
LeetCode #: 1492 | Difficulty: Medium
Link: https://leetcode.com/problems/the-kth-factor-of-n/

Approach:
Loop through numbers from 1 to n, counting how many of them divide n
evenly. Return the number as soon as the count reaches k. If the loop
finishes without reaching k, n has fewer than k factors, so return -1.

Time Complexity: O(n)
Space Complexity: O(1)

Note: Can be optimized to O(sqrt(n)) using divisor pairs (i, n // i).
"""

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        return -1