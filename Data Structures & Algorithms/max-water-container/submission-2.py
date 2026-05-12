class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Can't sort this data
        # unsorted 2 pointers approach
        # O(n) time
        # O(1) space

        l = 0
        r = len(heights) - 1
        area = 0

        while l < len(heights) - 1:
            r = len(heights) - 1
            while r > l:
                if (min(heights[l], heights[r]) * (r - l)) > area:
                    area = (min(heights[l], heights[r]) * (r - l))
                r -= 1
            l += 1
        
        return area



        
        