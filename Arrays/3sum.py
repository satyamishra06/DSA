class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = set()
        for i in range(0,n):
            s=set()
            for j in range(i+1,n):
                k = -(nums[i]+nums[j])
                if k in s:
                    temp =[nums[i],nums[j],k]
                    temp.sort()
                    result.add(tuple(temp))
                s.add(nums[j])

                
                
        return[list(ans)for ans in result]        