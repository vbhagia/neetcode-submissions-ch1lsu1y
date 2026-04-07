class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # I think I can make this into 1 big array...
        # Use the ends of each array as bin search "checkpoints"
        # Then bin search the array target is in
        
        l = 0
        r = len(matrix)

        which = 0
        while l <= r:
            m = (l + r)//2

            if l == m:
                which = m
                break

            if target == matrix[m][0]:
                return True
            
            if target < matrix[m][0]:
                r = m
            
            if target > matrix[m][0]:
                l = m

        l = 0
        r = len(matrix[which])

        while l <= r:
            m = (l + r)//2

            if target == matrix[which][m]:
                return True
            
            if l == m:
                break
            
            if matrix[which][m] < target:
                l = m
            
            if matrix[which][m] > target:
                r = m
        
        return False
            