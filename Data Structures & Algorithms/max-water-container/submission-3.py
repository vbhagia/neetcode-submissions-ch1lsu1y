class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Can't sort this data
        # unsorted 2 pointers approach
        # O(n) time
        # O(1) space

        l = 0
        r = len(heights) - 1
        area = 0

        while l < r:
            cur_area = min(heights[l], heights[r]) * (r - l)
            if cur_area > area:
                area = cur_area
            if heights[l] >= heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1      
        return area



        
        