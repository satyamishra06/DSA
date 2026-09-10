"""
Problem: GCD of Two Numbers
Source: TakeUForward (Striver's A2Z DSA Sheet) | Difficulty: Easy
Link: https://takeuforward.org/plus/dsa/problems/gcd-of-two-numbers?source=strivers-a2z-dsa-track

Approach:
Euclidean algorithm using repeated modulo instead of subtraction.
While both numbers are positive, reduce the larger one modulo the smaller.
Once one of them hits 0, the other is the GCD.

Time Complexity: O(log(min(n1, n2)))
Space Complexity: O(1)
"""

class Solution:
    def GCD(self, n1, n2):
        while n1 > 0 and n2 > 0:
            if n1 > n2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1

        if n1 == 0:
            return n2
        else:
            return n1