"""
Problem: Find Greatest Common Divisor of Array
LeetCode #: 1979 | Difficulty: Easy
Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/

Approach:
The GCD of the whole array is just the GCD of its smallest and largest
elements. Find min and max, then apply the subtraction-based Euclidean
algorithm: repeatedly subtract the smaller from the larger until one
becomes 0 — the other is the GCD.

Time Complexity: O(n + max(a, b)), where n = len(nums) for min/max scan,
and the GCD loop is bounded by the value of the larger number
Space Complexity: O(1)

Note: The modulo-based Euclidean algorithm (a % b instead of a - b)
runs in O(log(min(a, b))) and is faster for large values.
"""

from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        a = smallest
        b = largest
        while a > 0 and b > 0:
            if a > b:
                a = a - b
            else:
                b = b - a

        if a == 0:
            return b
        else:
            return a