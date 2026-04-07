class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force (O(n^2))
        output = 0
        l = 0
        r = len(heights) - 1

        while l < (len(heights) - 1):
            while r > l:
                curr_cap = ((r - l) * (min(heights[l], heights[r])))
                if curr_cap > output:
                    output = curr_cap
                r = r - 1
            l = l + 1
            r = len(heights) - 1
        
        return output


        
        