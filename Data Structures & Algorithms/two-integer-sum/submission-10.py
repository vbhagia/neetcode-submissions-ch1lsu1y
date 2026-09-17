class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Classic problem, classic solution
        # By iterating 1 time and using a hashmap
        # whose key is an integer in nums
        # and value is it's index
        # We have a solution that uses both O(n) time and space
        seen = dict()
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i