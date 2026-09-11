"""
Problem: Count Primes
LeetCode #: 204 | Difficulty: Medium
Link: https://leetcode.com/problems/count-primes/

Approach:
Sieve of Eratosthenes. Create a boolean array is_prime of size n, initially
assuming every number is prime. Mark 0 and 1 as not prime. For every prime
i starting from 2 up to sqrt(n), mark all its multiples (starting from i*i)
as not prime. Count how many indices remain True.

Time Complexity: O(n log log n)
Space Complexity: O(n)
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)