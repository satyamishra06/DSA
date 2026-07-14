class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = {}

        for row in grid:
            for num in row:
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1

        ans = [0,0]

        for i in range(1, n * n + 1):
            if count.get(i, 0) == 2:
                print("repeated:" , i)
                ans[0] = i

            if count.get(i, 0) == 0:
                print("missing:", i)
                ans[1] = i

        
        
        return ans