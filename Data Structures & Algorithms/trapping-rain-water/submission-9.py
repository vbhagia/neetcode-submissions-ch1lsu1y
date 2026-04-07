class Solution:
    def trap(self, height: List[int]) -> int:
        # Track the walls from the left and right of any position in height
        maxLeft = []
        for i in range(1, len(height) + 1):
            maxLeft.append(max(height[0:i]))
        
        maxRight = []
        for i in range(len(height) - 1):
            maxRight.append(max(height[i:len(height)]))
        maxRight.append(0)
        
        # Track the shortest wall at each index
        minLR = []
        for i in range(len(height)):
            minLR.append(min(maxLeft[i], maxRight[i]))
        
        # sum the water
        water = 0
        for i in range(len(height)):
            curr_water = minLR[i] - height[i]
            if curr_water > 0:
                water += curr_water
        
        return water


            
        