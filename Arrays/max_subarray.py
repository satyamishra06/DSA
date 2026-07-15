class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = nums[0]
        current_sum =0
        for i in range(0,n):
            current_sum += nums[i]
            maximum = max(maximum, current_sum)
            if current_sum<0:
                current_sum =0
        return maximum        
