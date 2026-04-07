class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Bin search to find which subarray we're in
        # Bin search again within the subarray to find the elem

        l = 0
        r = len(matrix) - 1
        which = 0 # Placeholder for subarray
        while l <= r:
            if l == r:
                which = l
                break

            if l == (r - 1):
                if matrix[r][0] <= target:
                    which = r
                    break
                else:
                    which = l
                    break

            m = (l + r)//2

            if matrix[m][0] > target:
                r = m
            
            if matrix[m][0] <= target:
                if matrix[m + 1][0] > target:
                    which = m
                    break
                else:
                    l = m
        
        # 2nd bin search
        l = 0
        r = len(matrix[which]) - 1
        while l <= r:
            

            m = (l + r)//2

            if l == m: # This will handle r - l = 1, and r = l
                if matrix[which][l] == target:
                    return True
                elif matrix[which][r] == target:
                    return True
                else:
                    return False
            
            if matrix[which][m] == target:
                return True
            
            if matrix[which][m] < target:
                l = m
            
            if matrix[which][m] > target:
                r = m
        
        return False


         

