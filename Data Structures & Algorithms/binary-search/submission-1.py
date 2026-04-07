class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if (r - l) <= 1:
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r
                else:
                    return -1
                break

            m = (l + r)//2

            if nums[m] == target:
                return m
                break
            if nums[m] < target:
                l = m
            if nums[m] > target:
                r = m

            

        