class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n  =  len(nums)
        prefix = [0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1]+nums[i]
        total = prefix[-1]
        for i in range(n):
            if i == 0:
                left = 0
            else:
                left = prefix[i-1]
            right = total - prefix[i]

            if left ==  right:
                return i
        return -1       


          
