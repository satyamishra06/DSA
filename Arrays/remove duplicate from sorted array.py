class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for right in range(1,len(nums)):
            if nums[right]!=nums[right-1]:
                
                nums[l]=nums[right]
                l+=1
            
        return l        