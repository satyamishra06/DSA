class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        largest = nums[-1]
        smallest = nums[0]
        ans=[]
        seen = set(nums)
        for i in range(smallest,largest):
            if i not in seen:
                ans.append(i)
        return ans     

       
       

                