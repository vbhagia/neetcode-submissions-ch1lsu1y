class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We can precompute all of the things
        prefix = [1] * len(nums) # stores the product of every int before
        suffix = [1] * len(nums) # stores the product of every int after
        output = []
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        # multiply suffix and prefix at an each index to get output
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        return output