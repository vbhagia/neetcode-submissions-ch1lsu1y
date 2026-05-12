class Solution:
    def trap(self, height: List[int]) -> int:
        # water can be trapped between two walls
        # The amount of water that can be trapped is:
        # the min of the height of the walls
        # and the distance between the 'floor' and the wall in height

        # In order for water to be trapped at an index
        # There must be a greater value left and right of that index

        # prefix min and max for each i
        pre = []
        cur_max = 0
        for num in height:
            pre.append(cur_max)
            if num > cur_max:
                cur_max = num
        suff = []
        cur_max = 0
        for i in range(len(height) - 1, -1, -1):
            suff.append(cur_max)
            if height[i] > cur_max:
                cur_max = height[i]
        suff.reverse()

        print(pre)
        print(suff)

        # Calculate total water trapped at each position
        trapped = 0
        for i in range(len(height)):
            water_i = min(pre[i], suff[i]) - height[i]
            if water_i > 0:
                trapped += water_i
        
        return trapped
                
