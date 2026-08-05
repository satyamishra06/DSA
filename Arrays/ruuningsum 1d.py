class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(nums)
        ans =[nums[0]]
        runningSum = nums[0]
        
        for i in range(1,n):
            runningSum += nums[i]
            
            
            ans.append(runningSum)
        return ans  

            
