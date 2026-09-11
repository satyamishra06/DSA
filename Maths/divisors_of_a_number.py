"""
Problem: Divisors of a Number
Source: TakeUForward (Striver's A2Z DSA Sheet) | Difficulty: Easy
Link: https://takeuforward.org/plus/dsa/problems/divisors-of-a-number?source=strivers-a2z-dsa-track

Approach:
Loop through every number i from 1 to n, and print i if it divides n evenly.

Time Complexity: O(n)
Space Complexity: O(1)

Note: Can be optimized to O(sqrt(n)) by checking divisors up to sqrt(n)
and printing both i and n // i for each match.
"""

class Solution:
    def divisors(self, n):
        for i in range(1, n + 1):
            if n % i == 0:
                print(i)