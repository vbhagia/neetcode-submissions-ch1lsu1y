class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(0, len(nums)):
            for y in range(0, len(nums)):
                if nums[x] == nums[y]:
                    if x!=y:
                        return True
                    else:
                        pass
        return False
