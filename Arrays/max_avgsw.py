class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window  = sum(nums[:k])
        maximum = window
        for i in range(k,len(nums)):
            window   -= nums[i-k]
            window += nums[i]
            maximum = max(maximum, window)
        return maximum/k  

      
        