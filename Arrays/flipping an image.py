class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
    
        for row in image:
            row.reverse()
            for i in range (n):
                if row[i] == 1:
                    row[i]=0
            
               
                else:
                    row[i]=1
        return image       

            
        