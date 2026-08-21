class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        left = 0
        result = 0
        window = {}

        for right in range(n):

            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            while window[s[right]] > 1:
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            length = right - left + 1

            if length > result:
                result = length

        return result