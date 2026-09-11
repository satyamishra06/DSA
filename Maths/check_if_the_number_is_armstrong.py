"""
Problem: Check if the Number is Armstrong
Source: TakeUForward (Striver's A2Z DSA Sheet) | Difficulty: Easy
Link: https://takeuforward.org/plus/dsa/problems/check-if-the-number-if-armstrong?source=strivers-a2z-dsa-track

Approach:
First count the number of digits in n.
Then, for each digit, raise it to the power of (digit count) and sum them up.
If this sum equals the original number, it's an Armstrong number.

Time Complexity: O(d), where d = number of digits in n
Space Complexity: O(1)
"""

class Solution:
    def isArmstrong(self, n):
        original = n

        count = 0
        temp = n
        while temp > 0:
            temp = temp // 10
            count += 1

        temp = n
        total = 0
        while temp > 0:
            digit = temp % 10
            total = total + digit ** count
            temp = temp // 10

        if total == original:
            return True
        else:
            return False