class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            
            elif r - l <= 1:
                if nums[r] == target:
                    return r
                else:
                    return -1
            
            elif nums[m] < target:
                l = m
            
            elif nums[m] > target:
                r = m
        return -1